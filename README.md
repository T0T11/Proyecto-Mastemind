- [Introduccion](#introduccion)
- [Manual](#manual)
    - [Pre-requisitos](#pre-requisitos)
    - [Instalación](#instalación)
    - [Uso](#uso)
- [Metodología](#metodología)
- [Descripción técnica](#descripción-técnica)
    - [Historias de usuario](#historias-de-usuario)
    - [Arquitectura de la aplicación](#arquitectura-de-la-aplicación)
- [Diseño](#diseño)
    - [Diagrama de Componentes](#diagrama-de-componentes)
- [Implementación](#implementación)
    - [Tecnologías y Herramientas utilizadas](#tecnologías-y-herramientas-utilizadas)
- [Pruebas](#pruebas)
    - [Test de unidad](#test-de-unidad)
- [Análisis del tiempo invertido](#análisis-del-tiempo-invertido)
    - [Wakatime](#wakatime)
    - [Justificación temporal](#justificación-temporal)
- [Uso de la IA](#uso-de-la-ia)
- [Coinclusión](#conclusión)
    - [Posibles mejoras](#posibles-mejoras)
    - [Dificultades](#dificultades)


# Introducción

Tomas Santiago Orellano - @T0T11
Jorge Pazos Domiguez - @jrgeepd

Somos alumnos de Desarollo de Aplicaciones Multiplataforma del IES de Teis. Hicimos este proyecto con el fin de demostrar nuestro aprendizaje en python,markdown y git.

# Manual

## Pre-requisitos
 requiere python = >=3.11
 requiere pipx 1.8.0 o mayor
 Entorno virtual ( opcional, pero muy recomedable)
 las dependencias listadas en pyproject.toml


## Instalación
Con el entorno virtual ya hecho (python -m venv venv), activado (.venv\Scripts\Activate) y con tu sesion de github logeada, escribes:  
`git clone https://github.com/T0T11/Proyecto-Mastemind`

mas tarde con uv ya instalado siguiendp los pasos de la web: https://docs.astral.sh/uv/getting-started/installation/ para descargar las dependencias del proyecto escribes:  
`uv sync` en la terminal

## Uso

el uso de la aplicacion es mediante la terminal con el comando `python main.py` en windows o `python3 main.py` en linux

# Metodología

Al princpio utilizamos la metodologia del Pair Programing debido a que creemos que trabajamos mejor asi, despues de hacer la parte "mas densa" del projecto en clase y siguiendo la metodologia anteriormente dicha, nos repartimos el trabajo en casa sumado a un pequeño feedback que nos haciamos mediante mensaje de texto .Posteriormente se uso la metodología del **TDD** con una especie de scrum que nos ofrece github a partir de las historias de usuario llamado **panel kanban**

Hemos escrito los casos test para poder pensar en el codigo y aparte nos hemos puesto como meta terminar las historias de usuario

# Descripción técnica

|   List (Implementado) / “On Scope”              |   Not List (No implementado) / “Out of Scope”       |   Unresolved                            |
|--------------------------------------------------|-----------------------------------------------------|------------------------------------------|
| Generación del código secreto                    | Selección por torneo                                | Modo versus o modo multijugador          |
| Selección de individuos por ruleta de pesos      | Uso de Elitismo                                     | Logging detallado por generación         |
| Cálculo de fichas negras y blancas               | Interfaz gráfica para jugar Mastermind              | Exportación automática de resultados     |
| Gráfico de evolución del fitness                 |                                                     |                                          |
| Visualización de intentos por consola            |                                                     |                                          |
| Separación modular                               |                                                     |                                          |
| Historias de usuario documentadas                |                                                     |                                          |


## Historias de usuario

## Historia de Usuario 1 – Generación del código secreto 
 como el jugador quiero que el sistema genere un código secreto de 4 colores aleatoriamente al inicio, con el fin de adivinarlo posteriormente.
 ### Criterios de aceptación 
    El código secreto se debera generar aleatoriamente solo entre los colores disponibles. 
    La longitud del código debe de no poder alterarse (por defecto, 4). 
    El código se debe de  mantener oculto hasta que la máquina adivine o termine la partida.
## Historia de Usuario 2 -  Visualizar las posibles combinaciones
 Como usuario quiero ver las combinaciones que propone la máquina en cada generación con el fin de ver la aproximacion y optimizacion del algoritmo genetico.
 ### Criterios de aceptación 
    Cada generación debe mostrarse en consola  con la mejor combinación propuesta y su valor de fitness.
    Se  debe indicar el número de generación correspondiente.
## Historia de Usuario 3 - Evaluación de fitness
 Como desarrollador quiero que la  función fitness  compare cada cromosoma(el intento) con el código secreto, para que el algoritmo genético pueda seleccionar las mejores combinaciones.
 ### Criterios de aceptación
    La función debe devolver en pantalla los aciertos exactos (tanto en color y  como en posición).
    La funcion debe poder contar los aciertos de color pero en la posicion incorrecta con el  fin de ayudar al algoritmo genetico.
## Historia de Usuario 4 - Seleccion de padres
 Como desarrollador quiero que el algoritmo filtre a los mejores individuos, con el fin de que, posteriormente, la descendencia de estos este mas cerca del codigo secreto.
 ### Criterios de aceptación
    Se debe seleccionar la mitad de la poblacion para la reproduccion.
    La seleccion de la descendencia se debe medir por su valor fitnesss.
## Historia de Usuario 5 - Cruce de individuos
 Como desarrolador quiero que el algoritmo cruce dos padres para la generacion de dos hijos, para asi, con el nivel de fitness que tienen los padres, tengan un fitness mayor los hijos.
 ### Criterios de aceptación
    el cruce debe devolver dos hijos fruto del curce de los dos padres.
## Historia de Usuario 6 - La posible mutacion.
 Como desarrolador, quiero una funcion de mutacion que deba cambiar de forma aleatoria un color del individuo en base a una probabilidad con el fin de tener diversidad genetica y evitar el estancamiento del algoritmo.
 ### Criterios de aceptación
    El color mutado debe de estar en las posibles probabilidades del color que puede albergar el cromosoma.
    Se deben poder mutar todas las posiciones.
## Historia de Usuario 7 - Ejecucion del Algoritmo Genetico en su totalidad
 Como usuario, quiero que la maquina ejecute el algoritmo genetico hasta adivinar el codigo secreto o hasta alcanzar el limite de intentos, con el fin de ver el proceso de como evoluciona el algoritmo genetico.
 ### Criterios de aceptación
    El algoritmo debe de detenerse si la maquina adivina el codigo.
    Se debe de informar si no se pudo adivinar el codigo con el limite de intentos
    Se debe mostrar los intentos que va haciendo la maquina para ver la evolucion del el algoritmo,
 

## Arquitectura de la aplicación

la aplicación tiene una arquitectura modular en la que cada archivo tiene su responsabilidad

# Diseño

## Diagrama de Componentes

![](/img/Diagrama%20Proyecto%20Mastermind.png)

# Implementación

## Tecnologías y Herramientas utilizadas

Python

Pytest Es un framework para facilitar y realizar los casos test para que sean más legibles y escalables. Referencia

pytest-sugar Es un plugin para mostrar de manera intuitiva los errores y fallos cometidos en nuestros test para mayor legibilidad Referencia

# Pruebas

## Test de unidad

todos los test usados han sido de unicidad:
```console
(proyecto-mastemind) PS C:\Users\pazos\Documents\proyecto - copia\Proyecto-Mastemind> pytest
Test session starts (platform: win32, Python 3.11.14, pytest 9.0.2, pytest-sugar 1.1.1)
rootdir: C:\Users\pazos\Documents\proyecto - copia\Proyecto-Mastemind
configfile: pytest.ini
plugins: sugar-1.1.1
collected 17 items                                                                                                                                                        

 test/test_calcular_fitness.py ✓✓✓✓✓✓✓                 41% ████▎     
 test/test_generar_poblacion.py ✓                        47% ████▊     
 test/test_generar_solucion.py ✓                         53% █████▍    
 test/test_poblar_siguiente_generacion.py ✓✓             65% ██████▌   
 test/test_reproducir_descendencia.py ✓✓✓✓✓             94% █████████▌
 test/test_seleccionar_padres.py ✓                      100% ██████████

Results (0.07s):
      17 passed
```


# Análisis del tiempo invertido

## Wakatime

Jorge

![](/img/Captura%20de%20pantalla%202026-01-07%20184041.png)
![](/img/Captura%20de%20pantalla%202026-01-07%20184058.png)

Tomás

![](/img/unnamed.png)
![](/img/unnamed2.png)

## Justificación temporal

Aunque el proyecto empezo conuna leve dificultad, tanto mi compañero y yo faltamos las dos primeras clases,  se pudo desarrolar de forma progresiva y flexible, realizándose mayoritariamente durante las sesiones de clase. El trabajo se fue ajustando sobre la marcha conforme avanzaba el aprendizaje, destinándose la última semana principalmente a la elaboración y revisión de la documentación final. 

# Uso de la IA

Durante el desarrollo del proyecto se utilizó una herramienta de Inteligencia Artificial generativa como apoyo al aprendizaje y al desarrollo del trabajo. Esta IA se empleó principalmente para resolver dudas conceptuales, orientar la estructura del proyecto, mejorar la comprensión del código y ayudar en la redacción de la documentación, sin sustituir en ningún momento el trabajo práctico ni la toma de decisiones por parte del alumnado

# Conclusión

El proyecto ha permitido aplicar de forma práctica los conocimientos adquiridos durante el curso, desarrollando una solución funcional para el juego Mastermind. A través de su implementación se ha reforzado la comprensión de conceptos como la lógica de programación, la resolución de problemas y el trabajo estructurado.

Asimismo, el desarrollo del proyecto ha favorecido el aprendizaje progresivo, la adaptación ante dificultades y la importancia de la documentación como parte final del proceso. En conjunto, el proyecto cumple los objetivos planteados y constituye una experiencia útil tanto a nivel técnico como formativo.

## Posibles mejoras

- Optimizar el algoritmo para reducir el número de intentos necesarios para resolver el juego.

- Mejorar la interfaz de usuario para hacer el programa más intuitivo y visual.

- Permitir distintos niveles de dificultad modificando la longitud del código o el número de colores.

- Añadir un sistema de estadísticas para analizar el rendimiento del algoritmo.

- Ampliar la documentación y comentarios del código para facilitar su mantenimiento.

## Dificultades

Las principales dificultades fueron la comprensión inicial del problema, la depuración del código y la organización del tiempo
