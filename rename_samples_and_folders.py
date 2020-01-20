from pathlib import Path

from utils import *


def fix_name(file):
    new_name = capitalize(replace_underscores(file.name))
    new_file = rename(file, new_name)
    return new_file


def rename_all_files_and_directories(root, indentation=0):
    directories = []
    print(root)
    for file in root.iterdir():
        if file.name == '.DS_Store':
            file.unlink()
            continue

        new_file = fix_name(file)
        if file != new_file:
            print(f'{"----" * indentation} {file.name} -> {new_file.name}')
        else:
            print(f'{"----" * indentation} {file.name}')

        if new_file.is_dir():
            directories.append(new_file)

    for directory in directories:
        rename_all_files_and_directories(directory, indentation + 1)


if __name__ == '__main__':
    root = Path('D:\\') / 'Musica' / 'Drive'
    if root.exists():
        print('Renaming all files and directories to replace undescores with spaces'
              'and to capitalize lowercase words...')
        rename_all_files_and_directories(root)
    else:
        print("The selected path doesn't exists({root}).".format(root=root))
