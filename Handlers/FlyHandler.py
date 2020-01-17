from .BaseEventHandler import BasicActionHandler


class FlyHandler(BasicActionHandler):
    ID = 'fly'
    DEF_RIGTHS = True

    CMD = "полетать"
    MSG = "[id{id}|{name}] летает"
