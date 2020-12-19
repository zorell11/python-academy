import os
import sys

def which(path):
    if os.path.isdir(path):
        return 'dir'
    elif os.path.isfile(path):
        return 'file'
    elif not os.path.exists(path):
        return 'PathNotValid'


print(which(sys.argv[1]))
