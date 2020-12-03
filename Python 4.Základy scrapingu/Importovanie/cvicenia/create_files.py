import os

def create_files(file_list, folder):
    for file in file_list:
        path = os.path.join(folder, file)
        f = open(path, 'w')
        f.close()

    dir_content = os.listdir(folder)
    for content in  dir_content:
        if not content in file_list:
            return False
        return True



print(create_files(['zoli', 'nigger', 'tongpo'],'files'))
