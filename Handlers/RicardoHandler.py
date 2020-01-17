from .BaseEventHandler import BasicActionHandler


class RicardoHandler(BasicActionHandler):
    ID = 'ricardo'
    DEF_RIGTHS = True

    CMD = "рикардо"
    MSG = "[id{id}|{name}], держи Рикардо!"
