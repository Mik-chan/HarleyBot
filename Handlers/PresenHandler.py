from .BaseEventHandler import BasicActionHandler


class PresentHandler(BasicActionHandler):
    ID = 'present'
    DEF_RIGTHS = True

    CMD = "подарить"
    MSG = "[id{id}|{name}] подарил{sex} {str_args}"

    SEX_M = ''
    SEX_F = 'а'
