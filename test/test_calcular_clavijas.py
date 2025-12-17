from src.calcular_clavijas import calcular_clavijas

def test_todo_correcto():
    solucion = [1,2,2,4]
    intento = [1,2,2,4]
    assert calcular_clavijas(intento, solucion) == (4,0)
def test_repetidos_blancas():
    solucion = [1,2,2,3]
    intento = [2,2,1,4]
    assert calcular_clavijas(intento, solucion) == (0,3)
def test_blancas_rojas():
    solucion = [3,1,2,5]
    intento = [3,2,5,4]
    assert calcular_clavijas(intento, solucion) == (1,2)
    