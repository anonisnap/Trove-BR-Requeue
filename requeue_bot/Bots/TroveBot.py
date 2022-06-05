import array
import os
import json
import string
from types import SimpleNamespace
import pyautogui as pag
import keyboard as kb
import numpy as np
from time import sleep, time
from python_imagesearch.imagesearch import imagesearch

from Bots.Modules.Chat import Chat
from Bots.Modules.ConsoleDebugger import ConsoleDebugger
from Bots.Modules.Hotkeys import Hotkeys
from Bots.Modules.Settings import Settings


class BasicBot:
    # Class Initialisation / Setup
    def __init__(self, started_in_debug_mode: bool = False) -> None:
        # Initialise Variables
        self.screen_offset = {'x': 0, 'y': 0}
        self.debug_mode = started_in_debug_mode
        self.debug = ConsoleDebugger(self.debug_mode)
        self.timer = timer()
        self.game_chat = Chat()
        self.hotkey_manager = Hotkeys()

        #
        self.__set_settings()
        return

    def set_timer(self, duration: int) -> None:
        self.timer = timer(duration)
        return

    def set_debug(self, set_on: bool = True) -> None:
        self.debug_mode = set_on
        self.debug.set_debug(set_on)
        return

    # User Imitation
    def send_message(self, message: string, channel: string = '/2') -> None:
        self.debug_print(f'\t> Sending a Message: \'{message}\'')
        self.game_chat.send_message(message, channel)
        return

    def click_location(self, pos: array, move_time: float = 0) -> None:
        self.debug_print(f'\t> Moving to location: \'{pos}\'')
        oldX, oldY = pag.position()
        pos = self.__fix_offset(pos)
        pag.moveTo(pos[0], pos[1], duration=move_time)
        pag.click()
        pag.moveTo(oldX, oldY)
        return

    def walk(self, direction: string, duration: float = 1) -> None:
        # Extract the direction
        direction = direction.lower()[0]

        # Ensure direction is a movement key
        if (direction != 'w' or direction != "d" or direction != "s" or direction != "d"):
            self.debug_print(f'{direction} is not a direction')
            return

        # Press the Key for a defined time
        self.debug_print(f'Walking {direction}')
        kb.press(direction)
        sleep(duration)
        kb.release(direction)
        return

    def jump(self, direction: string = ""):
        kb.send('space')
        if (direction != ""):
            self.walk(direction)
        return

    # Opening Menus
    def open_menu_cheatsheet(self) -> None:
        self.hotkey_manager.open_menu('v')
        return

    # Character
    def open_character_sheet(self) -> None:
        self.hotkey_manager.open_menu('c')
        return

    def open_inventory(self) -> None:
        self.hotkey_manager.open_menu('b')
        return

    def open_class_select(self) -> None:
        self.hotkey_manager.open_menu('j')
        return

    # Progression
    def open_leaderboards(self) -> None:
        self.hotkey_manager.open_menu('k')
        return

    def open_collections(self) -> None:
        self.hotkey_manager.open_menu('y')
        return

    # Activities
    def open_adventures(self) -> None:
        self.hotkey_manager.open_menu('i')
        return

    def queue_for_bomber_royale(self) -> None:
        self.hotkey_manager.open_menu('b', 'ctrl')
        return

    # Shopping
    def open_store(self) -> None:
        self.hotkey_manager.open_menu('n')
        return

    def open_marketplace(self) -> None:
        self.hotkey_manager.open_menu('u')
        return

    # Social
    def open_clubs(self) -> None:
        self.hotkey_manager.open_menu('p')
        return

    def open_friends(self) -> None:
        self.hotkey_manager.open_menu('o')
        return

    def open_liked_worlds(self) -> None:
        self.hotkey_manager.open_menu('å')
        return

    # World
    def open_atlas(self) -> None:
        self.hotkey_manager.open_menu('a', 'ctrl')
        return

    def open_cornerstones(self) -> None:
        self.hotkey_manager.open_menu('¨')
        return

    def open_map(self) -> None:
        self.hotkey_manager.open_menu('m')
        return

    def open_welcome(self) -> None:
        self.hotkey_manager.open_menu('F1')
        return

    def open_claims(self) -> None:
        self.hotkey_manager.open_menu('l')
        return

    # Bot Actions

    def find_image(self, image: string, precision: float = 0.9) -> array:
        self.debug_print(f'\t> Searching for image: \'{image}\'')
        screen_location = imagesearch(image, precision)
        if(screen_location[0] == -1): 
            return None
        else:
            return screen_location

    # Internal Actions

    def __fix_offset(self, location: array) -> array:
        return np.add(location, self.screen_offset)

    def start_timer(self, duration) -> None:
        self.timer.start_timer(duration)
        return

    def check_timer(self) -> bool:
        return self.timer.check_timer()

    def __set_settings(self) -> None:
        file_path = 'requeue_bot/Bots/settings.json'
        if (not os.path.exists(file_path)) or os.stat(file_path).st_size == 0:
            with open(file_path, 'w') as new_settings_file:
                self.debug_print('> Creating new Settings File')
                new_settings = Settings()
                json.dump(vars(new_settings), new_settings_file, indent=4)
        with open(file_path, 'r') as settings:
            user_settings = (
                json.load(settings, object_hook=lambda d: SimpleNamespace(**d)))
            self.screen_offset = user_settings.screen_offset
            self.debug_print(
                f'Offset : ({self.screen_offset[0]}, {self.screen_offset[1]})')
        return

    # Debugging

    def debug_print(self, msg: string) -> None:
        self.debug.print(msg)
        return


class timer():
    def __init__(self, time_in_seconds: float = 0) -> None:
        self.duration = time_in_seconds
        self.start_time = None
        return

    def start_timer(self, duration: float = 0) -> None:
        self.duration = duration
        self.start_time = time()
        return

    def check_timer(self) -> bool:
        end_time = (self.start_time + self.duration)
        return (time() > end_time)
