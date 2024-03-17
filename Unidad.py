

class Unidad:
    def __init__(self, nombre, equipo, hp, ataque, defensa):
        self.nombre = nombre
        self.equipo = equipo
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa

    def danio(self, objetivo):
        if self.equipo != objetivo.equipo:  # Verificar si los equipos son diferentes
            danio = max(0, self.ataque - objetivo.defensa)
            return danio

    def atacar(self, objetivo):
        if self.equipo != objetivo.equipo:  # Verificar si los equipos son diferentes
            danio = self.danio(objetivo)
            objetivo.hp -= danio
            print(f"{self.nombre} ataca a {objetivo.nombre} y le causa {danio} de daño.")
            if not objetivo.esta_vivo():
                print(f"{objetivo.nombre} ha sido derrotado.")  # Mensaje cuando una unidad muere
        else:
            print(f"{self.nombre} no puede atacar a una unidad de su mismo equipo.")

    def esta_vivo(self):
        return self.hp > 0