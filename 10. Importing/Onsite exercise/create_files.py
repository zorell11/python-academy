import os
dir1 = 'TestDir1'
dir2 = 'TestDir2'

os.mkdir(os.path.join('C:\\Users\\SOE-Load\\Desktop\\Test\\', dir1))
os.mkdir(os.path.join('C:\\Users\\SOE-Load\\Desktop\\Test\\', dir2))


os.listdir(os.getcwd())

vytvorit subor:
file = open('test1.txt', 'w')
with open('test2.txt', 'w') as file:
    pass
