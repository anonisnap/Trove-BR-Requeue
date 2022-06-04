@ECHO OFF

@ECHO == [31mTrove Bomber Royale Requeue[0m ==

@TYPE requeue_bot\disclaimer.txt

:dislaimer_notice
    set /P c="Are you sure you want to continue[Y/N]? "
    if /I "%c%" EQU "Y" goto :fix_offset
    if /I "%c%" EQU "N" goto :continue_no
    goto :fix_offset

:fix_offset
    @ECHO.
    @ECHO If you use Multiple Monitors, offset can be an issue for clicking
    set /P c="Do you wish to fix your Offset[Y/N]? "
    if /I "%c%" EQU "Y" goto :offset_yes
    if /I "%c%" EQU "N" goto :continue_yes

:continue_yes
    @ECHO Bot will turn on when you're ready. Please ensure Trove has been launched
    @PAUSE
    @ECHO [31mBot is turning on. Please tab into Trove within 5 seconds[0m
    @ECHO on
    @python requeue_bot/requeue.py True
    @pause
exit

:offset_yes
    @ECHO Please follow the instructions
    @python requeue_bot/OffsetFixer.py
goto :continue_yes

:continue_no
exit