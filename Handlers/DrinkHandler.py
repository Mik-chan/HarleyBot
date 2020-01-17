from .BaseEventHandler import BasicActionHandler


class DrinkHandler(BasicActionHandler):
    ID = 'drink'
    DEF_RIGTHS = True

    CMD = "напиться до инфаркта"
    MSG = "[id{id}|{name}] напил{sex} до инфаркта"

    SEX_M = 'ся'
    SEX_F = 'ась'
