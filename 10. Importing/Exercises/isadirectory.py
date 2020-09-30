import os

PATH = '/home/zorell/python/python-academy/10. Importing/Exercises/test/py'

def which(path):
    if os.path.isfile(path):
        return 'file'
    elif os.path.isdir(path):
        return 'dir'
    #elif not os.path.exists(path):
    #        return None

print(which(PATH))
