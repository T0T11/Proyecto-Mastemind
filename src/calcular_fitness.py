from parametros import *
def calcular_fitness(individuo,solucion):
    for i in range(len(individuo)):
        if individuo[i] == solucion[i]:
            fitness += 2
        elif individuo[i] in solucion:
            fitness += 1
    return fitness