class CantidadInvalidaError(Exception):
    def __init__(self, message="Cantidad no válida. Debes elegir entre 1 y 5 tarritos de sacol."):
        self.message = message
        super().__init__(self.message)