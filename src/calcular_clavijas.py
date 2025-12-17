from src.parametros import *
from collections import Counter

def calcular_clavijas(cromosoma, solucion):
    rojas = sum(1 for i in range(len(cromosoma)) if cromosoma[i] == solucion[i])
    colores_cromosoma = []
    colores_solucion =  []
    for i in range(len(cromosoma)):
        if cromosoma[i]  != solucion[i]:
            colores_solucion.append(solucion[i])
            colores_cromosoma.append(cromosoma[i])

    contar_cromosomas = Counter(colores_cromosoma)
    contar_solucion = Counter(colores_solucion)


    blancas = 0
    for alelo in contar_cromosomas:
        cantidad_cromosoma = contar_cromosomas[alelo]
        cantidad_solucion = contar_solucion[alelo]
        if cantidad_cromosoma < cantidad_solucion:
            blancas += cantidad_cromosoma
        else:
            blancas += cantidad_solucion
    return rojas, blancas



