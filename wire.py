#!/usr/bin/env/python3

# http://introtopython.org/terminal_apps.html#What-are-terminal-apps?
# much thanks to this guide for helping me build a terminal app

import os
from time import sleep
from subprocess import Popen, PIPE
import pyshark

### Title Bar ###

def display_title():
    os.system('clear')

    print("\t****************WirePy****************")

### User Input ###

def get_pcap_name():
    pcapName = input("pcap file name? ")

    return pcapName

def get_user_input():
    print("\n")
    print("[1] see everything")
    print("[2] choose a filter")
    print("[3] examine a packet in detail")
    print("[q] quit")
    print("\n")

    return input("well, what's your choice? ")

### Main Program ###

choice = ''
display_title()
pcapName = get_pcap_name()

while choice != 'q':

    choice = get_user_input()

    display_title()

    if choice == '1':
        # https://www.saltycrane.com/blog/2008/09/how-get-stdout-and-stderr-using-python
        # -subprocess-module/

        print("\nyou chose 1!\n")
        pcap = pyshark.FileCapture(pcapName, only_summaries=True)
        for packet in pcap:
            print(packet)

    elif choice == '2':
        print("\nyou chose 2!\n")
        validFilters = []
        filters = input("filters here (like 'http and ip.addr==10.10.4.251') ")
        pcap = pyshark.FileCapture(pcapName, display_filter=filters, only_summaries=True)
        for packet in pcap:
            print(packet)

    elif choice == '3':
        print("\nyou chose 3!\n")
        packetNumber = input("packet number: ")
        pcap = pyshark.FileCapture(pcapName)
        print(pcap[int(packetNumber)])

    elif choice == 'q':
        print("\nyou chose to quit\n")
    else:
        print("\nnot valid choice, try again\n")
