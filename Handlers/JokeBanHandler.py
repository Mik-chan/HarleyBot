from .BaseEventHandler import BasicActionHandler


class JokeBanHandler(BasicActionHandler):
    ID = 'joke_ban'
    DEF_RIGTHS = True

    CMD = "забанить"
    MSG = "[id{id}|{name}] забанил{sex} {str_args}"

    SEX_M = ''
    SEX_F = 'а'
