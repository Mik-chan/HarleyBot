class BaseEventHandler:
    ID = 'base_event'
    HELP_MSG = ''
    DEF_RIGTHS = False
    CMD = ''
    MIN_ARGS = 0

    def __init__(self, harley_bot):
        self.harley = harley_bot
        self.__data = None

    def handle(self, event):
        pass

    def trigger(self, event):
        if 'args' in event and len(event['args']) < 1 + self.MIN_ARGS:
            return False

        if isinstance(self.CMD, str):
            return self.__check_cmd(event, self.CMD)

        if isinstance(self.CMD, list):
            for cmd in self.CMD:
                if self.__check_cmd(event, cmd):
                    return True
        return False

    def _get_data(self, path=[]):
        return self.harley.get_data_table(['handlers', self.ID] + path)

    def __check_cmd(self, event, cmd):
        return (
            event['message'].lower() == cmd.lower() or
            event['message'].lower().startswith(cmd.lower() + ' ')
        )

    @property
    def _data(self):
        if self.__data is None:
            self.__data = self._get_data()
        return self.__data

    def __str__(self):
        return self.ID


class BasicActionHandler(BaseEventHandler):
    # Сообщение
    # Теги: id, name, sex_ending, args, str_args
    MSG = ''

    # Окончания
    SEX_M = ''
    SEX_F = ''

    # Добавлять ли изображение
    IMG = True

    def message(self, event, msg=None,
                id=None, name=None, sex_ending=None,
                sex=None, args=None):
        if msg is None:
            msg = self.MSG
        if id is None:
            id = event['from_id']
        if name is None:
            name = self.harley.user_info(id)['first_name']
        if sex is None:
            sex = self.harley.user_info(id)['sex']
        if sex_ending is None:
            sex_ending = self.SEX_F if sex == 1 else self.SEX_M
        if args is None:
            if isinstance(self.CMD, str):
                args = event['args'][len(self.CMD.split()):]
            else:
                args = event['args']

        message = msg.format(
            id=id, name=name,
            sex=sex_ending, str_args=' '.join(args),
            args=args
        )

        return message

    def handle(self, event):
        self.harley.send_msg(
            event['peer_id'],
            message=self.message(event),
            attachment=(
                None if self.IMG is False
                else self.harley.arts_pool.random(self.ID)
            )
        )
