import sys
import threading
import tkinter
sys.path.append("OS\\Drive\\SideOS\\pkg")



import xml.etree.ElementTree as XML
from SidecanGPU import desktop
import time
import os
import colorama
import keyboard

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

#keyboard.press('f11')

def boot():
    desktop.run()
        


def setup():
    print(AQUA + "Hello")
    time.sleep(1)
    os.system('cls')
    print("Welcome to your new SideOS" + WHITE)
    time.sleep(2)
    os.system('cls')
    print("What would you like your Userna")
mainthread = threading.Thread(target=boot)
mainthread.start()
with open("OS\\Drive\\ProgramFiles\\Sidecans\\OS\\Reg\\setup.txt", 'r+') as f:

    if f.read() == "0":
       
        setup()
        with open("OS\\Drive\\ProgramFiles\\Sidecans\S\\Reg\\setup.txt", 'w') as g:
            g.write("1")

    


