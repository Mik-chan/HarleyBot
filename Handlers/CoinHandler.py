from .BaseEventHandler import BasicActionHandler
import random


class CoinHandler(BasicActionHandler):
    ID = 'coin_toss'
    DEF_RIGTHS = True

    CMD = "монетка"

    def message(self, event):
        return random.choice([
            "Выпал орел", "Выпала решка"
        ])
