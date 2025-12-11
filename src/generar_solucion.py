import random
from parametros import *

def generar_solucion():
    return [random.choice(COLORES) for i in range(TAMAÑO_CODIGO)]
