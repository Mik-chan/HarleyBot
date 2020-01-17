from .BaseEventHandler import BasicActionHandler


class BecomeHandler(BasicActionHandler):
    ID = 'become'
    DEF_RIGTHS = True

    CMD = "стать"
    MSG = "[id{id}|{name}] стал{sex} {args}"

    SEX_M = ''
    SEX_F = 'а'

    def handle(self, event):
        msg = self.message()

        img = None
        if len(event['args']) > 1:
            if event['args'][1] == 'котом':
                img = self.harley.arts_pool.random('become_cat')
            elif event['args'][1] == 'мачо':
                img = self.harley.arts_pool.random('become_macho')
        
        self.harley.send_msg(
            event['peer_id'], message=msg, attachment=img
        )
