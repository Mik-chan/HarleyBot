from .BaseEventHandler import BasicActionHandler


class RudeHitHandler(BasicActionHandler):
    ID = 'hit'
    DEF_RIGTHS = True

    CMD = ["ебнуть", "ёбнуть"]
    MSG = "[id{id}|{name}] ёбнул{sex} {str_args}"

    SEX_M = ''
    SEX_F = 'а'
