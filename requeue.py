'''
    title: Trove Bomber Royale Requeue Script
    author: anonisnap
    date: 16/05/2022

    This script is capable of automatically requeuing for Bomber Royale within the game of Trove.
    It will automatically look for, and press, the Requeue button if, and only if, it matches the image supplied.
    Along with this, it is also capable of typing in chat, telling the other players to kill the bots first. This being possible if the "br_new_game.png" is found onscreen.
'''

import sys
from RequeueBot import RequeueBot


def main(debug_mode: bool = True):
    bot = RequeueBot()
    bot.set_debug(debug_mode)
    bot.run()

# STARTS THE SCRIPT
if __name__ == '__main__':
    try:
        debug = sys.argv[1]
        print(f'Debug: {debug}')
    except:
        pass
    main(debug.lower() == 'true')
