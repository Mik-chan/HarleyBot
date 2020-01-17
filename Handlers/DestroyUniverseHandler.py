from .BaseEventHandler import BasicActionHandler


class DestroyUniverseHandler(BasicActionHandler):
    ID = 'destroy_universe'
    DEF_RIGTHS = True

    CMD = "взорвать вселенную"
    MSG = "[id{id}|{name}] взорвал{sex} вселенную"

    SEX_M = ''
    SEX_F = 'а'
