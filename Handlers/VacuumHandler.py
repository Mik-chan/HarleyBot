from .BaseEventHandler import BasicActionHandler


class VacuumHandler(BasicActionHandler):
    ID = 'vacuum'
    DEF_RIGTHS = True

    CMD = "пропылесосить"
    MSG = "[id{id}|{name}] пропылесосил{sex} {args}"

    SEX_M = ''
    SEX_F = 'а'
