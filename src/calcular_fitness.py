from parametros import *
def calcular_fitness(individuo,solucion):
    for i in range(individuo):
        if individuo[i] == solucion[i]:
            return 2
        elif individuo[i] in solucion:
            return 1
        else:
            return 0