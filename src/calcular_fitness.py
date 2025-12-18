from src.parametros import *

def calcular_fichas(cromosoma,solucion):
    sol = solucion.copy()
    fichas = ["  "] * NUMERO_GENES
    for i in range(len(cromosoma)):
        if cromosoma[i] == solucion[i]:
            fichas[i] = "⚫"
            sol[i] = "  "
    for i in range(len(cromosoma)):
        if fichas[i] == "⚫":
            continue
        if cromosoma[i] in sol:
            fichas[i] = "⚪"
            sol[sol.index(cromosoma[i])] = "  "
    negras = fichas.count("⚫")
    blancas = fichas.count("⚪")
    return negras, blancas, fichas

def calcular_fitness(cromosoma, solucion):
    negras, blancas, _ = calcular_fichas(cromosoma, solucion)
    return negras * 2 + blancas
