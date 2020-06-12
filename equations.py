from buttons_HW import HWKey
from menu_mode import MenuMode
from num_pad import NumPad
from color import WHITE

class Equations:

	_num_pad = NumPad()
	_number = []

	def set_callback(self, callback):
		self._menu_mode_callback = callback

	def draw(self, draw):
		
		self._num_pad.draw(draw, 83, 19)

		draw.text((0, 0), "4 + 5 * 4 - 8 = ?", fill=WHITE)
		draw.text((0, 55), "Level 1", fill=WHITE)
		draw.text((0, 28), "".join(self._number), fill=WHITE)
		print(self._number)

	def handle_button(self, button):
		if self._num_pad.handle_button(button):
			return

		if button is HWKey.KEY_1:
			self._handle_key(self._num_pad.get_digit())
			
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