import random
from parametros import *
from calcular_fitness import calcular_fitness

def poblar_siguiente_generacion(poblacion_actual, descendencia, solucion):

    poblacion_total = poblacion_actual + descendencia

    fitnesses = [ 
        calcular_fitness(ind, solucion) 
        for ind in poblacion_total
    ]

    nueva_poblacion = random.choices(
        poblacion_total,
        fitnesses,
        k = TAMAÑO_POBLACION
    )

    return [individuo[:] for individuo in nueva_poblacion]
                                        
