from .BaseEventHandler import BasicActionHandler


class HitHandler(BasicActionHandler):
    ID = 'hit'
    DEF_RIGTHS = True

    CMD = "ударить"
    MSG = "[id{id}|{name}] ударил{sex} {str_args}"

    SEX_M = ''
    SEX_F = 'а'
