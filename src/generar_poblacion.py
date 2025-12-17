import random
from src.parametros import *

def generar_poblacion():
   return [[random.choice(ALELOS)for i in range(GEN) ] for i in range(TAMAÑO_POBLACION)]
