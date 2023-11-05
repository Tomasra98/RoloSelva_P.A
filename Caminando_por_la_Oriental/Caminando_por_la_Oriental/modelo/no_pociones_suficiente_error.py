class NoSacolError(Exception):
    def __init__(self):
        super().__init__("No tienes tarritos de sacol")
