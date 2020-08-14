import os

def create_dir(path_to_creation):
    os.mkdir(path_to_creation)

def read_file(path_to_files):
    with open(path_to_files) as file:
        content = file.read()
    lst = content.split('\n')
    return lst

        #parameter = (line.strip('\n')).split('=')
        #d1.update({ parameter[0] : parameter[1]})

def create_file(list_of_files, path_to_creation):
    for file in list_of_files:
        path = os.path.join(path_to_creation, file)
        with open(file, 'w'):
            pass


def main(path_to_creation, path_to_files):
    list_of_files = read_file(path_to_files)
    create_dir(path_to_creation)
    create_file(list_of_files, path_to_creation)

#create_dir()
if __name__ == '__main__':
    main('SEM','To_Be_Created.txt')
