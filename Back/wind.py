from distutils import cmd
from this import d
from pynput.keyboard import Controller, Key

keyboard = Controller()

keyboard.press(Key.cmd)

keyboard.tap('d')

keyboard.release(Key.cmd)