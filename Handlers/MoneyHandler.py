from .BaseEventHandler import BaseEventHandler


class MoneyHandler(BaseEventHandler):
    ID = 'money'
    DEF_RIGTHS = True

    CMD = ['тиньге', 'деньги']

    def handle(self, event):
        data = self._data
        args = event['args']

        from_id = str(event['from_id'])
        if from_id not in data:
            data[from_id] = 0

        if len(args) == 1:
            self.harley.send_msg(
                event['peer_id'],
                message="У вас {} тиньге".format(data[from_id])
            )

        if len(args) < 4:
            return

        cmd = args[1]
        ammo = int(event['args'][3])
        to_id = str(self.harley.user_id(args[2]))
        if to_id not in data:
            data[to_id] = 0

        if event['is_admin']:
            sent = False

            if cmd in ['добавить', '+']:
                data[to_id] += ammo
                sent = True
            elif cmd in ["удалить", "-"]:
                data[to_id] -= ammo
                sent = True

            if sent:
                self.harley.send_msg(
                        event['peer_id'],
                        message="Теперь у пользователя {} {} тиньге".format(
                            to_id,
                            data[to_id]
                        )
                    )
                return

        if cmd in ["перевести", "передать", "перевод"]:
            if ammo < 0:
                msg = 'Пожалуйста, введите положительное количество тиньге!'
            elif data[from_id] < ammo:
                msg = 'Вам не хватает Тиньге для перевода!'
            else:
                data[from_id] -= ammo
                data[to_id] += ammo

                msg = "Теперь у пользователя [id{}|{}] {} тиньге!".format(
                    to_id, self.harley.user_info(to_id)['first_name'], data[to_id]
                )

            self.harley.send_msg(
                event['peer_id'], message=msg
            )

    def trigger(self, event):
        if event['from_id'] == event['peer_id']:
            return False
        return super().trigger(event)
