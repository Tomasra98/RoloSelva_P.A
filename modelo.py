import platform
from queue import Empty
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
        self.escudos_restantes = 3

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
            elif vida_provicional >= 500 and self.raza == "l":
                self.vida = 500  # Restablecer la vida al máximo para la raza Luchador
            else:
                self.vida = vida_provicional  # Actualizar la vida con el valor calculado
        else:
            print("No tienes pociones")
        
    """def __str__(self):
        cadena=(f" {self.nombre} tiene {self.vida} de vida, {self.monedas} monedas, {self.victorias} victorias, {self.xp} de experiencia, {self.escudos_restantes} escudos restantes, {len(self.mochila.pociones)} pociones, {self.multiplicador_basico} de multiplicador de ataque basico y {self.multiplicador_poder} de multiplicador de poder")
        return print(cadena)"""

    
class Enemigo:
    nombres = ["Drácula", "Bruja Malvada", "Gigante", "Fantasma", "Ogro"]

    def __init__(self, nivel):
        self.nombre = random.choice(Enemigo.nombres)
        self.vida = 75 + nivel * 3.0  # mas 3% de vida por nivel
        self.nivel = nivel

    def atacar(self):
        return random.randint(8, 25) * (1 + self.nivel * 0.5)  # mas % de daño por nivel
    
class Store:
    
    def comprar_objeto(self, cantidad: int, jugador: Player) -> None:
        if cantidad > 0 and cantidad <= 5:
            if len(jugador.mochila.pociones) == 5:
                print("Tu mochila ya contiene 5 pócimas. No puedes comprar más.")
            else:
                costo_total = cantidad * 70
                if jugador.monedas >= costo_total:
                    for _ in range(cantidad):
                        if len(jugador.mochila.pociones) < 5:
                            jugador.mochila.pociones.append(Pocion())
                            jugador.monedas -= 70
                    print(f"Has comprado {cantidad} pócimas. Ahora tienes {len(jugador.mochila.pociones)} pócimas y {jugador.monedas} monedas.")
                else:
                    print("No tienes suficientes monedas para comprar estas pócimas.")
        else:
            print("Cantidad no válida. Debes elegir entre 1 y 5 pócimas.")
                
class Combate:

    def __init__(self, jugador:Player, npc):
        self.jugador_pelea=jugador
        self.npc=npc
        self.eleccion=0

    def huir(self):
        return False
    
    def usar_escudo(self):
        if self.jugador_pelea.escudos_restantes > 0:
            self.jugador_pelea.escudos_restantes -= 1
            return random.uniform(0.6, 0.9)  # reducir un porcentaje aleatorio del daño
        else:
            print("No tienes escudos restantes. Recibes el daño completo.")
            return 1.0
        
    def atacar(self, eleccion):
        # dependiendo de la raza los ataques tienen multiplicadores diferentes
        
        self.eleccion = eleccion
        if eleccion == "1":
            return random.randint(5, 15) * self.jugador_pelea.multiplicador_basico
        elif eleccion == "2":
            return random.randint(5, 15) * self.jugador_pelea.multiplicador_poder
        else:
            print("Seleccion no válida. Se usara un ataque normal.")
            return random.randint(5, 15) * self.jugador_pelea.multiplicador_basico

class BackPack:
    def __init__(self):                     #acá se supone que se crea la lista donde van los objetos pocion
        self.pociones: list[Pocion] = []

    """def __str__(self) -> str:
        print(f'Tienes una cantidad de {len(self.pociones)}, ¿deseas usar una de ellas?')"""
      

class Pocion:

    def __init__(self):
        self.vidaCurar:int=25               #aca se supone que se crea el objeto pocion con su atributo vidaCurar
        self.nombre:str="Pocion de vida"    #aca se supone que se crea el objeto pocion con su atributo nombre


juego = True        #es el bucle de todo el juego
partida=True        #es el bucle donde se hace la partida de un jugador
combates=True       #es el bucle donde se hace el combate
elegir=True         #es el bucle menu de elegir raza solo para raza
eleccion=True       #es el bucle menu de ir a pelear o combatir
tienda:True         #es el bucle menu de la tienda

while juego:        #aqui comienza el juego de los varios personajes
    print("----------------------------------")
    print("Bienvenido a RoloSelva")
    print("----------------------------------")
    print("desea jugar?: ")
    print("----------------------------------")
    print("1. Si\n2. No\n ----------------------------------\n")        #se pregunta si quiere jugar o no para terminar el juego en general

    seleccion=int(input())
    if seleccion<=2 and seleccion>0:    #se comprueba que la seleccion sea valida
        if seleccion==1:
            partida=True        #si eligio jugar, comienza la partida de un personaje
            while partida:
                print("Para empezar, dime el nombre de tu personaje")
                print("----------------------------------")
                nombrepersonaje = input()
                jugador = Player(nombrepersonaje)       #crea el objeto con el nombre que el usuario brinda
                print("Bienvenido", jugador.nombre)
                print("----------------------------------")
                print("Selecciona tu raza: ")
                print("----------------------------------")
                elegir=True
                while elegir:           #empieza el bucle de elegir raza, básicamente para que se compruebe, que si o si elija raza
                    
                    seleccion=int(input("1. Mago\n2. Luchador\n ----------------------------------\n"))
                    print("----------------------------------")
                    if seleccion<=2 and seleccion>0:            #se comprueba que la seleccion sea valida
                        if seleccion == 1:
                            jugador.razaMago()
                            eleccion=True
                            elegir=False
                        elif seleccion == 2:
                            jugador.razaLuchador()
                            eleccion=True
                            elegir=False
                    else:
                        print("----------------------------------")
                        print("Seleccion no valida, ingresa una raza valida: ")
                        print("----------------------------------")
                while eleccion:             #comienza a desplegarse el menu siempre y cuando el jugador no muera o huya

                    print("----------------------------------")
                    print("¿Qué deseas hacer?: ")
                    print("----------------------------------")
                    print("1. Ir a la tienda")
                    print("----------------------------------")
                    print("2. Ir a pelear")
                    print("----------------------------------")
                    seleccion=int(input())
                    if seleccion<=2 and seleccion>0:        #se comprueba que la seleccion sea valida
                        if seleccion==1:
                            tienda = True
                            store = Store()  # Crea una instancia de la tienda
                            while tienda:
                                print("Bienvenido a la tienda")
                                print("----------------------------------")
                                print("Cuantas pócimas deseas comprar?: ")
                                print("----------------------------------")
                                seleccion = int(input("1. 1 Poción\n2. 2 Pociones\n3. 3 Pociones\n4. 4 Pociones\n5. 5 Pociones\n6. Salir\n ----------------------------------\n"))

                                if seleccion <= 6 and seleccion > 0:
                                    if seleccion == 6:
                                        tienda = False
                                    else:
                                        if seleccion + len(jugador.mochila.pociones) <= 5:
                                            costo_total = seleccion * 70
                                            if jugador.monedas >= costo_total:
                                                store.comprar_objeto(seleccion, jugador)  # Pasa el objeto jugador como parámetro
                                            else:
                                                print("No tienes suficientes monedas para comprar estas pócimas.")
                                        else:
                                            print("Tu mochila no puede contener más de 5 pócimas.")
                                else:
                                    print("----------------------------------")
                                    print("Selección no válida, ingresa una opción válida: ")
                                    print("----------------------------------")                                        # despues de cada solicitud de comprar pocion sale del ciclo tienda
                            else:
                                    print("----------------------------------")
                                    print("Seleccion no valida, ingresa una opcion valida: ")
                                    print("----------------------------------")   
                                    
                        elif seleccion==2:                      #entra a pelear porque eligio 2
                                print("----------------------------------")
                                print("Te has encontrado con un enemigo")
                                print("----------------------------------")
                                enemigo=Enemigo(jugador.victorias)          #crea un enemigo con el nivel del jugador
                                combate1=Combate(jugador,enemigo)           #crea un combate con el jugador y el enemigo como atributos
                                print("----------------------------------")
                                print("El enemigo tiene ", enemigo.vida, "de vida", "y es de nivel ", enemigo.nivel)    #provicional para mirar vida y nivel del enemigo
                                print("----------------------------------")
                                combates=True                        #comienza el bucle de combate
                                while combates:
                                    if jugador.vida <= 0:           #si la vida del jugador es menor o igual a 0, muere y se termina el juego
                                        print("Has muerto")
                                        enemigo = 0             #se reinician los valores de enemigo y combate1
                                        combate1 = 0            #para que no se quede con los valores de la partida anterior
                                        partida = False         #se termina la partida
                                        elegir = False          #se termina el bucle de elegir raza
                                        eleccion = False        #se termina el bucle de ir a pelear o a la tienda
                                        tienda = False          #se termina el bucle de la tienda
                                        combates = False        # Actualiza combates a False para salir del bucle
                                    elif enemigo.vida <= 0:
                                        enemigo = 0             #se reinician los valores de enemigo y combate1
                                        combate1 = 0            #para que no se quede con los valores de la partida anterior
                                        print("Has ganado")
                                        jugador.victorias += 1                              #se aumenta en 1 las victorias del jugador
                                        jugador.xp += random.randint(100, 161)             #se aumenta la experiencia del jugador
                                        jugador.monedas += random.randint(70, 131)          #se aumentan las monedas del jugador
                                        combates = False                                    # Actualiza combates a False para salir del bucle
                                        
                                    else:                                                    #si el jugador y el enemigo siguen vivos, se despliega el menu de combate
                                        print("----------------------------------")
                                        print("Que deseas hacer?: ")
                                        print("----------------------------------")
                                        print("1. Atacar")
                                        print("----------------------------------")
                                        print("2. Usar escudo")
                                        print("----------------------------------")
                                        print("3. Usar pocion")
                                        print("----------------------------------")
                                        print("4. Huir")
                                        print("----------------------------------")
                                        seleccion=int(input())                          #selecciona la accion que quiere hacer
                                        if seleccion<=4 and seleccion>0:                #se comprueba que la seleccion sea valida
                                            if seleccion==1:                                #si selecciona atacar, se despliega el menu de ataque
                                                print("----------------------------------")
                                                print("Que ataque deseas usar?: ")
                                                print("----------------------------------")
                                                print("1. Ataque basico")
                                                print("----------------------------------")
                                                print("2. Ataque poderoso")
                                                print("----------------------------------")
                                                combate_eleccion=int(input())                           #selecciona el ataque que quiere hacer
                                                if combate_eleccion<=2 and combate_eleccion>0:              #se comprueba que la seleccion sea valida
                                                    if combate_eleccion==1:                                 #si selecciona ataque basico, se hace el ataque basico
                                                        print("Atacas")
                                                        dañoJugador=combate1.atacar("1")                    #se hace el ataque basico
                                                        enemigo.vida-=dañoJugador                               #se le resta la vida al enemigo
                                                        print("----------------------------------")
                                                        print("El enemigo ha recibido", dañoJugador, "de daño")                 #se muestra el daño que hizo el jugador
                                                        print("----------------------------------")
                                                        print("El enemigo tiene", enemigo.vida, "de vida")                      #se muestra la vida del enemigo
                                                        print("----------------------------------")
                                                        print("El enemigo te ataca")
                                                        dañoEnemigo=enemigo.atacar()                                    #se hace el ataque del enemigo
                                                        jugador.vida-=dañoEnemigo                                   #se le resta la vida al jugador
                                                        print("----------------------------------") 
                                                        print("Has recibido", dañoEnemigo, "de daño")                   #se muestra el daño que hizo el enemigo
                                                        print("----------------------------------")
                                                        print("Tienes", jugador.vida, "de vida")                        #se muestra la vida del jugador
                                                        print("----------------------------------")
                                                    elif combate_eleccion==2:                               #si selecciona ataque poderoso, se hace el ataque poderoso
                                                        print("Atacas") 
                                                        dañoJugador=combate1.atacar("2")                                        #se hace el ataque poderoso
                                                        enemigo.vida-=dañoJugador                               #se le resta la vida al enemigo
                                                        print("----------------------------------") 
                                                        print("El enemigo ha recibido", dañoJugador, "de daño")                 #se muestra el daño que hizo el jugador
                                                        print("----------------------------------")     
                                                        print("El enemigo tiene", enemigo.vida, "de vida")                          #se muestra la vida del enemigo
                                                        print("----------------------------------")
                                                        print("El enemigo te ataca")
                                                        dañoEnemigo=enemigo.atacar()                                        #se hace el ataque del enemigo
                                                        jugador.vida-=dañoEnemigo                                           #se le resta la vida al jugador
                                                        print("----------------------------------")
                                                        print("Has recibido", dañoEnemigo, "de daño")                                   #se muestra el daño que hizo el enemigo
                                                        print("----------------------------------")
                                                        print("Tienes", jugador.vida, "de vida")                                        #se muestra la vida del jugador
                                                        print("----------------------------------")
                                                    
                                            elif seleccion==2:                                      #si selecciona usar escudo, se hace el uso de escudo
                                                print("Usas escudo")
                                                print("----------------------------------")
                                                print("El enemigo te ataca")
                                                dañoEnemigo=enemigo.atacar()*combate1.usar_escudo()                 #se hace el ataque del enemigo y se reduce el daño con el escudo
                                                jugador.vida-=dañoEnemigo                                           #se le resta la vida al jugador
                                                print("----------------------------------")
                                                print("Has recibido", dañoEnemigo, "de daño")                   #se muestra el daño que hizo el enemigo
                                                print("----------------------------------")
                                                print("Tienes", jugador.vida, "de vida")                    #se muestra la vida del jugador
                                                print("----------------------------------")
                                            elif seleccion==3:                                          #si selecciona usar pocion, se hace el uso de pocion
                                                print("Usas pocion")
                                                jugador.curarVida()                        #FALLO__CON LA MOCHILA___Se cura la vida del jugador
                                                print("----------------------------------")
                                                print("Tu vida ha aumentado a", jugador.vida)          #se muestra la vida del jugador
                                                print("----------------------------------")
                                            elif seleccion==4:                                          #si selecciona huir, se hace el uso de huir
                                                print("Has huido")
                                                print("----------------------------------")
                                                print("perdiste")
                                                combates=False                      #se termina el bucle de combate
                                                eleccion=False                #se termina el bucle de ir a pelear o a la tienda
                                                elegir=False          #se termina el bucle de elegir raza
                                                tienda=False        #se termina el bucle de la tienda
                                                partida=False           #se termina la partida
                                        else:
                                            print("----------------------------------")
                                            print("Seleccion no valida, ingresa una opcion valida: ")       #por si la seleccion del menu de ataque no es valida
                                            print("----------------------------------")
                                    
                                
                                    
                    else:
                        print("----------------------------------")
                        print("Seleccion no valida, ingresa una opcion valida: ")    #por si la seleccion del menu de ir a la tienda o a pelear no es valida
                        print("----------------------------------")

        elif seleccion==2:                  #si selecciona que no desea jugar(2), se termina el juego
            juego=False

        


