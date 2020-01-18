from .BaseEventHandler import BasicActionHandler


class PrintPeerIdHandler(BasicActionHandler):
    ID = 'print_peer_id'
    DEF_RIGTHS = False

    CMD = "peer_id"

    def message(self, event):
        return str(event['peer_id'])
