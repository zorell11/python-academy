import os
dirs = ['DIR1', 'DIR2', 'DIR3']
path ='C:\\Users\\zveres\\Desktop\\docx\\learning\\python\\python-academy\\10. Importing\\Exercises\\DIR'
os.mkdir(path)
for i in dirs:
    os.mkdir(path + '\\' + i)

os.mkdir(path + '\\' + dirs[0] + '\\' + 'DIR1.1')
