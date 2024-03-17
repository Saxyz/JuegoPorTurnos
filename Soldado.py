from Unidad import *

class Soldado(Unidad):
    def __init__(self, nombre, equipo,):
        super().__init__(nombre, equipo, hp=100, ataque=20, defensa=10)

    def arma(self, opcion):
        while True:
            if opcion == 1:
                print(f"{self.nombre} a seleccionado la 'Scalibur'")
                self.defensa = 5
                self.ataque += 15
                break
            elif opcion == 2:
                print(f"{self.nombre} a seleccionado la 'Matademonios'")
                self.ataque += 7
                break
            else:
                print("Error: numero incorrecto")
        

   