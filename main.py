from src.parametros import *
from src.generar_poblacion import generar_poblacion
from src.generar_solucion import generar_solucion
from src.seleccionar_padres import seleccionar_padres
from src.reproducir_descendencia import reproducir_descendencia
from src.poblar_siguiente_generacion import poblar_siguiente_generacion
from src.calcular_fitness import calcular_fitness, calcular_fichas
from src.visual_mastermind import mostrar_feedback, cromosoma_emojis

def main():
    solucion = generar_solucion()
    print(f"\nSOLUCIÓN ----> {cromosoma_emojis(solucion)}\n")
    poblacion = generar_poblacion()
    for generacion in range(1, NUMERO_INTENTOS + 1):
        mejor_cromosoma = max(poblacion, key=lambda ind: calcular_fitness(ind, solucion))
        _, _, fichas = calcular_fichas(mejor_cromosoma, solucion)
        fitness = calcular_fitness(mejor_cromosoma, solucion)
        mostrar_feedback(mejor_cromosoma, fichas, generacion, fitness)
        if fitness == 8:
            print("¡Solución encontrada!")
            break
        padres = seleccionar_padres(poblacion, solucion)
        descendencia = reproducir_descendencia(padres, num_padres)
        poblacion = poblar_siguiente_generacion(poblacion, descendencia, solucion)

        
if __name__ == "__main__":
    main()
