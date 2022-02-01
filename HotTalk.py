####################################################################
# Created by Matthew Lopez - HotText App                           #
# HotText.py can only work if the PreText.py is in the same folder #
# Email: mattappleid793@gmail.com                                  #
####################################################################

import keyboard
from PreText import statements

while True:
    # 1 is the Ticket Starter.
    keyboard.add_hotkey('ctrl+alt+1', lambda: keyboard.write(statements['1']))

    # 2 is the send to App Support.
    keyboard.add_hotkey('ctrl+alt+2', lambda: keyboard.write(statements['2']))

    # 3 is the 3rd day reminder.
    keyboard.add_hotkey('ctrl+alt+3', lambda: keyboard.write(statements['3']))

    # 4 is the outage statement.
    keyboard.add_hotkey('ctrl+alt+4', lambda: keyboard.write(statements['4']))

    # 5 is the send to local I.T.
    keyboard.add_hotkey('ctrl+alt+5', lambda: keyboard.write(statements['5']))

    # 6 is the post Teams reply.
    keyboard.add_hotkey('ctrl+alt+6', lambda: keyboard.write(statements['6']))

    # 7 is just the signature.
    keyboard.add_hotkey('ctrl+alt+7', lambda: keyboard.write(statements['7']))


#########################################################
# Separator ----------------/---------------- Separator #                                               
#########################################################
    
    
    #Programs from HotKeys

    # Admin DiskClean.
    keyboard.add_hotkey('ctrl+shift+1', lambda: keyboard.write(statements['1p']))

    # Admin PowerShell.
    keyboard.add_hotkey('ctrl+shift+2', lambda: keyboard.write(statements['2p']))

    # App cashe location.
    keyboard.add_hotkey('ctrl+shift+3', lambda: keyboard.write(statements['3p']))

    keyboard.wait('Esc')
