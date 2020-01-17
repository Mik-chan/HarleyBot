from .BaseEventHandler import BasicActionHandler


class CryHandler(BasicActionHandler):
    ID = 'cry'
    DEF_RIGTHS = True

    CMD = "расплакаться"
    MSG = "[id{id}|{name}] расплакал{sex}"

    SEX_M = 'ся'
    SEX_F = 'ась'
