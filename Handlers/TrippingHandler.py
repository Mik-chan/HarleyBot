from .BaseEventHandler import BasicActionHandler


class TrippingHandler(BasicActionHandler):
    ID = 'tripping'
    DEF_RIGTHS = True

    CMD = "подножка"
    MSG = "[id{id}|{name}] поставил{sex} подножку {str_args}"

    SEX_M = ''
    SEX_F = 'а'
