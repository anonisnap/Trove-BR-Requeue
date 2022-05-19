from time import sleep
from Bots.TroveBot import BasicBot


class RequeueBot(BasicBot):
    # Class Initialisation / Setup
    def __init__(self):
        super().__init__()
        super().set_offset({-1080, -446})
        super().set_debug()
        # Screen Interaction
        self.requeue_img = './images/br_requeue.png'
        self.new_game_img = './images/br_new_game.png'
        self.reconnect_img = './images/trove_reconnect.png'
        # Player Interaction
        self.new_game_msg = 'Please kill Bots / AFK before other Players vv3'
        self.game_end_msg = 'GG WP - Cya Later! \o'
        #
        self.respawn_thread = None
        self.isIngame = False

    # Requeue Actions
    def requeue(self):
        super().debug_print('> Attempting to Requeue')
        # Find Image for Requeue
        requeue_image_location = super().find_image(self.requeue_img)
        # Check if Image was found
        if(requeue_image_location[0] == -1):
            super().debug_print('> Requeue Image was not found')
            return
        super().debug_print('> Requeueing')
        # Thank players for the game
        super().send_message(self.game_end_msg)
        # Click the Requeue Image
        super().click_location(requeue_image_location, 0.2)
        # Set ingame to False
        self.isIngame = False
        return

    def new_game_started(self):
        super().debug_print('> Attempt to chat with others')
        # If already ingame, don't do anything
        if(self.isIngame):
            super().debug_print('> Currently mid-game')
            return
        # Check if a New Game has Started
        new_game_image_location = super().find_image(self.new_game_img)
        if(new_game_image_location[0] == -1):
            super().debug_print('> Cannot find image for New Game')
            return
        super().debug_print('> Greeted new players')
        # Chat with Players
        super().send_message(self.new_game_msg)
        # Set ingame to True
        self.isIngame = True
        return

    def reconnect(self):
        super().debug_print('> Attempting to Reconnect to Trove Servers')
        reconnect_image_location = super().find_image(self.reconnect_img)
        if(reconnect_image_location[0] == -1):
            return
        super().debug_print('> Reconnecting to Servers')
        super().click_location(reconnect_image_location)

    def run(self, cooldown_timer: int = 5):
        while(True):
            sleep(cooldown_timer)
            self.new_game_started()
            self.requeue()
            self.reconnect()
