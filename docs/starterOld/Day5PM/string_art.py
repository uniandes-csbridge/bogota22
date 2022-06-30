"""
File: string_art.py
-------------------
This program creates string art using only straight lines.
"""

from graphics import Canvas

# Size of the canvas
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

# The number of pixels between end points of each line
LINE_SPACING = 20

# The number of lines we will have to draw
NUM_LINES = CANVAS_WIDTH // LINE_SPACING


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("String Art")

    # TODO: your code here!

    canvas.mainloop()


if __name__ == "__main__":
    main()
