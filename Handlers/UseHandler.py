from .BaseEventHandler import BaseEventHandler


class UseHandler(BaseEventHandler):
    ID = 'use'
    CMD = 'use'
    MIN_ARGS = 1

    def handle(self, event):
        self.harley.send_msg(
            event['peer_id'],
            message=self.harley.user_id(event['args'][1])
        )
