from PIL import ImageFont
from time import sleep
import pwd

from buttons_HW import Buttons_HW, HWKey
from display_LCD import Display_LCD
from menu_mode import MenuMode
from game_select import GameSelect
from equations import Equations

class PiGame:

	_index = 0
	_display = None

	_menu_mode = MenuMode.GAME_SELECT
	
	_game_select = None
	_equations = None

	def __init__(self):
		is_debug = self._debug_detect()
		if not is_debug:
			import RPi.GPIO as GPIO
			GPIO.setwarnings(False)
			GPIO.setmode(GPIO.BCM)

		buttons = Buttons_HW(is_debug)
		buttons.listen_buttons(self._buttons_callback)
		
		self._game_select = GameSelect()
		self._game_select.set_callback(self._change_menu_mode)

		self._equations = Equations()
		self._equations.set_callback(self._change_menu_mode)
		
		self._display = Display_LCD(is_debug, self._draw)

		if is_debug:
			self._draw(self._display.debug_draw())
			self._display.debug_show()

	def _draw(self, draw):
		if self._menu_mode == MenuMode.GAME_SELECT:
			self._game_select.draw(draw)
		elif self._menu_mode == MenuMode.EQUATIONS:
			self._equations.draw(draw)
		elif self._menu_mode == MenuMode.MATH_SQUARE:
			draw.text((2, 2), "TODO", fill="white")

	def _buttons_callback(self, button):
		print(button)
		if self._menu_mode == MenuMode.GAME_SELECT:
			self._game_select.handle_button(button)
		elif self._menu_mode == MenuMode.EQUATIONS:
			self._equations.handle_button(button)
		elif self._menu_mode == MenuMode.MATH_SQUARE:
			pass

		if self._debug_detect():
			self._display.debug_clear()
			self._draw(self._display.debug_draw())
			self._display.debug_show()

	def _change_menu_mode(self, menu_mode):
		self._menu_mode = menu_mode

	def _debug_detect(self):
		try:
			# Check if user named `pi` exists
			# If exists then we known that code is running on Raspberry
			pwd.getpwnam('pi')
			return False
		except KeyError:
			return True

PiGame()
