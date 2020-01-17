from .BaseEventHandler import BasicActionHandler


class CrusadeHandler(BasicActionHandler):
    ID = 'crusade'
    DEF_RIGTHS = True

    CMD = "крестовый"
    MSG = "[id{id}|{name}] совершил{sex} крестовый поход"

    SEX_M = ''
    SEX_F = 'a'
