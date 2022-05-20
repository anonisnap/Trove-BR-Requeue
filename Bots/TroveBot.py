import array
import json
import string
import pyautogui as pag
import keyboard as kb
import numpy as np
from time import sleep, time
from python_imagesearch.imagesearch import imagesearch


class BasicBot:
    # Class Initialisation / Setup
    def __init__(self, started_in_debug_mode: bool = False):
        self.screen_offset = (0, 0)
        self.debug_mode = started_in_debug_mode
        self.debug = debug_printer()
        self.timer = timer()
        return

    def set_offset(self, offset: tuple):
        self.screen_offset = offset
        return

    def set_timer(self, duration: int):
        self.timer = timer(duration)
        return

    def set_debug(self, on: bool = True):
        if (on):
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

    # Opening Menus
    def open_menu_cheatsheet(self):
        self.open_menu('v')
        return

    # Character
    def open_character_sheet(self):
        self.open_menu('c')
        return

    def open_inventory(self):
        self.open_menu('b')
        return

    def open_class_select(self):
        self.open_menu('j')
        return

    # Progression
    def open_leaderboards(self):
        self.open_menu('k')
        return

    def open_collections(self):
        self.open_menu('y')
        return

    # Activities
    def open_adventures(self):
        self.open_menu('i')
        return

    def queue_for_bomber_royale(self):
        self.open_menu('b', 'ctrl')
        return

    # Shopping
    def open_store(self):
        self.open_menu('n')
        return

    def open_marketplace(self):
        self.open_menu('u')
        return

    # Social
    def open_clubs(self):
        self.open_menu('p')
        return

    def open_friends(self):
        self.open_menu('o')
        return

    def open_liked_worlds(self):
        self.open_menu('å')
        return

    # World
    def open_atlas(self):
        self.open_menu('a', 'ctrl')
        return

    def open_cornerstones(self):
        self.open_menu('¨')
        return

    def open_map(self):
        self.open_menu('m')
        return

    def open_welcome(self):
        self.open_menu('F1')
        return

    def open_claims(self):
        self.open_menu('l')
        return

    # Bot Actions

    def find_image(self, image: string, precision: float = 0.9):
        self.debug_print(f'\t> Searching for image: \'{image}\'')
        screen_location = imagesearch(image, precision)
        return screen_location

    def open_menu(self, menu_hotkey: chr, modifier_key: string = 'none'):
        if(modifier_key == 'none'):
            kb.send(menu_hotkey)
        else:
            kb.send(modifier_key, do_release=False)
            kb.send(menu_hotkey)
            kb.send(modifier_key, do_press=False)
        return

    # Internal Actions
    def __fix_offset(self, location: array):
        return np.add(location, self.screen_offset)

    def start_timer(self, duration):
        self.timer.start_timer(duration)
        return

    def check_timer(self):
        return self.timer.check_timer()

    # Debugging

    def debug_print(self, msg: string):
        self.debug.print(msg)
        return


class debug_printer:
    def __init__(self):
        self.debug_enable = False

    def set_debug(self, on: bool = True):
        self.debug_enable = on
        if (on):
            print(f'Debug Mode: {self.debug_enable}')
        return

    def print(self, msg: string):
        if(self.debug_enable):
            print(msg)
        return


class timer():
    def __init__(self, time_in_seconds: float = 0):
        self.duration = time_in_seconds
        self.start_time = None
        return

    def start_timer(self, duration: float = 0):
        self.duration = duration
        self.start_time = time()
        return

    def check_timer(self):
        end_time = (self.start_time + self.duration)
        return (time() > end_time)


class setting_reader:
    def get_screen_offset():
        settings_json_file = open('settings.json')
        setting_dict = json.load(settings_json_file)
