import array
import json
import string
import pyautogui as pag
import numpy as np
from time import time
from python_imagesearch.imagesearch import imagesearch

from Bots.Modules.Chat import Chat
from Bots.Modules.ConsoleDebugger import ConsoleDebugger
from Bots.Modules.Hotkeys import Hotkeys


class BasicBot:
    # Class Initialisation / Setup
    def __init__(self, started_in_debug_mode: bool = False):
        self.screen_offset = (0, 0)
        self.debug_mode = started_in_debug_mode
        self.debug = ConsoleDebugger()
        self.timer = timer()
        self.game_chat = Chat()
        self.hotkey_manager = Hotkeys()
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
        self.hotkey_manager.open_menu('v')
        return

    # Character
    def open_character_sheet(self):
        self.hotkey_manager.open_menu('c')
        return

    def open_inventory(self):
        self.hotkey_manager.open_menu('b')
        return

    def open_class_select(self):
        self.hotkey_manager.open_menu('j')
        return

    # Progression
    def open_leaderboards(self):
        self.hotkey_manager.open_menu('k')
        return

    def open_collections(self):
        self.hotkey_manager.open_menu('y')
        return

    # Activities
    def open_adventures(self):
        self.hotkey_manager.open_menu('i')
        return

    def queue_for_bomber_royale(self):
        self.hotkey_manager.open_menu('b', 'ctrl')
        return

    # Shopping
    def open_store(self):
        self.hotkey_manager.open_menu('n')
        return

    def open_marketplace(self):
        self.hotkey_manager.open_menu('u')
        return

    # Social
    def open_clubs(self):
        self.hotkey_manager.open_menu('p')
        return

    def open_friends(self):
        self.hotkey_manager.open_menu('o')
        return

    def open_liked_worlds(self):
        self.hotkey_manager.open_menu('å')
        return

    # World
    def open_atlas(self):
        self.hotkey_manager.open_menu('a', 'ctrl')
        return

    def open_cornerstones(self):
        self.hotkey_manager.open_menu('¨')
        return

    def open_map(self):
        self.hotkey_manager.open_menu('m')
        return

    def open_welcome(self):
        self.hotkey_manager.open_menu('F1')
        return

    def open_claims(self):
        self.hotkey_manager.open_menu('l')
        return

    # Bot Actions

    def find_image(self, image: string, precision: float = 0.9):
        self.debug_print(f'\t> Searching for image: \'{image}\'')
        screen_location = imagesearch(image, precision)
        return screen_location


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
