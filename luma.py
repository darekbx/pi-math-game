from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106

from PIL import ImageFont
from time import sleep

import RPi.GPIO as GPIO

from buttons_HW import Buttons_HW, HWKey

class Luma:

	_index = 0

	def test(self):
		GPIO.setmode(GPIO.BCM)
		buttons = Buttons_HW(False)
		buttons.listen_buttons(self.buttons_callback)
		serial = spi(device=0, port=0)
		device = sh1106(serial, rotate=2)

		while True:
			with canvas(device) as draw:
    				#draw.rectangle(device.bounding_box, outline="white", fill="black")
				draw.text((12, 2), "Equations", fill="white")
				draw.text((12, 12), "Math Square", fill="white")
				y = self._index + (self._index + 0) * 9
				draw.ellipse((5, 5 + y, 9, 9 + y), fill="white")
				sleep(0.01)

	def buttons_callback(self, button):
		if button is HWKey.UP:
			self._index = 0
		elif button is HWKey.DOWN:
			self._index = 1

Luma().test()
#sleep(10)
