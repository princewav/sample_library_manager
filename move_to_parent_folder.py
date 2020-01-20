import os
import shutil
import stat
from shutil import move, rmtree
from pathlib import Path

from utils import rename

excluded_extensions = ('.ini', '.txt', '.DS_Store', '.pdf', '.png', '.jpeg', '.jpg')
WRITE_PERMISSION = stat.S_IWUSR


def count_elements(directory):
    return len(list(directory.iterdir()))


def is_exluded_type(file):
    return any([file.name.endswith(ext) for ext in excluded_extensions])


def clean_folders(root):
    directories = []
    for file in root.iterdir():
        if is_exluded_type(file):
            print(file, 'deleted')
            file.unlink()
        elif file.name.strip(' _') == 'MACOSX':
            print(file, 'deleted')
            rmtree(str(file))

        if file.is_dir():
            directories.append(file)

    for directory in directories:
        clean_folders(directory)


def move_to_parent(root):
    if count_elements(root) == 1:
        folder = list(root.iterdir())[0]
        old_name = folder.name
        folder = rename(folder, 'ao')

        print(f'Moving all content of {old_name} in the parent folder')
        for element in folder.iterdir():
            element.replace(root / element.name)

        folder.chmod(WRITE_PERMISSION)
        folder.rmdir()
        move_to_parent(root)


if __name__ == '__main__':
    root = Path('D:\\') / 'Musica' / 'Packki'
    if root.exists():
        print('Cleaning all folders from unwanted files...')
        print('----------------------------------------------------------------------------')
        clean_folders(root)
        print()

        print('Moving the content of the top_level folders to remove not needed folders...')
        print('----------------------------------------------------------------------------')
        move_to_parent(root)
    else:
        print("The selected path doesn't exists({root}).".format(root=root))
