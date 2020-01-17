from .BaseEventHandler import BaseEventHandler


class GreetingHandler(BaseEventHandler):
    ID = 'greeting'
    DEF_RIGTHS = True

    def handle(self, event):
        id = event['from_id']
        name = self.harley.user_info(id)['first_name']
        msg = (
            "Приветствую тебя впервые в нашей беседе! "
            "Твой аккаунт зарегестрирован, [id{}|{}]!"
        )

        self.harley.send_msg(
            event['peer_id'],
            message=msg.format(id, name)
        )

    def trigger(self, event):
        if event['action'] is not None:
            if event['action']['type'] in ['chat_invite_user', 'chat_invite_user_by_link']:
                return True

        return False
