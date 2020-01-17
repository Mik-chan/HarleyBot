from ..BaseEventHandler import BaseEventHandler


class RightsHandler(BaseEventHandler):
    ID = '_admin_rights'
    CMD = 'rights'

    def handle(self, event):
        args = event['args']

        access = args[1].lower() == 'promote'
        handler = args[2]
        user_id = self.harley.user_id(args[3])
        peer_id = event['peer_id']
        if len(args) >= 5:
            peer_id = args[4]

        self.set_rigths(access, handler, user_id, peer_id)

        if access:
            msg = "Команда {} была добавлена пользователю {}"
        else:
            msg = "Команда {} была убрана у пользователя {}"

        self.harley.send_msg(
            event['peer_id'],
            message=msg.format(handler, user_id)
        )

    def set_rigths(self, access, handler, user_id, peer_id=None):
        if peer_id is None:
            peer_id = 'global'

        rights_table = self._get_data([peer_id, user_id])
        rights_table[str(handler)] = access

    def has_rights(self, handler, user_id, peer_id=None):
        if peer_id is not None:
            rights_table = self._get_data([peer_id, user_id])
            if str(handler) in rights_table:
                return rights_table[str(handler)]

        rights_table = self._get_data(['global', user_id])
        if str(handler) in rights_table:
            return rights_table[str(handler)]

        return handler.DEF_RIGTHS
