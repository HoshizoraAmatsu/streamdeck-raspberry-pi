from pynput.keyboard import Controller, Key
from subprocess import Popen
import time

keyboard = Controller()

keyboard.tap(Key.print_screen)

Popen(["C:\Windows\system32\mspaint.exe"])

time.sleep(1)

keyboard.press(Key.ctrl)

keyboard.tap('v')

keyboard.release(Key.ctrl)