import pytest
from src.parametros import *
from src.generar_poblacion import generar_poblacion

poblacion = generar_poblacion()

def test_generar_poblacion():
    assert len(poblacion) == TAMAÑO_POBLACION