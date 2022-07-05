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
ANCHO_LADRILLO = math.floor((ANCHO_CANVAS - (NBRICK_COLUMNS + 1.0) * ESP_LADRILLO) / NBRICK_COLUMNS)

# Altura de cada ladrillo, en pixeles
ALTURA_LADRILLO = 8

# Desplazamiento de la fila de ladrillos superior desde la parte superior del canvas, en píxeles
ESPACIO_LADRILLO_ARRIBA = 70

# Stage 2: Crear la pelota que rebota

# Radio de la pelota, en pixeles
RADIO_PELOTA = 10

# La velocidad vertical de la pelota
VELOCIDAD_Y = 6.0

# La velocidad horizontal minima y maxima
# Tu velocidad initial en la direccion x debe ser entre estos valores.
VELOCIDAD_X_MIN = -6.0
VELOCIDAD_X_MAX = 6.0

# Pausa entre los cuadros, en segundos
PAUSA = 1 / 60

# Stage 3: Crear la raquetta

# Tamano de la raquetta
ANCHO_RAQUETA = 60
ALTURA_RAQUETA = 10

# Desplazamiento de la paleta hacia arriba 
# desde la pared inferior
RAQUETA_Y_ESP = 30

# Stage 5: Al final

# numero de turnos
NTURNS = 3

BOUNCE_SOUND = "bounce.au"


def main():
    canvas = Canvas(ANCHO_CANVAS, ALTURA_CANVAS)
    canvas.set_canvas_title("Breakout")

    # TODO: su codigo aca

    canvas.mainloop()


if __name__ == '__main__':
    main()
