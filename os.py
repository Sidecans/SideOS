import sys

sys.path.append("OS\\Drive\\SideOS")



import xml.etree.ElementTree as XML
import threading
import time
import os
import colorama
import keyboard
from bs4 import BeautifulSoup 

colorama.init()

GRAY = "\033[0;90m"
PINK = "\033[0;91m"
LIME = "\033[0;92m"
YELLOW = "\033[0;93m"
AQUA = "\033[0;94m"
MAGENTA = "\033[0;95m"
TEEL = "\033[0;96m"

BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
WHITE = "\033[0;37m"

keyboard.press('f11')

def boot():
    tree = XML.parse("OS\\Desktop\\Desktop.xml")
    root = tree.getroot()
    


def setup():
    print(AQUA + "Hello")
    time.sleep(1)
    os.system('cls')
    print("Welcome to your new SideOS" + WHITE)
    time.sleep(2)
    os.system('cls')
    
    





 

tree = XML.parse("OS\\Drive\\ProgramFiles\\Sidecans\\OS\\Data\\UserData.xml")
root = tree.getroot()

if root[0].text == "0":
    setup()
    with open("OS\\Drive\\ProgramFiles\\Sidecans\\OS\\Data\\UserData.xml", 'r') as f:
        data = f.read()
    bs_data = BeautifulSoup(data, 'xml')

while True:
    boot()


