from src.seleccionar_padres import seleccionar_padres
from src.generar_poblacion import generar_poblacion
from src.generar_solucion import generar_solucion
from src.parametros import *
def test_seleccionar_padres():
    poblacion = generar_poblacion()
    solucion = generar_solucion()
    padres = seleccionar_padres(poblacion, solucion)
    assert len(padres) == num_padres
