import random


class Enemigo:
    nombres = ["Brayan", "Stiwar", "Sneyder", "Jefferson", "Anderson", "Mayerli", "Britani", "Jeison", "Yuremy", "Maicol", "Stiven", "Leidi", "Kevin", "Yurleidi", "Yulitza", "Briyid", "Brandon", "Yamile", "Yasbleidy"]

    def __init__(self, nivel):
        self.nombre = random.choice(Enemigo.nombres)
        self.vida = 75 + nivel * 3.0  # mas 3% de vida por nivel
        self.nivel = nivel

    def estar_vivo(self)->bool:
        return self.vida>0
    
    def atacar(self):
        # mas % de daño por nivel
        return random.randint(8, 25) * (1 + self.nivel * 0.5)
