import string


class ConsoleDebugger:
    def __init__(self, console_debug: bool = False):
        self.is_debug_mode = console_debug
        print(f'> Console Debugging -> ({console_debug})')
        # Debug to a File could be nice
        return

    def set_debug(self, console_debug: bool = True):
        self.is_debug_mode = console_debug
        boolean_as_string = ('On', 'Off')[console_debug]
        print(f'> Turning Debug Mode {boolean_as_string}')
        return

    def print(self, msg: string):
        if(self.is_debug_mode):
            print(msg)
        return
