import os
import sys
import time
import json
import requests
from urllib.request import urlopen
from time import sleep as s
Version = "0.0.1"

clear = lambda: os.system('cls')
clear()

LICNECE = """
Copyright © 2021 RageWire#0001

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
print(LICNECE)
agrue = input("do you agrue to the legal LICNECE [yes or no]: ")
if agrue == "yes":
    print("loading main progarm")
    s(1)
    clear()
elif agrue == "no":
    print("ending progarm due to saying no")
    s(1)
    clear()
    sys.exit()
else:
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
    if connected() == False:
        print(" Not Connected, please connect so it can use all modules")
        sys.exit()

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
autoupdate()


def discordSub():
    while True:
        print("\n")
        print("What type is your question?")
        print("\n")
        print("[1]:what is 1+1")
        print("[2]:Exit")
        print("\n")
        menu = int(input(": "))
        if menu == 1:
            print(1+1)
        elif menu == 2:
            break

def discordMenu():
    while True:
        clear()
        print("[1]:")
        print("\n")
        print("[2]:Exit")
        print("\n")
        menu = int(input(": "))
        if menu == 1:
            discordSub()
        elif menu == 2:
            break

while True:
    clear()
    print("Welcome,what would you like to do?type the number")
    print("\n")
    print("[1]:discord options")
    print("[2]:misc options")
    print("[3]:exit")
    menu = int(input(": "))
    if menu == 1:
        discordMenu()
    elif menu == 3:
        break
