from .BaseEventHandler import BaseEventHandler


class CryHandler(BaseEventHandler):
    ID = 'cry'
    DEF_RIGTHS = True

    def handle(self, event):
        id = event['from_id']
        name = self.harley.user_info(id)['first_name']
        sex = self.harley.user_info(id)['sex']

        sex_ending = "ась" if sex == 1 else "ся"

        self.harley.send_msg(
            event['peer_id'],
            message="[id{}|{}] расплакал{}".format(id, name, sex_ending)
        )

    def trigger(self, event):
        if len(event['args']) == 0:
            return False

        return event['args'][0].lower() == 'расплакаться'
