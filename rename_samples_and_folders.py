import os
import stat
from shutil import move, rmtree
from pathlib import Path

excluded_extensions = ('.ini', '.txt', '.DS_Store', '.pdf', '.png', '.jpeg', '.jpg')


def fix_name(file):
    new_name_list = file.name.replace('_', ' ').split(' ')
    result = []
    for word in new_name_list:
        if word.upper() == word:
            result.append(word)
        else:
            result.append(word.lower().capitalize())
    new_name = ' '.join(result)
    try:
        file.rename(file.parent / new_name)
    except Exception as e:
        print(e)


def rename_all_only_files(file):
    for file in root.iterdir():
        fix_name(file)


def rename_all(root):
    for file in root.iterdir():
        print(file)
        fix_name(file)
        if file.is_dir():
            rename_all(file)
            rename_all_only_files(file)


if __name__ == '__main__':
    # root = Path('D:\\') / 'Musica' / 'gdhfdfhdffhdhfdfhdhfdfhd' / 'Sample Packs'
    root = Path('D:\\') / 'Musica' / 'Packki'
    for i in range(1):
        rename_all(root)
