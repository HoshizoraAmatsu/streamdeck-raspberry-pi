from subprocess import Popen
import sys

app_location = input(sys.stdin.readline())

Popen([app_location])

