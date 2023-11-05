from queue import Empty
import random
from modelo.jugador import Player
from modelo.enemigo import Enemigo
from modelo.No_insultos_suficientes import InsultosInsuficientesError


class Combate:

    def __init__(self, jugador: Player, enemigo: Enemigo):
        self.jugador_pelea = jugador
        self.enemigo = enemigo
        self.eleccion = 0

    def comparar_si_jugador_esta_vivo(self)->bool:
        return self.jugador_pelea.estar_vivo()      
        

    def comparar_si_enemigo_esta_vivo(self):
        return self.enemigo.estar_vivo()     
    """
    class InsultoInsuficienteError(Exception):
        def __str__(self):
            return "No tienes insultos restantes. El combate continua."




    try:
        combate.insultar()
        print("Insulto exitoso")
        print("ROLO Hp")  
    except InsultosInsuficientesError as err:
        print(err)


    """
    def insultar(self, combate: 'Combate'):
        if self.jugador_pelea.insultos_restantes > 0:
            self.jugador_pelea.insultos_restantes -= 1
            print("Insulto exitoso")
            print("ÑERO CATR*********A")
            self.enemigo.nivel -= (0.9 * combate.jugador_pelea.victorias)
            if self.enemigo.nivel < 0:
                self.enemigo.nivel = 0
        else:
            raise InsultosInsuficientesError()

    

    def atacar(self, eleccion):
        # dependiendo de la raza los ataques tienen multiplicadores diferentes

        self.eleccion = eleccion
        if eleccion == "1":
            print("Se navajeara rapidamente")
            daño = random.randint(5, 15) * self.jugador_pelea.multiplicador_basico
            self.enemigo.vida -= daño


            if self.enemigo.vida < 0:
                self.enemigo.vida = 0


            print("El ñerito ha recibido", daño, "de daño")
            print("El ñerito tiene", self.enemigo.vida, "de vida")
            daño_enemigo = self.enemigo.atacar()
            self.jugador_pelea.vida -= daño_enemigo

            if self.jugador_pelea.vida < 0:
                self.jugador_pelea.vida = 0

            print("El ñerito te ha hecho", daño_enemigo, "de daño")
            print("Tu tienes", self.jugador_pelea.vida, "de vida")
        elif eleccion == "2":
            print("Se navajeara bien aspero")
            daño = random.randint(5, 15) * self.jugador_pelea.multiplicador_poder
            self.enemigo.vida -= daño

            if  self.enemigo.vida < 0:
                self.enemigo.vida = 0

            print("El ñerito ha recibido", daño, "de daño")
            print("El ñerito tiene", self.enemigo.vida, "de vida")
            daño_enemigo = self.enemigo.atacar()
            self.jugador_pelea.vida -= daño_enemigo

            if self.jugador_pelea.vida < 0:
                self.jugador_pelea.vida = 0

            print("El ñerito te ha hecho", daño_enemigo, "de daño")
            print("Tu tienes", self.jugador_pelea.vida, "de vida")
        else:
            print("Eleccion no valida, se atacara con el ataque basico")
            daño = random.randint(5, 15) * self.jugador_pelea.multiplicador_basico
            self.enemigo.vida -= daño

            if self.enemigo.vida < 0:    
                self.enemigo.vida = 0
            
            print("El ñerito ha recibido", daño, "de daño")
            print("El ñerito tiene", self.enemigo.vida, "de vida")
            daño_enemigo = self.enemigo.atacar()
            self.jugador_pelea.vida -= daño_enemigo

            if self.jugador_pelea.vida < 0:
                self.jugador_pelea.vida = 0

            print("El ñerito te ha hecho", daño_enemigo, "de daño")
            print("Tu tienes", self.jugador_pelea.vida, "de vida")