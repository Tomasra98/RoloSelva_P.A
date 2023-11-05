class NoCalleSuficienteError(Exception):
    def __init__(self, message="Te falta calle pa"):
        self.message = message
        super().__init__(self.message)