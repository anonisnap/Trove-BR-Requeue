import string
from time import sleep
import keyboard as kb

class Chat:
    def __init__(self):
        return

    def send_message(self, message: string, channel: string = '/2'):
        kb.send('enter')
        kb.write(channel)
        kb.send('enter')
        sleep(0.2)
        kb.send('enter')
        kb.write(message)
        kb.send('enter')
        return
