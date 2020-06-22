from buttons_HW import HWKey
from menu_mode import MenuMode
from num_pad import NumPad
from color import WHITE
from random import randrange

class Equations:

	_correct = 0
	_failed = 0

	_level = 1
	_current_equation = None
	_num_pad = NumPad()
	_number = []

	def set_callback(self, callback):
		self._current_equation = self._create_equation(self._level)
		self._menu_mode_callback = callback

	def draw(self, draw):
		
		self._num_pad.draw(draw, 83, 19)

		draw.text((0, 0), "{0} = ?".format(self._current_equation), fill=WHITE)
		draw.text((0, 55), "Level {0}".format(self._level), fill=WHITE)
		draw.text((0, 28), "{value:{fill}{align}{width}}".format(value="".join(self._number), fill="_",align='<', width=2), fill=WHITE)
		draw.text((0, 44), "{0} / {1}".format(self._correct, self._failed), fill=WHITE)

	def handle_button(self, button):
		if self._num_pad.handle_button(button):
			return

		if button is HWKey.KEY_1:
			self._handle_key(self._num_pad.get_digit())
			
		if button is HWKey.KEY_2:
			self._check_result()

		if button is HWKey.KEY_3:
			self._num_pad.reset()
			self._menu_mode_callback(MenuMode.GAME_SELECT)

	def _handle_key(self, key):
		if isinstance(key, int):
			self._number.append("{0}".format(key))
		elif key == "backspace":
			if len(self._number) > 0:
				self._number.pop()
		elif key == "dot":
			pass

	def _check_result(self):
		if len(self._number) == 0:
			return

		result = "".join(self._number)
		is_correct = self._validate_result(self._current_equation, result)

		if is_correct:
			self._correct = self._correct + 1
			if self._correct % 10 == 0:
				self._level = self._level + 1
		else:
			self._failed = self._failed + 1

		self._number = []
		self._num_pad.reset()
		self._current_equation = self._create_equation(self._level)

	def _create_equation(self, level):
		operators = ["+", "-", "*"]
		operator_1 = operators[randrange(3)]
		operator_2 = operators[randrange(3)]
		a = randrange(9 + self._level) + 1
		b = randrange(9 + self._level) + 1
		c = randrange(9 + self._level) + 1
		return "{0} {1} {2} {3} {4}".format(a, operator_1, b, operator_2, c)

	def _validate_result(self, equation, result):
		equation_result = eval(equation)
		return int(equation_result) == int(result)