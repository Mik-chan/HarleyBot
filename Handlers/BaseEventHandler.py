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
