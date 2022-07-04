"""
File: catch_me_if_you_can.py
-------------------
This program draws several black "distractor" squares on the screen, along with a blue square that the user
tries to touch with their mouse.  But whenever the mouse touches the blue square, it moves to
another new random location!
"""

from graphics import Canvas
import random

# The dimensions of each black distractor square
DISTRACTOR_SIZE = 50

# The number of black squares on screen
N_DISTRACTORS = 20

# The dimensions of the blue square the user is trying to touch with the mouse
GOAL_SIZE = 60


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Catch Me If You Can")

    # TODO: your code here!

    canvas.mainloop()


if __name__ == '__main__':
    main()
