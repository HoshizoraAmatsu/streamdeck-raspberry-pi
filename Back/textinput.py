import string
from pynput.keyboard import Controller
import sys

keyboard = Controller()

textinput = sys.stdin.readline()

keyboard.type(textinput)