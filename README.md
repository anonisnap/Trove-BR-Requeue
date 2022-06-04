# Trove Bomber Royale Requeue

Getting tired of playing Bomber Royale in Trove?

Want to get the coins, but not put in the work?

Well! Here is the ~~bad~~ solution!

## Table of Contents

- [What is it?](#what-is-it-)
- [How does it work?](#how-does-it-work-)
- [Setting things up](#setting-things-up)
  - [Screenshots](#screenshots)
  - [Changing the Screenshots](#changing-the-screenshots)
- [Starting it](#starting-it)
- [It's not working for me, what do I do?](#it-s-not-working-for-me--what-do-i-do-)
  - [Bot is not clicking at all](#bot-is-not-clicking-at-all)
  - [Clicking the Wrong Place](#clicking-the-wrong-place)

## What is it?

In the main folder, you'll find 3 `.bat` scripts, the `Python Dependencies` script, and 2 different `Bomber Royale Requeue` scripts.

The `Python Dependencies` will let you easily download the needed Dependencies for Python.

The `Bomber Royale Requeue` scripts both do the same, and function to let you run the Python Bot.

## How does it work?

The **Trove BR Requeue** script runs in the background, and every 5th second it will search your entire screen (all monitors) in an attempt to find one of the supported images

- br_requeue.png
- br_new_game.png
- btn_yes.png
- queue_for_br.png

If either of these were to be found, the script will either requeue you into another round, or send an informative message to the other players, asking them to kill the bots first

## Setting things up

To set things up, you'll need to have Python installed. On Windows, this is easily done with the Windows Store.

Once Python has been installed, I suggest running the `Python Dependencies` file, which will take care of installing the needed Python Dependencies

After that, the bot should be able to run, though it may not work yet due to the bot using **Screenshots** to determine how to act

### Screenshots

Because the Python Bot uses Screenshots, you may need to change the screenshots yourself. Currently the Bot requires these following images to work. And you'll find them in the `requeue_bot/images` folder:

<table>
    <th>br_requeue</th>
    <th>br_new_game</th>
    <tr> 
        <td align=center>
            <img src=requeue_bot/images/br_requeue.png/>
        </td>
        <td align=center>
            <img src=requeue_bot/images/br_new_game.png/>
        </td>
    </tr>
    <th>btn_yes</th>
    <th>queue_for_br</th>
    <tr>
        <td align=center>
            <img src=requeue_bot/images/btn_yes.png/>
        </td>
        <td align=center>
            <img src=requeue_bot/images/queue_for_br.png/>
        </td>
    </tr>
<table>

### Changing the Screenshots

I'll guide you through the process of changing a screenshot. This example will be using the `queue_for_br` image.

To replace any of the screenshots, the easiest way is to first find the file itself, Right Click it, and click Edit. This will open the image in Paint.

![queueue_for_br in paint](guide/edit_image.png)

Then, head into Trove, and reproduce the screen where the screenshot was taken, for this it was simply attempting to queue for Bomber Royale.

To get a Screenshot of this, on your Keyboard press `Alt` and `PrtSc`, _also known as Print Screen_.

![Confirm Queue for Bomber Royale](guide/confirm_queue.png)

Then go back to paint. Here you just Paste the image and then select the part you need with the Select Tool.

![Selection Box around needed image](guide/paint_selection_box.png)

And lastly press the Crop Tool.

![Paint Cropping Tool](guide/crop_tool.png)

After this has been done, simply Save the file (`Ctrl + S`) and repeat for the other images.

## Starting it

To start the script, simply run either of the `Bomber Royale Requeue` batch scripts. The Bot is being developped using Python 3.10 and uses a couple of Pip installed Libraries.

Assuming Python has been installed, and the Libraries have been too, the Script should work when started.

## It's not working for me, what do I do?

If the bot is not working, it can help to run it as Debug Mode. The bot will then inform you about what it is trying to do.

### Bot is not clicking at all

If the bot isn't clicking at all, and says it's attempting to find the images, it is likely unable to find them on the screen. This can be due to the Resolution being different, or some UI mods changing the buttons

To fix this, please follow the [guide](#changing-the-screenshots)

### Clicking the Wrong Place

This issue can occur when either the Screenshots aren't precise enough, or the Screen Offset hasn't been correctly set.

If the Cursor is clicking very differently from where it is supposed to, it is likely due to the Offset being off, to fix this, Run the bot again, and say "Yes" to setting the Offset

If the Cursor is clicking closely to the buttons, but just barely to the Top Left of them, it is likely the Screenshots used being a little off.

It is important, that the Screenshots Top-Left Corner is part of the button. To fix this, open up the screenshots and Crop it a little more, so the Top Left corner is part of the button
