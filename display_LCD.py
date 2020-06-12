from PIL import Image
from PIL import ImageDraw

import psutil
from time import sleep

class Display_LCD:

	WIDTH = 128
	HEIGHT = 64
	_image = None
	_draw = None

	def __init__(self, is_debug, callback):
		if is_debug:
			self._image = Image.new("RGB", (self.WIDTH, self.HEIGHT), "BLACK")
			self._draw = ImageDraw.Draw(self._image)
		else:
			from luma.core.interface.serial import i2c, spi
			from luma.core.render import canvas
			from luma.oled.device import sh1106
			serial = spi(device=0, port=0)
			device = sh1106(serial, rotate=2)
			while True:
				with canvas(device) as draw:
					callback(draw)
				sleep(0.05)

	def debug_draw(self):
		return self._draw

	def debug_show(self):
		for proc in psutil.process_iter():
			if proc.name() == "display":
				proc.kill()
		self._image.show()

	def debug_clear(self):
		self._draw.rectangle((0,0,self.WIDTH,self.HEIGHT), fill="BLACK")

	def debug_getbuffer(self, image):
		return image
