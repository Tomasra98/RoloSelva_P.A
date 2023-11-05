class InsultosInsuficientesError(Exception):
    def __init__(self):
        super().__init__("No tienes insultos restantes. El combate continúa.")