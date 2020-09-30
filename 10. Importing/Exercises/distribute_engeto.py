import shutil, sys, os

names = {'Images': 0, 'Docs': 0, 'Tables': 0, 'Presentations': 0}
types = {
    'png': 'Images',
    'jpg': 'Images',
    'jpeg': 'Images',
    'tiff': 'Images',
    'gif': 'Images',
    'doc': 'Docs',
    'docx': 'Docs',
    'odt': 'Docs',
    'txt': 'Docs',
    'pdf': 'Docs',
    'xls': 'Tables',
    'xlsx': 'Tables',
    'ppt': 'Presentations',
    'pptx': 'Presentations'
}


def make_dirs(folder):
    # iterate over names in the names variable and
    # create new directory for it if it does not exist already
    for name in names:
        try:
            path = os.path.join(folder, name)
            os.mkdir(path)
        except FileExistsError:
            pass


def move_files(folder):
    # iterate over items in given directory
    for item in os.listdir(folder):
        try:
            # check whether the currently iterated item is a file
            src = os.path.join(folder, item)
            if os.path.isfile(src):
                # if yes acquire its file type and move it to
                # the corresponding folder
                file_type = os.path.splitext(item)[-1].lstrip('.')
                destination = os.path.join(folder, types[file_type])

                shutil.move(src, destination)
                # increase the counter of movements for a given folder
                # into which the file has been moved
                names[types[file_type]] += 1
        except KeyError:
            pass


def print_report(data):
    # print the brief report on how many items were MOVED
    # into each folder

    print('\nMOVED\n' + '=' * 15)
    max_width = len(max(data.keys(), key=len)) + 2

    for name in names:
        print('{:{width}}{:<}'.format(name,
                                      names[name],
                                      width=max_width))


if __name__ == '__main__':

    # check number of arguments
    if len(sys.argv) != 2:
        print('\nUSAGE: distribute.py path_to_dir\n')
    elif not os.path.exists(sys.argv[1]):
        print('\nFolder {} does not exist\n'.format(sys.argv[1]))
    else:
        folder = sys.argv[1]
        make_dirs(folder)
        move_files(folder)
        print_report(names)
