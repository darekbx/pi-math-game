# https://www.waveshare.com/wiki/Libraries_Installation_for_RPi
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor

from enum import Enum
import time

from display_LCD import Display_LCD
class MainMenu:

    lcd = None

    def init(self):
        self.lcd = Display_LCD(False)
        self.lcd.init()

    def display(self):
        image = Image.new("RGB", self.lcd.dimensions(), "WHITE")
        draw = ImageDraw.Draw(image)

        self.display_battery(draw, 100, False)

        self.lcd.show_image(image)

    def display_battery(self, draw, battery_level, is_charging=False):
        """
        Parameters
        ----------
        battery_level : int
            Battery level in percent
        """
        value = 18 * (battery_level / 100)
        draw.rectangle([(104, 2), (124, 10)], outline = 0) 
        draw.rectangle([(124, 6), (126, 8)], fill = 0)
        draw.rectangle([(106, 4), (104 + value, 8)], fill = 0)

        if is_charging:
            draw.line((108, 7, 114, 5, 114, 5, 114, 7, 114, 7, 120, 5), fill = "WHITE", width = 21)


mm = MainMenu()
mm.init()
mm.display()
