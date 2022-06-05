class Settings(object):
    loop_delay: int
    screen_offset: list

    def __init__(self, loop_delay: int = 5, screen_offset: list = [0, 0]) -> None:
        self.loop_delay = loop_delay
        self.screen_offset = screen_offset

    def set_loop_delay(self, val: int) -> None:
        self.loop_delay = val
        return

    def set_offset(self, x: int = 0, y: int = 0) -> None:
        self.screen_offset[0] = x
        self.screen_offset[1] = y
        return
