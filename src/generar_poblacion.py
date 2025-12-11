import random
from parametros import *

def generar_población():
   return [[random.choice(COLORES)for i in range(TAMAÑO_CODIGO) ] for i in range(TAMAÑO_POBLACION)]
