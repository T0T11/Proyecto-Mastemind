import random
from main import *

def generar_población():
    return [[random.choice(main.COLORES, TAMAÑO_CODIGO)] for i in range(main.TAMAÑO_POBLACION)]

print(generar_población)