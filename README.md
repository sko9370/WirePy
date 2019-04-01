# WirePy

31 MAR

A terminal application built to simplify the use of tshark.
It will utilize basic python libraries to present an interactive experience so that users don't have to deal with finding the right tshark filter parameters.

This may limit some functionality of tshark, but this is not that much of a problem for basic users, especially for most of the common tasks.

A goal would be to somehow read in all possible filters or flags from a text file so that wire.py could correct user inputs that are wrong.

A particular function could guess at what the user is trying to do by trying to match user inputs with that list of possible filters/arguments by searching for words with the most letters alike.

Have to decide between using tcpdump or tshark as the packet capture app.

## SETUP

- pip3 install pyshark
- sudo apt install tshark
- sudo dpkg-reconfigure wireshark-common 
- sudo chmod +x /usr/bin/dumpcap
- sudo setcap cap_net_raw,cap_net_admin+eip /usr/sbin/tcpdump

