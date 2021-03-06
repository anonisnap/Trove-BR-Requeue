'''
    title: Trove RequeueBot Start Script
    author: anonisnap
    date: 19/05/2022

    This script is responsible for the start-up logic needed to run the Trove Bomber Royale RequeueBot
    Its key features are Queueing up for a Bomber Royale Game, and then Requeueing until either stopped, or unexpected happenings (User gets Disconnected / Game Crashes) 
'''

import sys
from Bots.RequeueBot import RequeueBot


def main(debug_mode: bool = True):
    bot = RequeueBot(debug_mode)
    bot.run()

# STARTS THE SCRIPT
if __name__ == '__main__':
    try:     
        debug = sys.argv[1]
        main(debug.lower() == 'true')
        
    except IndexError:
        main(True)

    except KeyboardInterrupt:
        print('> Shutting down the RequeueBot')
        sys.exit()
