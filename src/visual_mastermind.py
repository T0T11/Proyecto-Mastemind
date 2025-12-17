from src.parametros import *
color_alelo  = {"negro": "⬛","rojo": "🟥","azul": 
                "🟦","amarillo": "🟨","blanco": "⬜","verde": "🟩" 
                }
def cromosoma_emojis(cromosoma):
    resultado = ""
    for color in cromosoma:
        if color in color_alelo:
            resultado += color_alelo[color] + " "
        else:
            resultado += color[0].upper() + " "
    return resultado.strip()
def mostrar_feedback(cromosoma,rojas,blancas,generacion,fitness):
    cromosoma_str = cromosoma_emojis(cromosoma)
    clavijas_str = "🔴" * rojas + "⚪" *blancas
    print("Generacion " + str(generacion) + ": " + cromosoma_str + " | Fitness: " + str(fitness) + " | Clavijas: " + clavijas_str)
