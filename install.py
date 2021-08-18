#!/usr/bin/env python3

from os import system
from getpass import getuser

if getuser() != "root":
    print("ERROR: You must run this as root!")
    exit()

system("chmod +x fetchfetch")
system("cp fetchfetch /usr/bin/")

print("FetchFetch Sucesfully installed!")

# yes i know this is useless but i do not care
