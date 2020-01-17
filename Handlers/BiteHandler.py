from .BaseEventHandler import BasicActionHandler


class BiteHandler(BasicActionHandler):
    ID = 'bite'
    DEF_RIGTHS = True

    CMD = "кусь"
    MSG = "[id{id}|{name}] укусил{sex} {str_args}"

    SEX_M = ''
    SEX_F = 'а'
