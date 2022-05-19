from time import sleep
from Bots.TroveBot import BasicBot


class RequeueBot(BasicBot):
    # Class Initialisation / Setup
    def __init__(self, started_in_debug_mode):
        super().__init__()
        super().set_offset((-1080, -446))
        super().set_debug(started_in_debug_mode)
        # Screen Interaction
        self.requeue_img = './images/br_requeue.png'
        self.new_game_img = './images/br_new_game.png'
        self.reconnect_img = './images/trove_reconnect.png'
        self.button_yes_img = './images/btn_yes.png'
        self.queue_for_bomber_royale_img = './images/queue_for_br.png'
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
        # Sleep Timer to allow more players to join
        sleep(5)
        super().debug_print('> Greeting new players')
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
        return

    def queue_for_bomber_royale(self):
        super().queue_for_bomber_royale()
        for i in range(5):
            super().debug_print(f'> Queueing for Bomber Royale (Attempt #{i})')
            queue_for_bomber_location = super().find_image(self.queue_for_bomber_royale_img)
            if(queue_for_bomber_location[0] != -1):
                has_queued = self.press_yes()
                if(has_queued):
                    return
            sleep(0.5)
        return

    def press_yes(self):
        yes_location = super().find_image(self.button_yes_img)
        if(yes_location[0] != -1):
            super().click_location(yes_location)
            return True
        return False

    def run(self, cooldown_timer: int = 5):
        sleep(cooldown_timer)
        self.queue_for_bomber_royale()
        while(True):
            self.new_game_started()
            self.requeue()
            self.reconnect()
            sleep(cooldown_timer)
