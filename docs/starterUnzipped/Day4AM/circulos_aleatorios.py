"""
File: circulos_aleatorios.py
-------------------
Dibuja 10 círculos al azar de modo que cada círculo esté en la pantalla.

"""

from graphics import Canvas

# Esto es necesario para generar números aleatorios.
import random

# El número de circulos que tendremos que dibujar
NUM_CIRCLES = 10


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Circulos Aleatorios")

    # TODO: su código aquí

    canvas.mainloop()



if __name__ == '__main__':
    main()
