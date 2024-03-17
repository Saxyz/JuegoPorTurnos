from Unidad import *

class Arquero(Unidad):
    def __init__(self, nombre, equipo):
        super().__init__(nombre, equipo, hp=80, ataque=25, defensa=5)

    def arma(self, opcion):
        while True:
            if opcion == 1:
                print(f"{self.nombre} a seleccionado el 'Arco de la muerte'")
                self.hp = 50 
                self.ataque += 15
                break
            elif opcion == 2:
                print(f"{self.nombre} a seleccionado el 'Arco de la vida'")
                self.hp = 75
                self.ataque += 5
                break
            else:
                print("Error: numero incorrecto")