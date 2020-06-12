from buttons_HW import HWKey
from color import WHITE
from color import BLACK

class NumPad:

	_selected_x_index = 0
	_selected_y_index = 0

	def reset(self):
		self._selected_x_index = 0
		self._selected_y_index = 0

	def get_digit(self):
		if self._selected_y_index == 3:
			if self._selected_x_index == 0:
				return "dot"
			elif self._selected_x_index == 1:
				return 0
			elif self._selected_x_index == 2:
				return "backspace"

		return (self._selected_x_index + 1) + self._selected_y_index * 3

	def draw(self, draw, base_x, base_y):
		draw.rectangle((base_x, base_y, base_x + 44, base_y + 44), outline=WHITE, fill=BLACK)

		nums = []
		nums.extend(range(1, 10))
		nums.append('.')
		nums.append(0)
		nums.append('<')

		x_offset = 9
		y_offset = 2
		x = x_offset
		y = y_offset
		x_index = 0
		y_index = 0

		for index, num in enumerate(nums):

			if self._selected_x_index == x_index and self._selected_y_index == y_index:
				draw.rectangle((base_x + x - 2, base_y + y, base_x + x + 6, base_y + y + 10), outline=WHITE, fill=BLACK)

			draw.text((base_x + x, base_y + y), "{0}".format(num), fill=WHITE)

			x_index = x_index + 1
			x = x + 10
			if (index + 1) % 3 == 0:
				y += 10
				x = x_offset
				x_index = 0
				y_index = y_index + 1

	def handle_button(self, button):
		if button is HWKey.UP:
			self._selected_y_index = min(3, max(0, self._selected_y_index - 1))
			return True
		elif button is HWKey.DOWN:
			self._selected_y_index = min(3, max(0, self._selected_y_index + 1))
			return True
		elif button is HWKey.LEFT:
			self._selected_x_index = min(2, max(0, self._selected_x_index - 1))
			return True
		elif button is HWKey.RIGHT:
			self._selected_x_index = min(2, max(0, self._selected_x_index + 1))
			return True
		return False