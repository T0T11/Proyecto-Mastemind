from src.parametros import *

color_alelo  = {
    "negro": "⚫",
    "rojo": "🔴",
    "azul": "🔵",
    "amarillo": "🟡",
    "blanco": "⚪",
    "verde": "🟢" 
}

def cromosoma_emojis(cromosoma):
    resultado = ""
    for color in cromosoma:
        if color in color_alelo:
            resultado += color_alelo[color]
        else:
            resultado += color[0].upper()
    return resultado.strip()

def mostrar_feedback(cromosoma, fichas, generacion, fitness):
    cromosoma_str = cromosoma_emojis(cromosoma)
    fichas_str = "".join(fichas)
    if generacion < 10:
        print(
            f'Generación 0{generacion}: '
            f'{cromosoma_str} | '
            f'Fitness: {fitness} | '
            f'{fichas_str}'
        )
    else:
        print(
            f'Generación {generacion}: '
            f'{cromosoma_str} | '
            f'Fitness: {fitness} | '
            f'{fichas_str}'
        )