from modelo.mochila import BackPack
from modelo.no_pociones_suficiente_error import NoSacolError
import random


class Player:

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.vida = 1
        self.monedas = 0
        self.multiplicador_basico = 1
        self.multiplicador_poder = 1
        self.victorias = 0
        self.xp = 0
        self.raza = "x"
        self.mochila = BackPack()
        self.insultos_restantes = 3
    def estar_vivo(self)->bool:
        return self.vida > 0

    def razaMago(self):
        self.vida = 250
        self.monedas = 70
        self.multiplicador_basico = 1
        self.multiplicador_poder = 4
        self.raza = "m"

    def razaLuchador(self):
        self.vida = 500
        self.monedas = 210
        self.multiplicador_basico = 4
        self.multiplicador_poder = 1
        self.raza = "l"

    def curarVida(self) -> None:
        if len(self.mochila.pociones) > 0:
            # Usa una poción de la mochila y retírala.
            potion = self.mochila.pociones.pop()
            vida_provicional = self.vida + potion.vidaCurar
            if vida_provicional >= 250 and self.raza == "m":
                self.vida = 250  # Restablecer la vida al máximo para la raza Mago
                print("Tu vida ha sido restablecida al máximo.")
            elif vida_provicional >= 500 and self.raza == "l":
                self.vida = 500  # Restablecer la vida al máximo para la raza Luchador
                print("Tu vida ha sido restablecida al máximo.")
            else:
                self.vida = vida_provicional  # Actualizar la vida con el valor calculado
                print("Tu vida ha sido restablecida a ", self.vida, ".")
        else:
            raise NoSacolError()

    def jugador_gano(self):
        self.victorias += 1
        self.xp += random.randint(100, 161)
        self.monedas += random.randint(70, 131)
     
    def comparar_victorias(self):
        return self.victorias