import string
import keyboard as kb

class Hotkeys:
    def __init__(self) -> None:
        return

    def open_menu(self, menu_hotkey: chr, modifier_key: string = 'none'):
        if(modifier_key == 'none'):
            kb.send(menu_hotkey)
        else:
            kb.send(modifier_key, do_release=False)
            kb.send(menu_hotkey)
            kb.send(modifier_key, do_press=False)
        return
