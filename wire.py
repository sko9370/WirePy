#!/usr/bin/env/python3

# http://introtopython.org/terminal_apps.html#What-are-terminal-apps?
# much thanks to this guide for helping me build a terminal app

import os
from time import sleep

### Title Bar ###

def display_title():
    os.system('clear')

    print("\t****************WirePy****************")

### User Input ###

def get_user_input():
    print("\n")
    print("[1] see list of commands")
    print("[2] see the full man page for tshark")
    print("[q] quit")

    return input("well, what's your choice? ")

### Main Program ###

choice = ''
display_title()
while choice != 'q':

    choice = get_user_input()

    display_title()
    if choice == '1':
        print("\nyou chose 1!\n")
    elif choice == '2':
        print("\nyou chose 2!\n")
    elif choice == 'q':
        print("\nyou chose to quit\n")
    else:
        print("\nnot valid choice, try again\n")
