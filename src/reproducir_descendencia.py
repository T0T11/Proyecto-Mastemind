import random
from src.parametros import *

def cruzar(padre1, padre2):
    punto_cruce = len(padre1) // 2
    return padre1[:punto_cruce] + padre2[punto_cruce:]

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
        hijo = cruzar(padre1, padre2)
        hijo = mutar(hijo)
        descendencia.append(hijo)
    return descendencia
