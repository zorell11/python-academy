import os, sys

def search(dir, name):
    if sys.platform == 'win32':
        delimeter = '\''
    else:
        delimeter = '/'

    for dirpath, dirnames, filenames in os.walk(dir):
        for i in dirnames:
            if name == i:
                print('DIR :', dirpath + delimeter + i)
        for j in filenames:
            if name in j:
                print('FILE :', dirpath + delimeter + j)


if __name__ == '__main__':
    try:
        dir, name = sys.argv[1:]
    except ValueError:
        print('Wrong number of arguments')
        print('Argument expected format: search.py START_FOLDER SEARCHED_NAME')
    else:
        search(dir, name)
