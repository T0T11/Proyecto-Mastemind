from src.parametros import *
from src.generar_poblacion import generar_poblacion
from src.generar_solucion import generar_solucion
from src.seleccionar_padres import seleccionar_padres
from src.reproducir_descendencia import reproducir_descendencia, cruzar, mutar
from src.poblar_siguiente_generacion import poblar_siguiente_generacion
from src.calcular_fitness import calcular_fitness
from src.visual_mastermind import mostrar_feedback
from src.calcular_clavijas import calcular_clavijas

def main():
    solucion = generar_solucion()
    print(f"Solución: {solucion}")
    poblacion = generar_poblacion()

    for gen in range(1, NUMERO_INTENTOS + 1):
        mejor_cromosoma = max(poblacion, key=lambda ind: calcular_fitness(ind, solucion))
        mejor_fitness = calcular_fitness(mejor_cromosoma, solucion)
        rojas, blancas = calcular_clavijas(mejor_cromosoma, solucion)

        mostrar_feedback(mejor_cromosoma, rojas, blancas, gen, mejor_fitness)
        if mejor_fitness == 8:
            print("¡Solución encontrada!")
            break

        padres = seleccionar_padres(poblacion, solucion)
        descendencia = reproducir_descendencia(padres, num_padres)
        poblacion = poblar_siguiente_generacion(poblacion, descendencia, solucion)

        
if __name__ == "__main__":
    main()