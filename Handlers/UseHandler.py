from .BaseEventHandler import BaseEventHandler


class UseHandler(BaseEventHandler):
    ID = 'use'

    def handle(self, event):
        self.harley.send_msg(
            event['peer_id'],
            message="Args: " + ", ".join(event['args'])
        )

    def trigger(self, event):
        if len(event['args']) == 0:
            return False
        return event['args'][0] == 'use'
