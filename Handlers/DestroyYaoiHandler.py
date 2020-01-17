from .BaseEventHandler import BasicActionHandler


class DestroyYaoiHandler(BasicActionHandler):
    ID = 'destroy_yaoi'
    DEF_RIGTHS = True

    CMD = "уничтожить яой"
    MSG = "[id{id}|{name}] уничтожил{sex} весь яой. Горите в аду, черти!"

    SEX_M = ''
    SEX_F = 'а'
