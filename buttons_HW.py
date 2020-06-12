import threading
import time
from enum import Enum

import sys, tty, termios

class HWKey(Enum):
	UP = 0
	DOWN = 1
	CENTER = 2
	LEFT = 3
	RIGHT = 4
	KEY_1 = 5
	KEY_2 = 6
	KEY_3 = 7

class Buttons_HW:

	KEY_DETECT_DELAY = 0.2

	KEY_UP_PIN = 6
	KEY_DOWN_PIN = 19
	KEY_LEFT_PIN = 5
	KEY_RIGHT_PIN = 26
	KEY_CENTER_PIN = 13
	KEY_1_PIN = 21
	KEY_2_PIN = 20
	KEY_3_PIN = 16

	_callback = None
	_is_debug = False

	def __init__(self, is_debug):
		self._is_debug = is_debug

	def listen_buttons(self, callback):
		self.callback = callback
		if self._is_debug:
			threading.Thread(target = self.debug_keylogger).start()
		else:
			import RPi.GPIO as GPIO
			GPIO.setup(self.KEY_UP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
			GPIO.setup(self.KEY_DOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
			GPIO.setup(self.KEY_CENTER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
			GPIO.setup(self.KEY_LEFT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
			GPIO.setup(self.KEY_RIGHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
			GPIO.setup(self.KEY_1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
			GPIO.setup(self.KEY_2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
			GPIO.setup(self.KEY_3_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
			threading.Thread(target=self.buttons_worker).start()

	def buttons_worker(self):
		import RPi.GPIO as GPIO
		while True:
			if GPIO.input(self.KEY_UP_PIN) == False:
				self.handle_key(HWKey.UP)
			elif GPIO.input(self.KEY_DOWN_PIN) == False:
				self.handle_key(HWKey.DOWN)
			elif GPIO.input(self.KEY_CENTER_PIN) == False:
				self.handle_key(HWKey.CENTER)
			elif GPIO.input(self.KEY_LEFT_PIN) == False:
				self.handle_key(HWKey.LEFT)
			elif GPIO.input(self.KEY_RIGHT_PIN) == False:
				self.handle_key(HWKey.RIGHT)
			elif GPIO.input(self.KEY_1_PIN) == False:
				self.handle_key(HWKey.KEY_1)
			elif GPIO.input(self.KEY_2_PIN) == False:
				self.handle_key(HWKey.KEY_2)
			elif GPIO.input(self.KEY_3_PIN) == False:
				self.handle_key(HWKey.KEY_3)
			time.sleep(self.KEY_DETECT_DELAY)

	def handle_key(self, key):
		self.callback(key)

	def debug_keylogger(self):
		lock = threading.Lock()
		while True:
			with lock:
				fd = sys.stdin.fileno()
				old_settings = termios.tcgetattr(fd)
				try:
					tty.setraw(sys.stdin.fileno())
					ch = sys.stdin.read(1)
					if ch is 'w':
						self.handle_key(HWKey.UP)
					elif ch is 's':
						self.handle_key(HWKey.DOWN)
					elif ch is 'c':
						self.handle_key(HWKey.CENTER)
					elif ch is 'a':
						self.handle_key(HWKey.LEFT)
					elif ch is 'd':
						self.handle_key(HWKey.RIGHT)
					elif ch is '1':
						self.handle_key(HWKey.KEY_1)
					elif ch is '2':
						self.handle_key(HWKey.KEY_2)
					elif ch is '3':
						self.handle_key(HWKey.KEY_3)
					else:
						sys.exit()
				finally:
					termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)