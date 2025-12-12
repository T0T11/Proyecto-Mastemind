from calcular_fitness import calcular_fitness
from parametros import num_padres
import random

def seleccionar_padres(poblacion, solucion):
    fitnesses = [ 
        calcular_fitness(ind,solucion) for ind in poblacion
    ]

    padres = random.choices(
        population = poblacion,
        weights = fitnesses,
        k = num_padres
    )
    return padres
