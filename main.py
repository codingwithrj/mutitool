import os
import sys
import time
import json
import requests
from urllib.request import urlopen
from time import sleep as s


from plugins.discord.discordgen import *

Version = "0.0.1"

clear = lambda: os.system('cls')
clear()

LICNECE = """
Copyright © 2021 RageWire#0001

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
ctypes.windll.kernel32.SetConsoleTitleW("mutitool accept LICNECE - Made by RageWire#0001")
print(LICNECE)
agrue = input("do you agrue to the legal LICNECE [yes or no]: ")
if agrue == "yes":
    ctypes.windll.kernel32.SetConsoleTitleW("mutitool LOADING PROGARM - Made by RageWire#0001")
    print("loading main progarm")
    s(1)
    clear()
elif agrue == "no":
    print("ending progarm due to saying no")
    ctypes.windll.kernel32.SetConsoleTitleW("mutitool ENDING PROGARM - Made by RageWire#0001")
    s(1)
    clear()
    sys.exit()
else:
    ctypes.windll.kernel32.SetConsoleTitleW("mutitool pick yes or no - Made by RageWire#0001")
    print("please pick yes or no")
    print("restart the progarm")
    s(1)
    sys.exit()
def connected(host='http://duckduckgo.com'):
    try:
        urlopen(host)
        return True
    except:
        return False

def pre():
    ctypes.windll.kernel32.SetConsoleTitleW("mutitool checking wifi - Made by RageWire#0001")
    if connected() == False:
        print(" Not Connected, please connect so it can use all modules")
        sys.exit()

def modules():
    ctypes.windll.kernel32.SetConsoleTitleW("mutitool checking modules - Made by RageWire#0001")
    clear()
    try: # Check if the requrements have been installed
        from discord_webhook import DiscordWebhook # Try to import discord_webhook
    except ImportError: # If it chould not be installed
        input(f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nPress enter to exit") # Tell the user it has not been installed and how to install it
        exit() # Exit the program
    try: # Setup try statement to catch the error
        import requests # Try to import requests
    except ImportError: # If it has not been installed
        input(f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")# Tell the user it has not been installed and how to install it
        exit() #

def autoupdate():

		with open('config.json') as json_file:
			data = json.load(json_file)
		if data['check-for-updates'] == "yes":
			print(" Checking for updates...")
			test = requests.get("https://raw.githubusercontent.com/codingwithrj/mutitool/master/version.dat")
			s(2)
			if Version in test.text:
				print(" You Are Using mutitool v.{}, you are upto date!".format(Version))
				s(2)
				clear()
			else:
				print(" Looks Like You Are Using mutiltool v.{}, There Is A Newer Version Out, Please Update Repo!".format(Version))
				print("https://github.com/codingwithrj/mutitool")
				sys.exit()
		else:
			pass
pre()
ctypes.windll.kernel32.SetConsoleTitleW("mutitool checking version - Made by RageWire#0001")
autoupdate()
modules()

try:
    def discordSub():
        while True:
            ctypes.windll.kernel32.SetConsoleTitleW("mutitool discord sub menu - Made by RageWire#0001")
            clear()
            print("discord gens")
            print("[1]:discord nitro gen and check (most likly not going to work)")
            print("[2]:Exit")
            print("\n")
            menu = int(input(": "))
            if menu == 1:
                Gen = NitroGen() # Create the nitro generator object
                Gen.main()
            elif menu == 2:
                break

    def discordMenu():
        while True:
            ctypes.windll.kernel32.SetConsoleTitleW("mutitool discord menu - Made by RageWire#0001")
            clear()
            print("[1]:discord gens")
            print("[2]:Exit")
            print("\n")
            menu = int(input(": "))
            if menu == 1:
                discordSub()
            elif menu == 2:
                break

    def miscdMenu():
        while True:
            ctypes.windll.kernel32.SetConsoleTitleW("mutitool misc menu - Made by RageWire#0001")
            clear()
            print("[1]:textholder")
            print("[2]:Exit")
            print("\n")
            menu = int(input(": "))
            if menu == 1:
                pass
            elif menu == 2:
                break

    while True:
        ctypes.windll.kernel32.SetConsoleTitleW("mutitool main menu - Made by RageWire#0001")
        clear()
        print("Welcome,what would you like to do? type the number")
        print("[1]:discord options")
        print("[2]:misc options")
        print("[3]:exit")
        print("\n")
        menu = int(input(": "))
        if menu == 1:
            discordMenu()
        elif menu == 2:
            miscdMenu()
        elif menu == 3:
            clear()
            ctypes.windll.kernel32.SetConsoleTitleW("mutitool good bye - Made by RageWire#0001")
            print("good bye")
            s(1)
            break
except KeyboardInterrupt:
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("mutitool good bye - Made by RageWire#0001")
    print("good bye user")
    s(1)
    sys.exit()
