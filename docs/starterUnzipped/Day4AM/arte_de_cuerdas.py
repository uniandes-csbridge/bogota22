"""
File: arte_de_cuerdas.py
-------------------
"""

from graphics import Canvas


# El tamaño de la pantalla
ANCHO_DE_APLICACION = 400
ALTURA_DE_APLICACION = 400

# El número de píxeles entre los puntos finales de la línea
ESPACIADO_ENTRE_LINEAS = 20

# El número de líneas que tendremos que dibujar
NUM_LINES = ANCHO_DE_APLICACION // ESPACIADO_ENTRE_LINEAS


def main():
    canvas = Canvas(ANCHO_DE_APLICACION, ALTURA_DE_APLICACION)
    canvas.set_canvas_title("Arte de Cuerdas")

    # TODO: su código aquí

    canvas.mainloop()


if __name__ == "__main__":
    main()
