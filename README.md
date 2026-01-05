- [Introduccion](#introduccion)
- [Manual](#manual)
    - [Pre-requisitos](#pre-requisitos)
    - [Instalación](#instalación)
    - [Uso](#uso)
- [Metodología](#metodología)
- [Descripción técnica](#descripción-técnica)
    - [Requisitos funcionales/no funcionales](#requisitos-funcionalesno-funcionales)
    - [Historias de usuario](#historias-de-usuario)
    - [Arquitectura de la aplicación](#arquitectura-de-la-aplicación)
- [Diseño](#diseño)
    - [Diagrama de Componentes](#diagrama-de-componentes)
- [Implementación](#implementación)
    - [Tecnologías y Herramientas utilizadas](#tecnologías-y-herramientas-utilizadas)
    - [Backend](#backend)
- [Pruebas](#pruebas)
    - [Coverage](#coverage)
    - [Test de unidad](#test-de-unidad)
    - [Test de integracion](#test-de-integracion)
- [Analisis del tiempo invertido](#analisis-del-tiempo-invertido)
    - [Clokify + Wakatime](#clokify-+-wakatime)
    - [Justificacion temporal](justificacion-temporal)
- [Uso de la IA](#uso-de-la-ia)
- [Coinclusion](#conclusion)
    - [Posibles mejoras](#posibles-mejoras)
    - [Dificultades](#dificultades)


Introducción

Tomas Santiago Orellano - @T0T11
Jorge Pazos Domiguez - @jrgeepd

Somos alumnos de Desarollo de Aplicaciones Multiplataforma del IES de Teis. Hicimos este proyecto con el fin de demostrar nuestro aprendizaje en python,markdown y git.

Manual

Pre-requisitos
 requiere python = >=3.11
 requiere pipx 1.8.0 o mayor
 Entorno virtual ( opcional, pero muy recomedable)
 las dependencias listadas en pyproject.toml


Instalación Windows/Linux
Con el entorno virtual ya hecho (python -m venv venv), activado (.venv\Scripts\Activate) y con tu sesion de github logeada, escribes:  
`git clone https://github.com/T0T11/Proyecto-Mastemind`

mas tarde con uv ya instalado siguiendp los pasos de la web: https://docs.astral.sh/uv/getting-started/installation/ para descargar las dependencias del proyecto escribes:  
`uv sync` en la terminal

Uso

el uso de la aplicacion es mediante la terminal con el comando `python main.py` en windows o `python3 main.py` en linux

Metodología

La metodología que hemos usado en estre proyecto ha sido el **TDD** con una especie de scrum que nos ofrece github a partir de las historias de usuario llamado **panel kanban**

Hemos escrito los casos test para poder pensar en el codigo y aparte nos hemos puesto como meta terminar las historias de usuario

Descripción técnica

Requisitos funcionales/no funcionales

...

Historias de usuario

...

Arquitectura de la aplicación

la aplicación tiene una arquitectura modular en la que cada archivo tiene su responsabilidad

Diseño

Diagrama de Componentes

```
Proyecto-Mastermind  
│  
├── Punto de entrada
│   │
├── main.py  
│
├── Componentes  
│   ├── parametros.py  
│   ├── generar_poblacion.py  
│   ├── calcular_fitness.py  
│   ├── seleccionar_padres.py  
│   ├── reproducir_descendencia.py  
│   ├── poblar_siguiente_generacio.py  
│   └── generar_solucion.py  
│  
└── Visualizacion  
    ├── visual_mastermind.py  
    └── graficos.py
```

Implementación

Tecnologías y Herramientas utilizadas

Python

Pytest Es un framework para facilitar y realizar los casos test para que sean más legibles y escalables. Referencia

pytest-sugar Es un plugin para mostrar de manera intuitiva los errores y fallos cometidos en nuestros test para mayor legibilidad Referencia

Pruebas

Test de unidad

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


Análisis del tiempo invertido

 Clokify + Wakatime

...

Justificación temporal

...

Uso de la IA

...

Conclusión

Posibles mejoras

...

Dificultades

...
