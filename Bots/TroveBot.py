import array
import string
import pyautogui as pag
import keyboard as kb
import numpy as np
from time import sleep
from python_imagesearch.imagesearch import imagesearch


class BasicBot:
    # Class Initialisation / Setup
    def __init__(self):
        self.screen_offset = (0, 0)
        self.debug_mode = False
        self.debug = debug_printer()
        return

    def set_offset(self, offset: tuple):
        self.screen_offset = offset
        return

    def set_debug(self, on: bool = True):
        print('> Turning on Debug Mode')
        self.debug_mode = on
        self.debug.set_debug(on)
        return

    # User Imitation
    def send_message(self, message: string, channel: string = '/2'):
        self.debug_print(f'\t> Sending a Message: \'{message}\'')
        kb.send('enter')
        kb.write(channel)
        kb.send('enter')
        sleep(0.2)
        kb.send('enter')
        kb.write(message)
        kb.send('enter')
        return

    def click_location(self, pos: array, move_time: float = 0):
        self.debug_print(f'\t> Moving to location: \'{pos}\'')
        oldX, oldY = pag.position()
        pos = self.__fix_offset(pos)
        pag.moveTo(pos[0], pos[1], duration=move_time)
        pag.click()
        pag.moveTo(oldX, oldY)
        return

    # Bot Actions
    def find_image(self, image: string, precision: float = 0.8):
        self.debug_print(f'\t> Searching for image: \'{image}\'')
        screen_location = imagesearch(image, precision)
        return screen_location

    # Internal Actions
    def __fix_offset(self, location: array):
        print(f'Location: {type(location)}')
        print(f'Offset  : {type(self.screen_offset)}')
        return np.add(location, self.screen_offset)

    # Debugging
    def debug_print(self, msg: string):
        self.debug.print(msg)
        return

class debug_printer:
    def __init__(self):
        self.debug_enable = False

    def set_debug(self, on: bool = True):
        self.debug_enable = on
        print(f'Debug Mode: {self.debug_enable}')
        return

    def print(self, msg: string):
        if(self.debug_enable):
            print(msg)
        return
