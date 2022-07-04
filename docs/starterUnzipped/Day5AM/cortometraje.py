"""
File: cortometraje.py
----------------
"""

from graphics import Canvas
import time  # Esto es necesario para pausar el tiempo. No lo borre

RADIO_DEL_SOL = 25

# La cantidad que el sol debe moverse por el lienzo en cada cuadro
DESCENT = 2

# Pausa entre los cuadros, en segundos
PAUSA = 0.03


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Cortometraje")

    # TODO: animar una pelicula!

    canvas.mainloop()


if __name__ == '__main__':
    main()
