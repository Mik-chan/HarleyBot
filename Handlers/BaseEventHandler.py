class BaseEventHandler:
    ID = 'base_event'
    HELP_MSG = ''
    DEF_RIGTHS = False

    def __init__(self, harley_bot):
        self.harley = harley_bot
        self.__data = None

    def handle(self, event):
        pass

    def trigger(self, event):
        return False

    def _get_data(self, path=[]):
        return self.harley.get_data_table(['handlers', self.ID] + path)

    @property
    def _data(self):
        if self.__data is None:
            self.__data = self._get_data()
        return self.__data

    def __str__(self):
        return self.ID


class BasicActionHandler(BaseEventHandler):
    # Сообщение
    # Теги: id, name, sex_ending, args
    MSG = ''

    # Команда
    CMD = ''

    # Окончания
    SEX_M = ''
    SEX_F = ''

    # Добавлять ли изображение
    IMG = True

    def message(self, event):
        id = event['from_id']
        name = self.harley.user_info(id)['first_name']
        sex = self.harley.user_info(id)['sex']
        sex_ending = self.SEX_F if sex == 1 else self.SEX_M
        args = event['args'][len(self.CMD.split()):]

        message = self.MSG.format(
            id=id, name=name,
            sex=sex_ending, args=' '.join(args)
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

    def trigger(self, event):
        return (
            event['message'].lower() == self.CMD.lower() or
            event['message'].lower().startswith(self.CMD.lower() + ' ')
        )
