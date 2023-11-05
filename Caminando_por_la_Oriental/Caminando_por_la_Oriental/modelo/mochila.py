from modelo.pocion import Pocion


class BackPack:
    def __init__(self):  # acá se supone que se crea la lista donde van los objetos pocion
        self.pociones: list[Pocion] = []
