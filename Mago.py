from Unidad import *

class Mago(Unidad):
    def __init__(self, nombre, equipo):
        super().__init__(nombre, equipo, hp=60, ataque=35, defensa=2)

    def arma(self, opcion):
        while True:
            if opcion == 1:
                print(f"{self.nombre} a seleccionado el 'Grimorio del trébol de 5 hojas'")
                self.hp = 40
                self.ataque += 25
                break
            elif opcion == 2:
                print(f"{self.nombre} a seleccionado el 'Libro de Favonius'")
                self.defensa = 20
                self.ataque += 10
                break
            else:
                print("Error: numero incorrecto")