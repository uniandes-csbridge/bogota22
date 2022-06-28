
TRANSLATIONS = {
	"move": "moverse",
	"turn_left": "girar_izquierda",
	"put_beeper": "poner_cono",
	"pick_beeper": "recoger_cono",
    'front_is_clear': 'frente_despejado',
    'front_is_blocked': 'frente_bloqueado ',
    'left_is_clear': 'izquierda_despejada',
    'left_is_blocked': 'izquierda_bloqueada',
    'right_is_clear': 'derecha_despejada',
    'right_is_blocked': 'derecha_bloqueada',
    'beepers_present': 'conos_presentes',
    'no_beepers_present': 'conos_ausentes',
    'beepers_in_bag': 'bolsa_con_conos',
    'no_beepers_in_bag': 'bolsa_sin_conos',
    'facing_north': 'rumbo_norte',
    'not_facing_north': 'sin_rumbo_norte',
    'facing_east': 'rumbo_este',
    'not_facing_east': 'sin_rumbo_este',
    'facing_west': 'rumbo_oeste',
    'not_facing_west': 'sin_rumbo_oeste',
    'facing_south': 'rumbo_sur',
    'not_facing_south': 'sin_rumbo_sur',
    'paint_corner': 'pintarEsquina',
    'corner_color_is': 'esquina_color_es',
    'random': 'aleatorio'
}


KAREL_APP = """
		self.mod.turn_left = self.karel_action_decorator(self.karel.turn_left)
		self.mod.move = self.karel_action_decorator(self.karel.move)
		self.mod.pick_beeper = self.beeper_action_decorator(self.karel.pick_beeper)
		self.mod.put_beeper = self.beeper_action_decorator(self.karel.put_beeper)
		self.mod.facing_north = self.karel.facing_north
		self.mod.facing_south = self.karel.facing_south
		self.mod.facing_east = self.karel.facing_east
		self.mod.facing_west = self.karel.facing_west
		self.mod.not_facing_north = self.karel.not_facing_north
		self.mod.not_facing_south = self.karel.not_facing_south
		self.mod.not_facing_east = self.karel.not_facing_east
		self.mod.not_facing_west = self.karel.not_facing_west
		self.mod.front_is_clear = self.karel.front_is_clear
		self.mod.beepers_present = self.karel.beepers_present
		self.mod.no_beepers_present = self.karel.no_beepers_present
		self.mod.beepers_in_bag = self.karel.beepers_in_bag
		self.mod.no_beepers_in_bag = self.karel.no_beepers_in_bag
		self.mod.front_is_blocked = self.karel.front_is_blocked
		self.mod.left_is_clear = self.karel.left_is_clear
		self.mod.left_is_blocked = self.karel.left_is_blocked
		self.mod.right_is_clear = self.karel.right_is_clear
		self.mod.right_is_blocked = self.karel.right_is_blocked
		self.mod.paint_corner = self.corner_action_decorator(self.karel.paint_corner)
		self.mod.corner_color_is = self.karel.corner_color_is
		self.mod.random = KarelApplication.random
"""


def output_fns():
    for k, v in TRANSLATIONS.items():
        print("""
def {}():
    pass
        """.format(v))

def output_app_bindings():
    s = KAREL_APP
    for k,v in TRANSLATIONS.items():
        s = s.replace(f'mod.{k}', f'mod.{v}')
    print(s)

if __name__ == '__main__':
    # output_fns()
    output_app_bindings()

