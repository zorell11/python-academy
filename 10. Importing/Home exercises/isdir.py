import os

def which(path):

    if os.path.isdir(path):
        print('dir')

    elif os.path.isfile(path):
        print('file')


which(r'C:\Program Files')
which('/user/bin')
