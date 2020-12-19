import os

dir = 'C:\\Users\\zveres\\AppData\\Local\\Programs\\Python\\Python37'

def remdir(dir):
    files = os.listdir(dir)
    for i in files:
        os.remove((os.path.join(dir,i)))
    os.rmdir(dir)


remdir('C:\\Users\\zveres\\AppData\\Local\\Programs\\Python\\Python37\\test\\TestDir1')
