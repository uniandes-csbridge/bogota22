from karel.stanfordkarel import *

"""
File: karel_misterioso.py
------------------------------
"""


def main():
    for i in range(8):
        if frente_despejado():
            moverse()
        else:
            girar_izquierda()
            while derecha_bloqueada():
                moverse()
            girar_izquierda()
            girar_izquierda()
            girar_izquierda()
            for i in range(4):
                poner_cono()
                moverse()
                girar_izquierda()
            moverse()
            girar_izquierda()
            girar_izquierda()
            girar_izquierda()
            while frente_despejado():
                moverse()
            girar_izquierda()


# No debes editar mas allá de este punto
if __name__ == "__main__":
    run_karel_program()
