from .BaseEventHandler import BaseEventHandler


class HateHandler(BaseEventHandler):
    ID = 'hate'
    DEF_RIGTHS = True

    def handle(self, event):
        id = event['from_id']
        name = self.harley.user_info(id)['first_name']
        args = event['args'][1:]

        self.harley.send_msg(
            event['peer_id'],
            message="[id{}|{}] ненавидит {}".format(id, name, ' '.join(args))
        )

    def trigger(self, event):
        if len(event['args']) == 0:
            return False

        return event['args'][0].lower() == 'ненавидеть'
