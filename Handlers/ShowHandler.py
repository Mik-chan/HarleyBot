from .BaseEventHandler import BasicActionHandler


class ShowHandler(BasicActionHandler):
    ID = 'show'
    DEF_RIGTHS = True

    CMD = "показать"
    MSG = "[id{id}|{name}] показал{sex} {str_args}"

    SEX_M = ''
    SEX_F = 'а'

    def handle(self, event):
        msg = self.message()

        img = None
        if len(event['args']) > 1:
            if event['args'][1] == 'сиськи':
                img = self.harley.arts_pool.random('show_tits')

        self.harley.send_msg(
            event['peer_id'], message=msg, attachment=img
        )
