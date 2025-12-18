from src.calcular_fitness import calcular_fitness


def test_fitness_exactos():

    solucion = ["rojo", "azul", "verde", "amarillo"]
    cromosoma = ["rojo", "azul", "verde", "amarillo"]

    fitness = calcular_fitness(cromosoma, solucion)

    assert fitness == 8


def test_fitness_color_en_otro_sitio():

    solucion = ["rojo", "azul", "verde", "amarillo"]
    cromosoma = ["azul", "verde", "amarillo", "rojo"]

    fitness = calcular_fitness(cromosoma, solucion)

    assert fitness == 4


def test_fitness_color_incorrecto():

    solucion = ["rojo", "azul", "verde", "amarillo"]
    cromosoma = ["negro", "negro", "negro", "negro"]

    fitness = calcular_fitness(cromosoma, solucion)

    assert fitness == 0


def test_fitness_combinado():

    solucion = ["rojo", "azul", "verde", "amarillo"]
    individuo = ["rojo", "verde", "negro", "amarillo"]

    fitness = calcular_fitness(individuo, solucion)

    assert fitness == 5


def test_fitness_solucion_individuo_identicos():

    solucion = ["rojo", "azul", "verde", "amarillo"]
    individuo = ["rojo", "azul", "verde", "amarillo"]

    fitness = calcular_fitness(individuo, solucion)

    assert fitness == 8


def test_fitness_colores_repetidos():

    solucion = ["rojo", "azul", "verde", "amarillo"]
    individuo = ["rojo", "rojo", "rojo", "rojo"]

    fitness = calcular_fitness(individuo, solucion)

    assert fitness == 2


def test_fitness_listas_vacias():

    solucion = []
    individuo = []

    fitness = calcular_fitness(individuo, solucion)

    assert fitness == 0
