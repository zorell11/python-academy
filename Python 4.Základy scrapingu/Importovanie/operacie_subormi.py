import os

os.chdir('C:\\Users\\zveres\\AppData\\Local\\Programs\\Python\\Python37')

#premnenovanie suboru
os.rename('test\\TestDir1\\tasks.txt', 'test\\TestDir1\\todo.txt')

# presunutine suboru
os.rename('test\\TestDir1\\config.txt', 'test\\TestDir2\\config.txt')

# presunut a premenovat subor
os.rename('test\\TestDir1\\test.txt', 'test\\TestDir3\\review.txt')
