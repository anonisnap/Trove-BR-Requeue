type info.txt

@ECHO OFF

:choice
    set /P c="Are you sure you want to continue[Y/N]?"
    if /I "%c%" EQU "Y" goto :continue_yes
    if /I "%c%" EQU "N" goto :continue_no
    goto :choice


:continue_yes
    @ECHO "Bot is turning on. Please ensure Trove is opened within 5 seconds"
    @ECHO on
    python requeue.py True
exit

:continue_no
exit