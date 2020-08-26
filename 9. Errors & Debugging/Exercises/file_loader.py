def file_loader(filepath):
    try:
        file = open(filepath)

    except FileNotFoundError:
        filename = filepath.split('\\')[-1]
        print('File {} does not exist.'.format(filename))

    else:
        content = file.read()
        file.close()
        return content


print(file_loader(input()))
#print(file_loader("names.txt"))
