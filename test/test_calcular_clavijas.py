from src.calcular_clavijas import calcular_clavijas

def test_correcto():
    solucion = [1,2,2,4]
    intento = [1,2,2,4]
    assert calcular_clavijas(intento, solucion) == (4,0)