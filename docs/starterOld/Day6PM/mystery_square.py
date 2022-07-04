"""
File: mystery_square.py
-------------------
This program creates a centered square that changes color randomly every second.
"""

from graphics import Canvas

# Needed for pausing for animation.  Don't remove this.
import time

# Size of the centered square
SQUARE_SIZE = 400

# Delay between color changes, in seconds
DELAY = 1


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Mystery Square")

    # TODO: your code here

    canvas.mainloop()


if __name__ == "__main__":
    main()
