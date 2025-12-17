from src.parametros import *
def calcular_fitness(cromosoma,solucion):
    fitness = 0
    for i in range(len(cromosoma)):
        if cromosoma[i] == solucion[i]:
            fitness += 2
        elif cromosoma[i] in solucion:
            fitness += 1
    return fitness