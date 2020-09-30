import sys

a = 1
try:
    sys.exit()
except SystemExit:
    inpt = input('Do you really want to exit the program? y/n ')
    if inpt == 'y': raise
