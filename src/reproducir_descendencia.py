import random
from src.parametros import *

def cruzar(padre1, padre2):
    punto_cruce = len(padre1) // 2
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre1[punto_cruce:] + padre2[:punto_cruce]
    return hijo1, hijo2

def mutar(cromosoma):
    mutado = cromosoma[:]
    for i in range(len(mutado)):
        if random.random() < TASA_MUTACION:
            opciones = [c for c in ALELOS if c != mutado[i]]
            mutado[i] = random.choice(opciones)
    return mutado

def reproducir_descendencia(padres, num_hijos):
    descendencia = []
    for _ in range(num_hijos):
        padre1, padre2 = random.sample(padres, 2)

        hijo1 , hijo2 = cruzar(padre1, padre2)

        hijo1 = mutar(hijo1)
        hijo2 = mutar(hijo2)

        descendencia.append(hijo1)
        descendencia.append(hijo2)
    return descendencia
