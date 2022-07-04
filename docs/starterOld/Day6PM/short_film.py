"""
File: short_film.py
----------------
Creates a short animated film with a sunset to start off with.
"""

from graphics import Canvas
import time

SUN_RADIUS = 25

# The amount the sun should move down the screen each frame
DESCENT = 2

# in seconds
DELAY = 0.03


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Short Film")

    # TODO: your code here

    canvas.mainloop()


if __name__ == '__main__':
    main()
