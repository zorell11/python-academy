import os


def file_size(path):
    if not os.path.exists(path):
        print('Path does not exist.')
        return None

    if not os.path.isdir(path):
        print('{} is not a directory'.format(os.path.split(path)[1]))
        return None

    for i in os.listdir(path):
        print(i, os.path.getsize(os.path.join(path, i)))


path = 'C:\\Users\\zveres\\AppData\\Local\\Programs\\Python\\Python37\\test\\TestDir1\\'
file_size(path)
