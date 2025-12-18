from src.parametros import *
from src.generar_solucion import *

 
def test_generar_solucion():
    solucion = generar_solucion()
    assert len(solucion)== 4