import random
from src.parametros import *

def generar_poblacion():
   return [[random.choice(ALELOS)for i in range(NUMERO_GENES) ] for i in range(TAMAÑO_POBLACION)]
