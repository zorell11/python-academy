import create_dir
import os, shutil

def created_folders(list_of_folders):
    list_of_folders = ['Images', 'Docs', 'Tables', 'Presentations']

    for folder in list_of_folders:
        path = os.path.join(folder_to_clean, folder)
        create_dir.create_dir(folder)


def main(folder_to_clean):
    created_folders(folder_to_clean)
