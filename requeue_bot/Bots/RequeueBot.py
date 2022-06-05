import string
import sys
from time import sleep
from Bots.TroveBot import BasicBot


class RequeueBot(BasicBot):
    # Class Initialisation / Setup
    def __init__(self, started_in_debug_mode) -> None:
        # Super Init Call
        super().__init__(started_in_debug_mode)

        # Screen Interaction
        self.requeue_img                    = 'requeue_bot/images/br_requeue.png'
        self.new_game_img                   = 'requeue_bot/images/br_new_game.png'
        self.reconnect_img                  = 'requeue_bot/images/trove_reconnect.png'
        self.button_yes_img                 = 'requeue_bot/images/btn_yes.png'
        self.queue_for_bomber_royale_img    = 'requeue_bot/images/queue_for_br.png'
        self.game_crash_img                 = 'requeue_bot/images/trove_crashed.png'
        self.player_count_10                = 'requeue_bot/images/player_count_10.png'
        self.player_count_9                 = 'requeue_bot/images/player_count_9.png'
        self.player_count_head              = 'requeue_bot/images/player_count_head.png'

        # Player Interaction
        self.new_game_msg = 'Please kill Bots / AFK before other Players vv3'
        self.game_end_msg = 'GG WP - Cya Later! \o'
        #
        self.isIngame = False

    # Requeue Actions
    def requeue(self) -> None:
        super().debug_print('> Attempting to Requeue')

        # Find Image for Requeue
        requeue_image_location = super().find_image(self.requeue_img)

        super().debug_print('> Requeueing')

        # Thank players for the game
        super().send_message(self.game_end_msg)

        # Click the Requeue Image
        super().click_location(requeue_image_location, 0.2)

        # Set ingame to False
        self.isIngame = False
        return

    def new_game_started(self) -> None:
        super().debug_print('> Attempt to chat with others')

        # If already ingame, don't do anything
        if(self.isIngame):
            super().debug_print('> Currently mid-game')
            return

        # Jump to remove wings
        sleep(2)
        super().debug_print("> Jumping to remove Wings")
        super().jump()

        # Sleep Timer to allow more players to join
        sleep(3)
        super().debug_print('> Greeting new players')

        # Chat with Players
        super().send_message(self.new_game_msg)

        # Start a Respawn Timer
        self.start_respawn_timer()

        # Set ingame to True
        self.isIngame = True

        # Buffer Timer
        sleep(10)

        return

    def check_if_respawn(self) -> None:
        if(super().check_timer() or self.check_player_count()):
            super().debug_print('> Respawning')
            super().send_message('/respawn')
        return

    def check_player_count(self) -> bool:
        p_10 = super().find_image(self.player_count_10)
        p_9 = super().find_image(self.player_count_9)
        self.debug_print(f'\t\t>> Player Count 10: {p_10 != None}\n\t\t>> Player Count 9: {p_9 != None}')
        if (p_10 or p_9):
            return False
        stuck_in_lobby = super().find_image(self.player_count_head) == None
        if (stuck_in_lobby):
            self.queue_for_bomber_royale()
            return False
        return True

    def start_respawn_timer(self) -> None:
        super().start_timer(120)
        return

    def reconnect(self) -> None:
        super().debug_print('> Attempting to Reconnect to Trove Servers')
        reconnect_image_location = super().find_image(self.reconnect_img)

        # Press Reconnect
        super().debug_print('> Reconnecting to Servers')
        super().click_location(reconnect_image_location)
        return

    def queue_for_bomber_royale(self) -> None:
        # Send Queue for Bomber Royale Hotkey
        super().queue_for_bomber_royale()

        # Check for Image
        for i in range(5):
            super().debug_print(f'> Queueing for Bomber Royale (Attempt #{i})')
            queue_for_bomber_location = super().find_image(self.queue_for_bomber_royale_img)
            if(queue_for_bomber_location != None):
                has_queued = self.press_yes()
                if(has_queued):
                    return
            sleep(0.5)
        return

    def press_yes(self) -> bool:
        yes_location = super().find_image(self.button_yes_img)
        if(yes_location[0] != -1):
            super().click_location(yes_location)
            return True
        return False

    def check_for_images(self) -> string:
        if(super().find_image(self.requeue_img)): return "requeue"
        if(super().find_image(self.new_game_img)): return "new_game"
        if(super().find_image(self.reconnect_img)): return "reconnect"
        if(super().find_image(self.game_crash_img)): return "game_crash"
        return None


    def run(self, cooldown_timer: int = 5):
        sleep(cooldown_timer)
        self.queue_for_bomber_royale()

        # Action Loop
        while(True):
            img = self.check_for_images()

            match img:
                case "requeue":
                    self.requeue()
                case "new_game":
                    self.new_game_started()
                case "reconnect":
                    self.reconnect()
                case "game_crash":
                    super().debug_print('The Game has Crashed. Shutting Down')
                    sys.exit(1)                    

            if (self.isIngame):
                self.check_if_respawn()
            sleep(cooldown_timer)
