


class NoSuficientesPesosError(Exception):
    def __init__(self, message="No tienes suficientes pesos colombianos para comprar estas tarritos de sacol."):
        self.message = message
        super().__init__(self.message)