"""
This file defines the necessary functions and definitions that students must
import in order to be able to write a new Karel program. Any new Karel file
must include the following line:

	from karel.stanfordkarel import *

Original Author: Nicholas Bowman
Credits: Kylie Jue
License: MIT
Version: 1.0.0
Email: nbowman@stanford.edu
Date of Creation: 10/1/2019
Last Modified: 3/31/2020
"""

import sys
import os
import tkinter as tk
from karel.KarelApplication import KarelApplication
from karel.KarelWorld import KarelWorld
from karel.Karel import Karel
from karel.kareldefinitions import DEFAULT_WORLD_FILE


"""
The following function definitions are defined as stubs so that IDEs can recognize
the function definitions in student code. These names are re-bound upon program
execution to asscoiate their behavior to the one particular Karel object located
in a given world.
"""
def moverse():
    pass


def girar_izquierda():
    pass


def poner_cono():
    pass


def recoger_cono():
    pass


def frente_despejado():
    pass


def frente_bloqueado ():
    pass


def izquierda_despejada():
    pass


def izquierda_bloqueada():
    pass


def derecha_despejada():
    pass


def derecha_bloqueada():
    pass


def conos_presentes():
    pass


def conos_ausentes():
    pass


def bolsa_con_conos():
    pass


def bolsa_sin_conos():
    pass


def rumbo_norte():
    pass


def sin_rumbo_norte():
    pass


def rumbo_este():
    pass


def sin_rumbo_este():
    pass


def rumbo_oeste():
    pass


def sin_rumbo_oeste():
    pass


def rumbo_sur():
    pass


def sin_rumbo_sur():
    pass


def pintarEsquina():
    pass


def esquina_color_es():
    pass


def aleatorio(p):
    pass

# Defined constants for ease of use by students when coloring corners
RED = "red"
BLACK = "black"
CYAN = "cyan"
DARK_GRAY = "gray30"
GRAY = "gray55"
GREEN = "green"
LIGHT_GRAY = "gray80"
MAGENTA = "magenta3"
ORANGE = "orange"
PINK = "pink"
WHITE = "snow"
BLUE = "blue"
YELLOW = "yellow"
BLANK = ""

def run_karel_program(world_file=None):
	# Extract the name of the file the student is executing
	student_code_file = sys.argv[0]

	if not world_file:
		# Find world file that matches program name
		base_filename = os.path.basename(student_code_file)
		module_name = os.path.splitext(base_filename)[0]
		# Look for existing file name in the worlds/ directory
		karel_world_file = f"worlds/{module_name}.w"
		if os.path.exists(karel_world_file):
			world_file = karel_world_file
		else:
			print(f"Could not find a world matching filename {module_name}.w, defaulting to default world.")
			default_world_file = f"worlds/{DEFAULT_WORLD_FILE}"
			if os.path.exists(default_world_file):
				world_file = default_world_file
			else:
				print("Could not find a default world to use, please specify a world filename.")
				return

	# Create the world as specified in the given world file
	try:
		# Attempt to open the file that has been specified
		world_file = open(world_file, "r")
	except OSError:
		try:
			# Before failing, look inside the worlds folder for this file
			world_file = open(os.path.join("worlds", world_file))
		except OSError:
			# Print warning to user and exit out of the program
			print(f"Could not find world file with name: {world_file}")
			return

	world = KarelWorld(world_file)

	# Create Karel and assign it to live in the newly created world
	karel = Karel(world)

	# Initialize root Tk Window and spawn Karel application
	root = tk.Tk()
	app = KarelApplication(karel, world, student_code_file, master=root)
	app.mainloop()
