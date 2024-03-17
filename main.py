from Unidad import *
from Soldado import * 
from Mago import *
from Arquero import *
import random


def turno_de_ataque(atacante, defensores):
    if atacante.esta_vivo() and defensores:  # Verificar si el atacante está vivo y hay defensores
        unidades_vivas = [unidad for unidad in defensores if unidad.esta_vivo()]
        if unidades_vivas:  # Verificar si hay unidades vivas en el equipo defensor
            objetivo = random.choice(unidades_vivas)
            atacante.atacar(objetivo)
            if not objetivo.esta_vivo():
                defensores.remove(objetivo)
        else:
            print("No hay unidades vivas en el equipo defensor.")
    else:
        print(f"{atacante.nombre} está muerto y no puede realizar acciones.")

def juego_de_estrategia():
    equipo_1 = [Soldado("Avendano", "Equipo 1"), Arquero("Meikell", "Equipo 1"), Mago("Josepo", "Equipo 1")]
    equipo_2 = [Soldado("Mateo", "Equipo 2"), Arquero("Arturo", "Equipo 2"), Mago("Andrés", "Equipo 2")]
    contador = 0

    for unidad in equipo_1:
        opcion = random.randint(1, 2)
        unidad.arma(opcion)
    
    for unidad in equipo_2:
        opcion = random.randint(1, 2)
        unidad.arma(opcion)

    while equipo_1 and equipo_2:
        contador += 1
        print("----------------------------------------------------------------")
        print(f"Turno #{contador}")
        print("\nTurno del equipo azul:")
        for unidad in equipo_1:
            turno_de_ataque(unidad, equipo_2)
        
        if equipo_2:
            print("\nTurno del equipo rojo:")
            for unidad in equipo_2:
                turno_de_ataque(unidad, equipo_1)
    
    print("----------------------------------------------------------------")
    if equipo_1:
        print("\n ¡Los azules han ganado!")
    else:
        print("\n ¡Los rojos han ganado!")
    print("\n----------------------------------------------------------------")

juego_de_estrategia()
