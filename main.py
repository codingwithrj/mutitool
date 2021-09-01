import os
import sys
import time
import json
import requests
from urllib.request import urlopen
from time import sleep as s
Version = "0.0.1"

clear = lambda: os.system('cls')

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
			time.sleep(2)
			if Version in test.text:
				print(" You Are Using PhishMailer v.{}, you are upto date!".format(Version))
				time.sleep(2)
				clear()
			else:
				print(" Looks Like You Are Using Phishmailer v.{}, There Is A Newer Version Out, Please Update Repo!".format(Version))
				print("https://github.com/BiZken/PhishMailer.git")
				sys.exit()
		else:
			pass
pre()
autoupdate()
s(2)


def math_menu2():
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

def math_menu():
    while True:
        print("\n")
        print("What type is your question?")
        print("\n")
        print("[1]:some simple math")
        print("[2]:Exit")
        print("\n")
        menu = int(input(": "))
        if menu == 1:
            math_menu2()
        elif menu == 2:
            break

while True:
    print("\n")
    print("Welcome,what would you like to do?type the number")
    print("\n")
    print("[1]:Math solver")
    print("[2]:exit")
    print("\n")
    menu = int(input(": "))
    if menu == 1:
        math_menu()
    elif menu == 2:
        break
