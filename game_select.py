from buttons_HW import HWKey
from menu_mode import MenuMode
from color import WHITE

class GameSelect:

	_index = 0
	_menu_mode_callback = None

	def set_callback(self, callback):
		self._menu_mode_callback = callback

	def draw(self, draw):
		draw.text((12, 2), "Equations", fill=WHITE)
		draw.text((12, 12), "Math Square", fill=WHITE)
		y = self._index + (self._index + 0) * 9
		draw.ellipse((5, 5 + y, 9, 9 + y), fill=WHITE)

	def handle_button(self, button):
		if button is HWKey.UP:
			self._index = 0
		elif button is HWKey.DOWN:
			self._index = 1
		elif button is HWKey.KEY_1 or button is HWKey.KEY_2 or button is HWKey.KEY_3:
			if self._index == 0:
				self._menu_mode_callback(MenuMode.EQUATIONS)
			elif self._index == 1:
				self._menu_mode_callback(MenuMode.MATH_SQUARE)