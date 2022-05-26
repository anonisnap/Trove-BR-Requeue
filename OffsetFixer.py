import json
from time import sleep
import pyautogui

from Bots.Modules.Settings import Settings


def main() -> None:
    # Create the Settings Object
    bot_settings = Settings()

    # Ask User to move the Cursor to the Top-Left corner of their Left-most Monitor
    inform_user()
    # Let User move Cursor
    sleep(1)
    # Get Cursorposition
    offset = get_cursor_position()
    # Set Offset to Location
    bot_settings.set_offset(offset[0], offset[1])
    # Dump into the Settings File
    with open('Bots/settings.json', 'w') as settings_file:
        json.dump(bot_settings.__dict__, settings_file, indent=4)
    # Inform User the Offset has been set
    print(f'Your Offset has now been set as ({offset[0]}, {offset[1]})')


def inform_user() -> None:
    print('Please move your Cursor to the Top Left Corner, of your Left most Monitor')
    sleep(1)
    print('Wait for further notice...')


def get_cursor_position() -> dict:
    pos = pyautogui.position()
    print('Offset has been Measured. You are free to move your Cursor again')
    return pos

if __name__ == '__main__':
    main()
