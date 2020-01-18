from .BaseEventHandler import BasicActionHandler


class GreetingHandler(BasicActionHandler):
    ID = 'greeting'
    DEF_RIGTHS = True
    CMD = ['sethello', 'приветствие']

    DEFAULT_MSG = (
        "Приветствую тебя впервые в нашей беседе! "
        "Твой аккаунт зарегистрирован, [id{id}|{name}]!"
    )

    def handle(self, event):
        data = self._data
        peer = str(event['peer_id'])

        if peer in data:
            msg = data[peer]
        else:
            msg = self.DEFAULT_MSG

        if (event['action'] is not None or
           event['message'].lower().startswith('приветствие')):
            id = (event['from_id'] if event['action'] is None
                  else event['action']['member_id'])

            self.harley.send_msg(
                peer,
                message=self.message(event, msg=msg, id=id, args=[])
            )

        elif event['is_admin']:
            if event['message'].lower().startswith('sethello'):
                hello_msg = event['message'].split(' ', 1)[1:][0]
                data[peer] = hello_msg

                self.harley.send_msg(
                    peer,
                    message="Приветствие установлено!"
                )

    def trigger(self, event):
        if event['action'] is not None:
            if event['action']['type'] in ['chat_invite_user',
                                           'chat_invite_user_by_link']:
                return True

        return super().trigger(event)
