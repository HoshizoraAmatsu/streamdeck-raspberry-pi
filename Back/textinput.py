import string
from pynput.keyboard import Controller
import sys
import time

keyboard = Controller()

textinput = sys.stdin.readline()

time.sleep(2)

keyboard.type(textinput)