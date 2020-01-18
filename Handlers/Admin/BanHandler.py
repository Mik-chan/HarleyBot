from ..BaseEventHandler import BaseEventHandler


class BanHandler(BaseEventHandler):
    ID = '_admin_ban'
    CMD = ['бан', 'разбан']
    DEF_RIGTHS = True

    MIN_ARGS = 1

    def handle(self, event):
        data = self._data
        where = str(event['peer_id'])
        if where not in data:
            data[where] = []

        if event['action'] is not None:
            who = str(event['action']['member_id'])
            if who in data[where]:
                self.harley.kick(int(where) - 2000000000, who)
            return

        if not event['is_admin']:
            return

        cmd = event['args'][0]
        who = str(self.harley.user_id(event['args'][1]))

        if cmd == 'бан':
            data[where].append(who)
            self.harley.send_msg(
                event['peer_id'],
                message="Пользователь @id{} теперь в бане.".format(who)
            )
            self.harley.kick(int(where) - 2000000000, who)

        elif cmd == 'разбан':
            data[where] = [a for a in data[where] if a != who]
            self.harley.send_msg(
                event['peer_id'],
                message="Пользователь @id{} теперь не бане.".format(who)
            )

    def trigger(self, event):
        if event['action'] is not None:
            if event['action']['type'] in ['chat_invite_user',
                                           'chat_invite_user_by_link']:
                return True
        return super().trigger(event)
