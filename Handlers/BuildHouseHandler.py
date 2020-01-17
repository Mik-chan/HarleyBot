from .BaseEventHandler import BasicActionHandler


class BuildHouseHandler(BasicActionHandler):
    ID = 'house'
    DEF_RIGTHS = True

    CMD = "построить дом"
    MSG = "[id{id}|{name}] построил{sex} дом"

    SEX_M = ''
    SEX_F = 'а'
