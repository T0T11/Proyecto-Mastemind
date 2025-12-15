from src.poblar_siguiente_generacion import poblar_siguiente_generacion
from src.parametros import TAMAÑO_POBLACION, COLORES, TAMAÑO_CODIGO

def test_poblar_siguiente_generacion_tamano_y_dominio():
    poblacion_actual = [
    ["negro", "rojo", "azul", "amarillo"],
    ["blanco", "verde", "rojo", "azul"],
    ]

    descendencia = [
    ["verde", "verde", "azul", "rojo"],
    ["amarillo", "rojo", "blanco", "negro"],
    ]

    solucion = ["negro", "rojo", "azul", "amarillo"]

    nueva = poblar_siguiente_generacion(poblacion_actual, descendencia, solucion)

    # 1) Tamaño fijo
    assert len(nueva) == TAMAÑO_POBLACION

    # 2) Cada individuo tiene el tamaño correcto y genes válidos
    for ind in nueva:
        assert len(ind) == TAMAÑO_CODIGO
    for gen in ind:
        assert gen in COLORES

    # 3) Los individuos seleccionados provienen de la población total (por igualdad de contenido)
    poblacion_total = poblacion_actual + descendencia
    assert all(ind in poblacion_total for ind in nueva)


def test_poblar_siguiente_generacion_no_comparte_referencias():
    poblacion_actual = [["negro", "rojo", "azul", "amarillo"]]
    descendencia = [["blanco", "verde", "rojo", "azul"]]
    solucion = ["negro", "rojo", "azul", "amarillo"]

    nueva = poblar_siguiente_generacion(poblacion_actual, descendencia, solucion)

    # Si modifico un individuo de la nueva población, NO debe modificar los originales
    original_total = poblacion_actual + descendencia
    copia_original = [ind[:] for ind in original_total]

    nueva[0][0] = "verde"

    assert original_total == copia_original