import os

path ='C:\\Users\\zveres\\Desktop\\docx\\learning\\python\\python-academy\\10. Importing\\Exercises\\DIR\\'

all_content = []
while True:
    actual_content = os.listdir(path)
    all_content += actual_content
    for i in actual_content:
        if os.path.isdir(i):
            path = ''.join([path, i])
