from .BaseEventHandler import BasicActionHandler


class FaggotHandler(BasicActionHandler):
    ID = 'faggot'
    DEF_RIGTHS = True

    CMD = "опидорасить"
    MSG = "[id{id}|{name}] опидорасил{sex} {str_args}"

    SEX_M = ''
    SEX_F = 'а'
