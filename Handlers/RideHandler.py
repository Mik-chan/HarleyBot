from .BaseEventHandler import BasicActionHandler


class RideHandler(BasicActionHandler):
    ID = 'ride'
    DEF_RIGTHS = True

    CMD = "кататься"
    MSG = "[id{id}|{name}] катается {str_args}"
