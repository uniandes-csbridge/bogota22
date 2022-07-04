"""
File: pelota_que_rebota.py
---------------------
"""

from graphics import Canvas

# Estos son necesarios para generar números aleatorios y pausar el tiempo
import random
import time

# Radio de la pelota
RADIO_PELOTA = 20

# Pausa entre los cuadros, en segundos
PAUSA = 0.02

"""
La velocidad en la dirección x y y en la que la pelota debe moverse. 
O sea, la pelota se moverá +5 o -5 en la dirección x y +5 o -5 en la dirección y,
siempre.
"""
VELOCIDAD_PELOTA = 5


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Pelota que rebota")

    # TODO: su codigo aca

    canvas.mainloop()


if __name__ == "__main__":
    main()
