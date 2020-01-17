from .BaseEventHandler import BaseEventHandler


class UseHandler(BaseEventHandler):
    ID = 'use'
    CMD = 'use'

    def handle(self, event):
        self.harley.send_msg(
            event['peer_id'],
            message="Args: " + ", ".join(event['args'])
        )
