# https://www.waveshare.com/wiki/Libraries_Installation_for_RPi
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor

import time
import pwd

from buttons_HW import Buttons_HW, HWKey
from display_LCD import Display_LCD

class GameSelect:

    _lcd = None
    _buttons = None
    _debug_mode = False

    _index = 0

    def init(self):
        self._debug_mode = self._debug_detect()

        self._lcd = Display_LCD(self._debug_mode)
        self._lcd.init()

        self._buttons = Buttons_HW(self._debug_mode)
        self._buttons.listen_buttons(self.buttons_callback)

    def buttons_callback(self, button):
if button is HWKey.UP:
self._index = 0
elif button is HWKey.DOWN:
self._index = 1
        elif button is HWKey.LEFT:
            pass
        elif button is HWKey.RIGHT:
            pass
        elif button is HWKey.KEY_1:
            pass
        elif button is HWKey.KEY_2:
            pass
        elif button is HWKey.KEY_3:
            pass
        self.display()

    def display(self):
        image = Image.new("RGB", self._lcd.dimensions(), "WHITE")
        draw = ImageDraw.Draw(image)
        
        self._display_menu(draw)

        self._lcd.show_image(image)

    def _display_menu(self, draw):
        font = self._provide_font(10)
        #draw.text((14, 10), "Math Square", (0, 0, 0), font=font)
        #draw.text((14, 20), "Equations", (0, 0, 0), font=font)

        draw.text((10, 0), "1 2 3 4 5 6 7 8 9 0 - + ( ) * :", (0, 0, 0), font=self._provide_font(10, "Font.ttf"))
        draw.text((10, 10), "1 2 3 4 5 6 7 8 9 0 - + ( ) * :", (0, 0, 0), font=self._provide_font(12, "Font.ttf"))
        draw.text((10, 20), "1 2 3 4 5 6 7 8 9 0 - + ( ) * :", (0, 0, 0), font=self._provide_font(10, "maki.ttf"))
        draw.text((10, 30), "1 2 3 4 5 6 7 8 9 0 - + ( ) * :", (0, 0, 0), font=self._provide_font(12, "maki.ttf"))
        draw.text((10, 40), "1 2 3 4 5 6 7 8 9 0 - + ( ) * :", (0, 0, 0), font=self._provide_font(14, "nova.ttf"))
        draw.text((10, 50), "1 2 3 4 5 6 7 8 9 0 - + ( ) * :", (0, 0, 0), font=self._provide_font(18, "nova.ttf"))

        y = self._index + (self._index + 1) * 9
        draw.ellipse((5, y + 5, 9, y + 9), fill = 0)
    
    def _provide_font(self, size = 18, name = "Font.ttf"):
        path = 'fonts/{0}'.format(name) if self._debug_mode else '/home/pi/pi-game/fonts/{0}'.format(name)
        return ImageFont.truetype(path, size)

    def _debug_detect(self):
        try:
            # Check if user named `pi` exists
            # If exists then we known that code is running on Raspberry
            pwd.getpwnam('pi')
            return False
        except KeyError:
            return True

game_select = GameSelect()
game_select.init()
game_select.display()