import keyboard
from PreText import statements

while True:
    keyboard.add_hotkey('ctrl+1', lambda: keyboard.write(statements['1']))

    keyboard.add_hotkey('ctrl+2', lambda: keyboard.write(statements['2']))

    keyboard.add_hotkey('ctrl+3', lambda: keyboard.write(statements['3']))

    keyboard.add_hotkey('ctrl+4', lambda: keyboard.write(statements['4']))

    keyboard.add_hotkey('ctrl+5', lambda: keyboard.write(statements['5']))

    keyboard.wait('Esc')
    