from .Pool import Pool
import random


class ArtsPool(Pool):
    ID = 'arts'

    def add_art(self, topic, url):
        data = self._data
        if not (topic in data):
            data[topic] = []

        data[topic].append(url)

    def random(self, topic):
        data = self._data
        if not (topic in data):
            return None

        if len(data[topic]) == 0:
            return None

        return random.choice(data[topic])
