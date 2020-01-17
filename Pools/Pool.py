class Pool:
    ID = ''

    def __init__(self, harley_bot):
        self.harley = harley_bot
        self.__data = None

    def _get_data(self):
        return self.harley.get_data_table(['pools', self.ID])

    @property
    def _data(self):
        if self.__data is None:
            self.__data = self._get_data()
        return self.__data
