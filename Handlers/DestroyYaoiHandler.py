from .BaseEventHandler import BaseEventHandler


class DestroyYaoiHandler(BaseEventHandler):
    ID = 'destroy_yaoi'
    DEF_RIGTHS = True

    def handle(self, event):
        id = event['from_id']
        name = self.harley.user_info(id)['first_name']
        sex = self.harley.user_info(id)['sex']
        sex_ending = 'a' if sex == 1 else ''

        msg = "[id{}|{}] уничтожил{} весь яой. Горите в аду, черти!"

        self.harley.send_msg(
            event['peer_id'],
            message=msg.format(id, name, sex_ending)
        )

    def trigger(self, event):
        return event['message'].lower().startswith('уничтожить яой')
