####################################################################
# Created by Matthew Lopez - HotText App                           #
# HotText.py can only work if the PreText.py is in the same folder #
# Email: mattappleid793@gmail.com                                  #
####################################################################

# Automates hotkeys
import keyboard

# Imports the python dictonary file for all the statments and commands
from PreText import statements

# Adds ability to import a non-python file
import os
 
# Imports local password file. User must make '.hide1' file.
file_path = ".hide1"
 
# Check if file is present
if os.path.isfile(file_path):
    
    # Open text file in read mode
    text_file = open(file_path, "r")
 
    # Read whole file to a string
    data = text_file.read()
 
    # Close file
    text_file.close()

# Imports local password file. User must make '.hide2' file.
file_path = ".hide2"
 
# Check if file is present
if os.path.isfile(file_path):
    
    # Open text file in read mode
    text_file = open(file_path, "r")
 
    # Read whole file to a string
    data = text_file.read()
 
    # Close file
    text_file.close()

# loops the listener
while True:

    # Run statements from HotKeys

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
    
     # 8 Duo reactivation link.
    keyboard.add_hotkey('ctrl+alt+8', lambda: keyboard.write(statements['8']))


#########################################################
# Separator ----------------/---------------- Separator #                                               
#########################################################
    
    
    # Run programs from HotKeys

    # Admin DiskClean.
    keyboard.add_hotkey('ctrl+shift+1', lambda: keyboard.write(statements['1p']))

    # Admin PowerShell.
    keyboard.add_hotkey('ctrl+shift+2', lambda: keyboard.write(statements['2p']))

    # App cashe location.
    keyboard.add_hotkey('ctrl+shift+3', lambda: keyboard.write(statements['3p']))

    # Adds password to hotkey
    keyboard.add_hotkey('ctrl+shift+4', lambda: keyboard.write(data))
    
    # Must have code line to make listener work.
    keyboard.wait('Esc')