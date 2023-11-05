from modelo.jugador import Player
import pickle

class Tabla_de_posiciones:

    def __init__(self):
        self.listado: list[Player] = []

    def agregar_jugador(self, jugador: Player):
        self.listado.append(jugador)
        self.listado.sort(key=Player.comparar_victorias, reverse=True)

    def cargar_tabla(self):
        with open("tablaposiciones.txt", "rb") as archivo:
            self.listado = pickle.load(archivo)
            #print("Tab cargado con exito!")

    def guardar_tabla(self):
        with open("tablaposiciones.txt", "wb") as archivo:
            pickle.dump(self.listado, archivo)


    def ver_tabla_de_posiciones(self):
        print("Tabla de posiciones")
        print("__________________________")
        for i in (self.listado):
            print(i.nombre, " se ha bajado a ", i.victorias, " ñeritos en la oriental")
            print("-")

    