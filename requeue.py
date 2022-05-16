'''
    title: Trove Bomber Royale Requeue Script
    author: anonisnap
    date: 16/05/2022

    This script is capable of automatically requeuing for Bomber Royale within the game of Trove.
    It will automatically look for, and press, the Requeue button if, and only if, it matches the image supplied.
    Along with this, it is also capable of typing in chat, telling the other players to kill the bots first. This being possible if the "br_new_game.png" is found onscreen.
'''

from python_imagesearch.imagesearch import imagesearch
import pyautogui as pag
import keyboard as kb
from time import sleep

requeue_img = 'br_requeue.png'
new_game_img = 'br_new_game.png'

# Screen Offset, incase you're struggling with multiple monitors
screen_offset = [-1080, -446]


def main():
    print('> Starting REQUEUE  BOT (5s)')
    sleep(5)
    ingame = False

    # RECALIBRATING OFFSET
    # calculate_screen_offset()
    
    # Main Running Loop
    while(True):
        ingame = loop_calls(ingame)
        sleep(5)


# LOOP ACTIONS
# - Main Loop
# - Check if New Game
# - Check if Requeue
def loop_calls(is_ingame):
    # Check for Requeue Image
    is_ingame = loop_check_if_new_game(is_ingame)
    is_ingame = loop_requeue(is_ingame)
    return is_ingame


def loop_check_if_new_game(ingame):
    if not ingame:
        # Check for New Game Image
        pos = imagesearch(new_game_img)
        if (pos[0] != -1):
            # print('> Asking players to kill Bots')
            type_message('Please kill Bots before other Players vv3')
            ingame = True
    return ingame

def loop_requeue(ingame):
    # Check for New Game Image
    pos = imagesearch(requeue_img)
    # Click if Present
    if (pos[0] != -1):
        # print('> Thanking players for game')
        type_message('GG WP - Cya Later! \o')

        sleep(0.5)

        # print('> Clicking Requeue')
        click_requeue(pos)
        ingame = False
    return ingame


# USER ACTIONS
# - Click Requeue
# - Type Message
def click_requeue(pos):
    # Setup
    oldX, oldY = pag.position()

    # Actions
    pag.moveTo(pos[0] + screen_offset[0], pos[1] + screen_offset[1])
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(oldX, oldY)


def type_message(chat_msg, chat_room='/2'):
    # Actions
    kb.send('enter')
    kb.write(chat_room)
    kb.send('enter')
    sleep(0.2)
    kb.send('enter')
    kb.write(chat_msg)
    kb.send('enter')

# SCREEN OFFSET CALCULATIONS
def calculate_screen_offset():
    print('Move the Cursor to the Top Left of your monitors\n\tCtrl + C to exit')
    while(True):
        sleep(2)
        x, y = pag.position()
        print(f'Offset should be: [{x}, {y}]')
    


# STARTS THE SCRIPT
if __name__ == "__main__":
    main()
