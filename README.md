# Trove Bomber Royale Requeue (This Readme is not Up To Date)

Getting tired of playing Bomber Royale in Trove?

Want to get the coins, but not put in the work?

Well! Here is the solution! _or, just a solution_

## Contents

- What is it?
- Settings things up
- Starting it
- How does it work?
- It's not working for me, what do I do?

## What is it?

The **Trove BR Requeue** script is a fairly simple Python Script, making use of Image Recognition to keep track of whether or not you're currently in an ongoing BR game, whether it has ended, or if you've just started a new one!

## Setting things up

To set things up, you'll need to have Python installed. On Windows, this is easily done with the Windows Store.

Something about the Screenshots

Maybe a visualisation of how

## Starting it

To start the script, simply run either of the `Bomber Royale Requeue.bat` batch scripts. If you have Python 3.9 (or maybe newer) the rest should work by itself

## How does it work?

The **Trove BR Requeue** script runs in the background, and every 5th second it will search your entire screen (all monitors) in an attempt to find one of the supported images

- br_requeue.png
- br_new_game.png
- btn_yes.png
- queue_for_br.png

If either of these were to be found, the script will either requeue you into another round, or send an informative message to the other players, asking them to kill the bots first

## It's not working for me, what do I do?

If the script is not working for you, it may be due to the images provided do not match your game, either caused by the graphics having changed or screen-resolution being different

### Images being different

To fix this, simply start Trove, enter Bomber Royale, and get similar screenshots to the ones provided, and then replace the provided ones with your own

### Screen Offset

If the cursor is clicking random places, and not on the buttons themselves, you may have to change the offset used for the clicking. Often occuring when using multiple monitors and the game isn't on the left-most monitor.

To change the offset, go into requeue.py and look for `# RECALIBRATING OFFSET`. Below this you'll find a Function call that has been commented out, 
```py
# calculate_screen_offset()
```
simply remove the `#` infront and run the script again, follow the instructions (which simply tell you to move the cursor to the top left most point of your screen) and remember what the scripts tells your your Offset should be
eg: `Offset should be: [-1080, -446]`
Once it has given you an Offset, you have to go into the script again, requeue.py, and near the top, change the Offset, `screen_offset = [x, y]`, to be as told
