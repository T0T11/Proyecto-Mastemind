from src.parametros import *
from src.reproducir_descendencia import *

def test_reproducir_descendencia_num_hijos():
    padres = [
        ["negro", "rojo", "azul", "amarillo"],
        ["blanco", "verde", "rojo", "azul"]
    ]
    hijos = reproducir_descendencia(padres, 2)
    assert len(hijos) == 2

def test_reproducir_descendencia_longitud_hijo():
    padres = [
        ["negro", "rojo", "azul", "amarillo"],
        ["blanco", "verde", "rojo", "azul"]
    ]
    hijos = reproducir_descendencia(padres, 2)
    for hijo in hijos:
        assert len(hijo) == NUMERO_GENES

def test_reproducir_descendencia_colores_validos():
    padres = [
        ["negro", "rojo", "azul", "amarillo"],
        ["blanco", "verde", "rojo", "azul"]
    ]
    hijos = reproducir_descendencia(padres, 2)
    for hijo in hijos:
        for color in hijo:
            assert color in ALELOS

def test_cruzar_a_mitad():

    padre1 = ["negro", "rojo", "azul", "amarillo"]
    padre2 = ["blanco", "verde", "rojo", "azul"]

    copia1 = padre1[:]
    copia2 = padre2[:]

    _ = cruzar(padre1, padre2)

    assert padre1 == copia1
    assert padre2 == copia2


def test_mutar():
    cromosoma = ["negro", "rojo", "azul", "amarillo"]
    
    mutado = mutar(cromosoma)

    assert isinstance(mutado, list)

    assert len(mutado) == NUMERO_GENES

    for color in mutado:
        assert color in ALELOS