import vk_api.vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import audio

import random
import json
import threading
import traceback

from EventHandlerHelper import build_handler_list
from Handlers.Admin.RightsHandler import RightsHandler

from Pools.ArtsPool import ArtsPool


class HarleyBot:
    def __init__(self, api_token, group_id, creator_id=0):
        self.data = {}

        self.creator_id = int(creator_id)

        self.vk_session = vk_api.VkApi(token=api_token)
        self.vk_api = self.vk_session.get_api()
        self.long_poll = VkBotLongPoll(self.vk_session, group_id)

        self.rights_handler = RightsHandler(self)

        self.handlers = build_handler_list(self, [
            self.rights_handler,
        ])

        self.__stop = False
        self.__lock = threading.Lock()

        self.arts_pool = ArtsPool(self)

    @staticmethod
    def __filter_event(event):
        if 'action' in event.obj.message:
            return True
        if event.obj.message['text'].lower().startswith('харли. '):
            return True
        if event.obj.message['text'].lower().startswith('харли, '):
            return True
        if event.obj.message['text'].lower().startswith('harli. '):
            return True
        if event.obj.message['text'].lower().startswith('harli, '):
            return True

        return False

    def __start_console(self):
        print('Entered console mode')
        stop = False

        while not stop:
            cmd = input('> ')
            args = cmd.split()

            if cmd == 'quit' or cmd == 'stop':
                with self.__lock:
                    self.__stop = True

                print('Stoping...')

            elif cmd == 'data':
                print(self.data)

            elif args[0] == 'promote' and len(args) == 2:
                self.get_data_list(['admins']).append(int(args[1]))

            elif args[0] == 'save' and len(args) == 2:
                self.save(str(args[1]))

            with self.__lock:
                stop = self.__stop

    def start(self):
        self.__stop = False
        console = threading.Thread(target=self.__start_console, daemon=True)
        console.start()

        stop = False
        while not stop:
            try:
                for event in self.long_poll.check():
                    if not self.__filter_event(event):
                        continue
                    if event.type != VkBotEventType.MESSAGE_NEW:
                        continue

                    _event = self.__cleanup_event(event)
                    is_admin = self.is_admin(
                        _event['peer_id'],
                        _event['from_id']
                    )

                    handler = next(
                        (
                            h for h in self.handlers
                            if (
                                is_admin or
                                self.rights_handler.has_rights(
                                    h,
                                    _event['from_id'],
                                    _event['peer_id']
                                )
                            ) and
                            h.trigger(_event)
                        ),
                        None
                    )

                    if handler is not None:
                        handler.handle(_event)

            except Exception as e:
                print(e)
                traceback.print_exc()

            with self.__lock:
                stop = self.__stop

        console.join()

    def get_data_table(self, path):
        res = self.data

        for node in path:
            if not (str(node) in res):
                res[str(node)] = {}
            res = res[str(node)]

        return res

    def get_data_list(self, path):
        if len(path) < 1:
            return []

        res = self.get_data_table(path[:-1])
        if not (str(path[-1]) in res):
            res[str(path[-1])] = []

        return res[str(path[-1])]

    @staticmethod
    def __cleanup_event(event):
        res = {
            'date': event.obj.message['date'],
            'from_id': event.obj.message['from_id'],
            'id': event.obj.message['id'],
            'out': event.obj.message['out'],
            'peer_id': event.obj.message['peer_id'],
            'message': event.obj.message['text'],
            'conversation_message_id': event.obj.message['conversation_message_id'],
            'fwd_messages': event.obj.message['fwd_messages'],
            'important': event.obj.message['important'],
            'random_id': event.obj.message['random_id'],
            'attachments': event.obj.message['attachments'],
            'is_hidden': event.obj.message['is_hidden'],
        }

        if 'action' in event.obj.message:
            res['action'] = event.obj.message['action']
            res['args'] = []
        else:
            res['action'] = None
            res['message'] = ' '.join(res['message'].split()[1:])
            res['args'] = res['message'].split()

        return res

    def send_msg(self, peer_id, message=None, attachment=None, disable_mentions=None):
        self.vk_api.messages.send(
            peer_id=int(peer_id),
            message=message,
            attachment=attachment,
            random_id=random.randint(-2135425010, 2135425010),
            disable_mentions=disable_mentions
        )

    def user_id(self, screen_name):
        if screen_name.startswith('https://vk.com/'):
            user = screen_name[15:]
        elif screen_name.startswith('[id'):
            user = screen_name.split('|')[0][1:]
        elif screen_name.startswith('id'):
            user = str(screen_name)
        else:
            user = 'id' + screen_name
        return self.vk_api.utils.resolveScreenName(screen_name=user)['object_id']

    __uinfo = {}
    __USER_FIELDS = 'sex,first_name,last_name'

    def user_info(self, user_id):
        if not (user_id in self.__uinfo):
            self.__uinfo[user_id] = self.vk_api.users.get(user_ids=user_id, fields=self.__USER_FIELDS)[0]
        return self.__uinfo[user_id]

    def members(self, peer_id):
        res = self.vk_api.messages.getConversationMembers(peer_id=peer_id, fields=self.__USER_FIELDS)
        for user in res['profiles']:
            if not (user['id'] in self.__uinfo):
                self.__uinfo[user['id']] = user

        return [item for item in res['items'] if item['member_id'] > 0]

    def is_admin(self, peer_id, user_id):
        admins = [item['member_id'] for item in self.members(peer_id) if 'is_admin' in item and item['is_admin']]

        admins.extend(self.get_data_list(['peers', str(peer_id), 'admins']))
        admins.extend(self.get_data_list(['admins']))
        admins.append(self.creator_id)

        return user_id in admins

    def save(self, filename):
        with open(filename, 'w', encoding='utf-8') as fout:
            json.dump(self.data, fout, indent=4, ensure_ascii=False)

    def load(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as fin:
                self.data = json.load(fin)
        except IOError:
            pass
