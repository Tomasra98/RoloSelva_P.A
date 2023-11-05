import sys
from modelo.jugador import Player
from modelo.enemigo import Enemigo
from modelo.tienda import Store
from modelo.combate import Combate
from modelo.entrenamiento import Entrenar
from modelo.tabla_de_posiciones import Tabla_de_posiciones
from modelo.no_calle_suficienteerror import NoCalleSuficienteError
from modelo.No_insultos_suficientes import InsultosInsuficientesError

class UIConsola:

    NAVAJAZO_VELOZ = "1"
    NAVAJAZO_ASPERO = "2"
    INSULTAR = "3"
    COSTAL = "4"
    HUIR = "5"


        
    def elegir_raza(self, jugador: Player):
        self.mostrar_menu_raza()
        eleccion = input("Ingrese su eleccion: ")
        while True:
            if eleccion == "1":
                jugador.razaMago()
                break

            elif eleccion == "2":
                jugador.razaLuchador()
                break
            else:
                print("Seleccion no válida. Se usara la raza por defecto.")

    def nombrar_personaje(self):
        nombre = input("Ingrese el nombre de su personaje: ")
        return Player(nombre)
    

    def ir_a_tienda(self, jugador: Player):
        self.mostrar_menu_tienda()
        Cuantas_pociones_desea_comprar = int(input("Ingrese su eleccion: "))
        if Cuantas_pociones_desea_comprar != 5 \
                and Cuantas_pociones_desea_comprar != 4 \
                and Cuantas_pociones_desea_comprar != 3 \
                and Cuantas_pociones_desea_comprar != 2 \
                and Cuantas_pociones_desea_comprar != 1:
            tienda1= Store(Cuantas_pociones_desea_comprar, jugador)
            tienda1.comprar_objeto()
        # manejar excepcion aca AAAAAAAAAAA

    def crear_combate(self, jugador: Player, tabla:Tabla_de_posiciones):
        print("Uy! ibas caminando por la oriental y te cuñó un ñero en la calle")
        enemigo = Enemigo(jugador.victorias)
        combate1 = Combate(jugador, enemigo)
        print(f"{enemigo.nombre} tiene {enemigo.vida} de vida y lleva {enemigo.nivel} años robando")
        return self.ir_a_pelear(combate1, tabla)

    def modificar_tabla_de_posiciones(self, tabla: Tabla_de_posiciones, jugador: Player):
        tabla.agregar_jugador(jugador)
        tabla.guardar_tabla()

    def ir_a_pelear(self, combate: Combate, tabla: Tabla_de_posiciones):
        Wcombate = True
        try:
            while Wcombate:
                self.mostrar_menu_combate()
                eleccion = input("Ingrese su eleccion: ")
                if eleccion == UIConsola.NAVAJAZO_VELOZ:
                    combate.atacar(eleccion)
                    if self.verificar_si_enemigo_gano(combate):
                        self.modificar_tabla_de_posiciones(tabla, combate.jugador_pelea)
                        self.perder()
                        return False
                    if self.verificar_si_jugador_gano(combate):
                        self.gano_combate(combate)
                        return True
                elif eleccion == UIConsola.NAVAJAZO_ASPERO:
                    combate.atacar(eleccion)
                    if self.verificar_si_enemigo_gano(combate):
                        self.modificar_tabla_de_posiciones(tabla, combate.jugador_pelea)
                        self.perder()
                        return False
                    if self.verificar_si_jugador_gano(combate):
                        self.gano_combate(combate)
                        return True
                elif eleccion == UIConsola.INSULTAR:
                    combate.insultar(combate)
                    if self.verificar_si_enemigo_gano(combate):
                        self.modificar_tabla_de_posiciones(tabla, combate.jugador_pelea)
                        self.perder()
                        return False
                    if self.verificar_si_jugador_gano(combate):
                        self.gano_combate(combate)
                        return True
                elif eleccion == UIConsola.COSTAL:
                    combate.jugador_pelea.curarVida()
                    if self.verificar_si_enemigo_gano(combate):
                        self.modificar_tabla_de_posiciones(tabla, combate.jugador_pelea)
                        self.perder()
                        return False
                    if self.verificar_si_jugador_gano(combate):
                        self.gano_combate(combate)
                        return True
                elif eleccion == UIConsola.HUIR:
                    self.modificar_tabla_de_posiciones(tabla, combate.jugador_pelea)
                    self.huir()  # aquí puedes agregar el código para volver al menú principal
                    return False
                else:
                    print("Seleccion no válida. Se usará ataque básico.")
                    combate.atacar(UIConsola.NAVAJAZO_VELOZ)
                    if self.verificar_si_enemigo_gano(combate):
                        self.modificar_tabla_de_posiciones(tabla, combate.jugador_pelea)
                        self.perder()
                        return True
        except InsultosInsuficientesError as e:
            print(e)

    def ir_a_entrenar(self, jugador: Player, eleccion: int):
        try:
            entrenamiento = Entrenar(jugador)
            if eleccion == 1:
                if jugador.xp < 100:
                    raise NoCalleSuficienteError()
                else:
                    entrenamiento.aumentar_multiplicador_basico()
            elif eleccion == 2:
                if jugador.xp < 100:
                    raise NoCalleSuficienteError()
                else:
                    entrenamiento.aumentar_multiplicador_poder()
            else:
                print("Selección no válida. No se entrenará.")
        except NoCalleSuficienteError as e:
            print(e)

    def ver_mochila(self, jugador: Player):
        print("Tienes", len(jugador.mochila.pociones), "tarritos de sacol")
        print("Tienes", jugador.insultos_restantes, "insultos restantes")
        print("Tienes", jugador.monedas, " pesos colombianos")
        print("Tienes", jugador.xp, "de experiencia")


    def verificar_si_enemigo_gano(self, combate: Combate):
        return not combate.jugador_pelea.estar_vivo()
    
    def verificar_si_jugador_gano(self, combate: Combate):
        return not combate.enemigo.estar_vivo()



       

    def perder(self):
        print("Perdiste la pelea con el ñerito")
        # guardar datos

    def huir(self):

        print("Reeee locaa, te fuiste corriendo... pero")
        print("No lograste huir, te hicieron un roto y no sabias cocer")
        print("Perdiste la pelea con el ñerito, moriste")

    def gano_combate(self, combate:Combate):
        print("Le ganaste al ñerito pa")
        combate.jugador_pelea.jugador_gano()
        print("Le has ganado a ", combate.jugador_pelea.victorias, " ñeritos")
        print("tienes", combate.jugador_pelea.xp, " de experiencia")
        print("tienes", combate.jugador_pelea.monedas, " pesos colombianos")
        
       

    def __init__(self):

        self.opciones_menu_principal = {
            "1": self.ir_a_tienda,
            "2": self.crear_combate,
            "3": self.ir_a_entrenar,
            "4": self.ver_mochila,
            #"5": tabla.ver_tabla_de_posiciones,
            "6": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR JUGAR A ''CAMINANDO POR LA ORIENTAL''")
        print("")
        sys.exit(0)
        

    @staticmethod
    def mostrar_menu_partidas():
        titulo = "¿Quieres caminar a las 9pm por la oriental?"
        print(f"\n{titulo:_^30}")
        print("1. Si")
        print("2. No")
        print("3. No, solo quiero ver la tabla de posiciones")
        print("")

    @staticmethod
    def mostrar_menu_entrenamiento():
        titulo = "¿Que habilidad deseas aumentar?"
        print(f"\n{titulo:_^30}")
        print("Cada aumento de habilidad cuesta 100 de experiencia")
        print("Puedes ganar experiencia bajandote a ñeritos")
        print("")
        print("1. Navajazo rapido pero suavezongo")
        print("2. Navajazo lento pero aspero")
        print("")

    @staticmethod
    def mostrar_menu():
        titulo = "¿Que deseas hacer?"
        print(f"\n{titulo:_^30}")
        print("1. Ir a la ferreteria")
        print("2. Arriesgarte a caminar y posiblemente pelear con un ñerito")
        print("3. Ir a entrenar con esa lata")
        print("4. Ver el costal")
        print("5. Ver la tabla de posiciones")
        print("6. Salir")
        print("")
        print(f"{'_':_^30}")

    @staticmethod
    def mostrar_menu_combate():
        titulo = "¿Que deseas hacer?"
        print(f"\n{titulo:_^30}")
        print("")
        print("1. Navajazo rapido")
        print("2. Navajazo aspero")
        print("3. Insultar al enemigo (bajara su multiplicador de daño en 0.9 [ acumulable con limite de 0 ])")
        print("4. Oler sacol (recuperaras 50 de vida)")
        print("5. Huir")
        print("")
        print(f"{'_':_^30}")

    @staticmethod
    def mostrar_menu_tienda():
        titulo = "¿cuantas pociones deseas comprar?"
        print(f"\n{titulo:_^30}")
        print("")
        print("Cada poción cuesta 70 monedas")
        print("")
        print("1. Un tarro de sacol")
        print("2. Dos tarros de sacol")
        print("3. Tres tarros de sacol")
        print("4. Cuatro tarros de sacol")
        print("5. Cinco tarros de sacol")
        print("6. No quiero sacol todavia pa")
        print("")
        print(f"{'_':_^30}")

    @staticmethod
    def mostrar_menu_raza():
        titulo = "¡Hola, que habilidad deseas elegir!"
        print(f"\n{titulo:_^30}")
        print("1. Navajear bien rapido pero mas suavezongo")
        print("recibiras los siguientes atributos, 250 de vida, 70 pesos colombianos, 1 de multiplicador de velocidad y 4 de multiplicador de asperosidad")
        print("")
        print("2. Navajear bien aspero pero mas lento")
        print("recibiras los siguientes atributos, 500 de vida, 210 pesos colombianos, 4 de multiplicador de velocidad y 1 de multiplicador de asperosidad")
        print("")
        print(f"{'_':_^30}")

    """def borrar_posicion_tabla(self, tabla: Tabla_de_posiciones):
        tabla.listado.pop(3)
        print("hecho")"""

    def ejecutar_app(self):
        juego = True
        while juego:

            partida = True
            eleccion = True
            self.mostrar_menu_partidas()
            eleccion_usuario =int(input("")) 
            tabla_de_posiciones1= Tabla_de_posiciones()
            tabla_de_posiciones1.cargar_tabla()
            if eleccion_usuario == 1:
                while partida:
                    Jugador1 = self.nombrar_personaje()
                    self.elegir_raza(Jugador1)
                    while eleccion:
                        self.mostrar_menu()
                        opcion = input("Seleccione una opción: ")
                        if opcion == "1":
                            self.ir_a_tienda(Jugador1)
                        elif opcion == "2":
                            jugador_jugo=self.crear_combate(Jugador1, tabla_de_posiciones1)
                            if not jugador_jugo:
                                partida=False
                                eleccion=False
                        elif opcion == "3":
                            self.mostrar_menu_entrenamiento()
                            self.ir_a_entrenar(Jugador1, int(input("Ingrese su eleccion: ")))
                        elif opcion == "4":
                            self.ver_mochila(Jugador1)
                        elif opcion == "5":
                            tabla_de_posiciones1.ver_tabla_de_posiciones()
                        elif opcion == "6":
                            self.modificar_tabla_de_posiciones(tabla_de_posiciones1, Jugador1)
                            partida = False
                            eleccion = False
                        else:
                            print(f"{opcion} no es una opción válida")

            elif eleccion_usuario == 2:
                tabla_de_posiciones1.guardar_tabla()
                self.salir()

            elif eleccion_usuario==3:
                tabla_de_posiciones1.ver_tabla_de_posiciones()
            
            
            else:
                print("Opcion no valida")

    