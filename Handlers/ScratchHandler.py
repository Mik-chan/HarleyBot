from .BaseEventHandler import BasicActionHandler


class ScratchHandler(BasicActionHandler):
    ID = 'scratch'
    DEF_RIGTHS = True

    CMD = "почесать"
    MSG = "[id{id}|{name}] почесал{sex} {str_args}"

    SEX_M = ''
    SEX_F = 'а'
