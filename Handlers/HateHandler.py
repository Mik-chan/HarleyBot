from .BaseEventHandler import BasicActionHandler


class HateHandler(BasicActionHandler):
    ID = 'hate'
    DEF_RIGTHS = True

    CMD = "ненавидеть"
    MSG = "[id{id}|{name}] ненавидит {args}"
