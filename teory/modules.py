import sys

sys.platform.startswith('win')
sys.argv - print(sys.argv) - print comand line arguments
sys.exit()  - exit the program


################################################################################
import os
os.listdir()
os.listdir('C:\\...')
os.getcwd()
os.mkdir()
os.makedirs('TestDir1/Inner1/InInner1')
os.listdir()
os.rename()  - rename and move directory and file

import shutil
shutil.copy(source,destination)
shutil.move(source,destination) move also subdirs

os.remove()  - remove file
os.rmdir()   - remove empty dir
shutil.rmtree('TestDir1')


>>> with open('TestDir/test.txt','w') as f:
...     f.write('This is a test file')


>>> items = ['C:', os.sep, 'User', 'PythonBeginner','Lesson8','test.txt']
>>> os.path.join(*items)
'C:\\User\\PythonBeginner\\Lesson8\\test.txt'

>>> os.path.dirname(path)
'/usr/PythonBeginner/Lesson8'

>>> os.path.basename(path)
'test.txt

>>> os.path.split(path)
('/usr/PythonBeginner/Lesson8', 'test.txt')

>>> os.path.splitext(path)
('/usr/PythonBeginner/Lesson8/test', '.txt')

os.path.exists(path) - returns True, if a given path exists in the file system:
os.path.isfile(path) - returns True, if a given path references a file
os.path.isdir(path) - - returns True, if a given path references a directory


>>> os.path.getsize('TestDir1/test.txt')
19

os.walk to iterate over all the directories and filenames under a given path.
 returns on each iteration a tuple (dirpath, dirnames, filenames)

os.system()

>>> os.get_terminal_size()
os.terminal_size(columns=80, lines=24)
>>> os.get_terminal_size().columns
80
>>> os.get_terminal_size().lines
24

################################################################################
