#!/usr/bin/python3
import sys, os, shutil

DIRS = { 'Images' : ['png', 'jpg', 'jpeg', 'tiff', 'gif'],
         'Docs' : ['doc', 'docx', 'odt', 'txt', 'pdf'],
         'Tables' : ['xls', 'xlsx'],
         'Presentations' : ['ppt', 'pptx']}
LOCATION = '/home/zorell/python/python-academy/10. Importing/Exercises/FILES'
names = {'Images': 0, 'Docs': 0, 'Tables': 0, 'Presentations': 0}

def distribute(dir):
    for i in os.listdir(dir):
        for folder in DIRS:
            if os.path.splitext(i)[1].strip('.') in DIRS[folder]:
                source = os.path.join(dir,i)
                destination = os.path.join(LOCATION, folder)
                shutil.move(source, destination)
                names[folder] += 1
                continue

def print_report(data):
    max_width = len(max(data.keys(), key=len)) + 2
    print(max_width)
    print('MOVED')
    for i in data:
        print('{:{width}}{:<}'.format(i, data[i], width=max_width))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Wrong number of arguments')
        print('Argument expected format: distribute.py DIR_NAME')
    elif not os.path.exists(sys.argv[1]) and not os.path.isdir(sys.argv[1]):
            print('Folder {} does not exist'.format(sys.argv[1]))
            quit()
    else:
        dir = sys.argv[1]
        distribute(dir)
        print_report(names)
