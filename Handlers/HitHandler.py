from .BaseEventHandler import BaseEventHandler


class HitHandler(BaseEventHandler):
    ID = 'hit'
    DEF_RIGTHS = True

    def handle(self, event):
        id = event['from_id']
        name = self.harley.user_info(id)['first_name']
        sex = self.harley.user_info(id)['sex']
        sex_ending = 'a' if sex == 1 else ''
        obj = ' '.join(event['args'][1:])

        if event['args'][0] == 'ударить':
            action = 'ударил'
        else:
            action = 'ёбнул'

        msg = '[id{}|{}] {}{} {}'
        self.harley.send_msg(
            event['peer_id'],
            message=msg.format(id, name, action, sex_ending, obj)
        )

    def trigger(self, event):
        if len(event['args']) == 0:
            return False

        return event['args'][0].lower() in ['ударить', 'ёбнуть', 'ебнуть']
