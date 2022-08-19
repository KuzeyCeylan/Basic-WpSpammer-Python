import os
#coded by kuzey ceylan.
import random
import pyautogui as pg
import time

class colors:
    PEMBE = '\033[95m'
    MAVI = '\033[94m'
    CAMGOBEGI = '\033[96m'
    YESIL = '\033[92m'
    SARI = '\033[93m'
    KIRMIZI = '\033[91m'
    DUZ = '\033[0m'
    KALIN = '\033[1m'
    ALTICIZILI = '\033[4m'


print(colors.KALIN)
print(colors.KIRMIZI + "Welcome To Wp Spammer.")
time.sleep(2)
if os.name == "nt":
    os.system("cls")

elif os.name == "posix":
    os.system("clear")

print(colors.CAMGOBEGI + "Importing Text Data...")
time.sleep(1)
txtfile = open("resource/data.txt", "r")

if os.name == "nt":
    os.system("cls")

elif os.name == "posix":
    os.system("clear")

print(colors.YESIL + "Imported Your Text Data.")
time.sleep(1)
print(colors.SARI + "[< CODE >] Spam Has Been Starting 5 Seconds Later.")
time.sleep(5)

for word in txtfile:
    pg.typewrite(word)
    pg.press("enter")
