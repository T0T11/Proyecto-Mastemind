from src.calcular_fitness import calcular_fitness

def test_fitness_exactos():
    solucion = ['rojo', 'azul', 'verde', 'amarillo']
    individuo = ['rojo', 'azul', 'verde', 'amarillo']
    
    fitness = calcular_fitness(individuo, solucion)
    
    assert fitness == 8