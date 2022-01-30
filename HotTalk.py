import keyboard
from PreText import statements

while True:
    # 1 is the Ticket Starter.
    keyboard.add_hotkey('ctrl+1', lambda: keyboard.write(statements['1']))

    # 2 is the send to App Support.
    keyboard.add_hotkey('ctrl+2', lambda: keyboard.write(statements['2']))

    # 3 is the 3rd day reminder.
    keyboard.add_hotkey('ctrl+3', lambda: keyboard.write(statements['3']))

    # 4 is the outage statement.
    keyboard.add_hotkey('ctrl+4', lambda: keyboard.write(statements['4']))

    # 5 is the send to local I.T.
    keyboard.add_hotkey('ctrl+5', lambda: keyboard.write(statements['5']))

    #Programs from HotKeys

    # Admin DiskClean.
    keyboard.add_hotkey('ctrl+shift+1', lambda: keyboard.write(statements['1p']))

    # Admin PowerShell.
    keyboard.add_hotkey('ctrl+shift+2', lambda: keyboard.write(statements['2p']))

    keyboard.wait('Esc')
    