import pygad
import matplotlib.pyplot as plt
from src.parametros import *
from src.calcular_fitness import *
from src.generar_solucion import generar_solucion

def graficos():
    def indices_a_colores(indices_solucion):
        return [ALELOS[i] for i in indices_solucion ]

    def colores_a_indices(colores):
        return [ALELOS.index(c) for c in colores]

    solucion_color = generar_solucion()
    solucion_indices = colores_a_indices(solucion_color)

    def fitness_func(ga_instance,solution, solution_idx): 
        cromosoma_colores = indices_a_colores(solution) 
        negras, blancas, _ = calcular_fichas(cromosoma_colores, solucion_color) 
        fitness = negras * 2 + blancas 
        return fitness

    ga_instance = pygad.GA(
        num_generations= NUMERO_INTENTOS,
        sol_per_pop= TAMAÑO_POBLACION ,
        num_parents_mating= TAMAÑO_POBLACION // 2,
        num_genes= NUMERO_GENES,
        fitness_func= fitness_func,
        gene_space= list(range(len(ALELOS))),
        gene_type=int,
        mutation_probability= TASA_MUTACION,
        mutation_type= "random",
        crossover_type= "single_point",

    )

    ga_instance.run()

    best_solution, best_fitness, best_idx = ga_instance.best_solution()
    best_solution_colores = indices_a_colores(best_solution)

    print("Solucion real:           ", solucion_color)
    print("Mejor solucion encontrada:", best_solution_colores)
    print("Fitness:", best_fitness)

    ga_instance.plot_fitness()
    plt.show()