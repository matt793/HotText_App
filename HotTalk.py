import keyboard
from PreText import statements

while True:
    keyboard.add_hotkey('1+.', lambda: keyboard.write(statements['1']))

    keyboard.add_hotkey('2+.', lambda: keyboard.write(statements['2']))

    keyboard.add_hotkey('3+.', lambda: keyboard.write(statements['3']))

    keyboard.wait('Esc')
    