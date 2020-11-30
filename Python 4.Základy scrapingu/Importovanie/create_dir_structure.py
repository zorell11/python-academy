import os

dir = 'C:\\Users\\zveres\\AppData\\Local\\Programs\\Python\\Python37'
os.chdir(dir)
os.mkdir('test')

for i in range(1,4):
    os.mkdir('test\\TestDir' + str(i))

for i in ['config.txt', 'tasks.txt', 'test.txt']:
    f = open('test\\TestDir1\\' + i, 'w')
    f.close()
