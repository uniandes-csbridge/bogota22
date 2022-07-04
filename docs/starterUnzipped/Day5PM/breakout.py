"""
File: breakout.py
-----------------
"""

import math
from graphics import Canvas
import random
import time


# Tamano del canvas, en pixeles
ANCHO_CANVAS = 420
ALTURA_CANVAS = 600

# Stage 1: Crear Ladrillos

# numeros de los ladrillos en cada fila
NBRICK_COLUMNS = 10

# Numero de filas de los ladrillos
NBRICK_ROWS = 10

# Espacio entre ladrillas de vecinos, en pixeles
ESP_LADRILLO = 4

# Ancho de cada ladrillo, en pixeles
ANCHO_LADRILLO = math.floor((CANVAS_WIDTH - (NBRICK_COLUMNS + 1.0) * BRICK_SEP) / NBRICK_COLUMNS)

# Altura de cada ladrillo, en pixeles
ALTURA_LADRILLO BRICK_HEIGHT = 8

# Desplazamiento de la fila de ladrillos superior desde la parte superior del canvas, en píxeles
ESPACIO_LADRILLO_ARRIBA = 70


def main():
    canvas = Canvas(ANCHO_CANVAS, ALTURA_CANVAS)
    canvas.set_canvas_title("Breakout")

    # TODO: su codigo aca

    canvas.mainloop()


if __name__ == '__main__':
    main()
