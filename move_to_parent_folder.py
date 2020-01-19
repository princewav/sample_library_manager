import os
import shutil
import stat
from shutil import move, rmtree
from pathlib import Path

excluded_extensions = ('.ini', '.txt', '.DS_Store', '.pdf', '.png', '.jpeg', '.jpg')


def clean_folders(root):
    for sub_folder in root.iterdir():
        if len(list(sub_folder.iterdir())) < 3:
            for file in sub_folder.iterdir():
                if any([file.name.endswith(ext) for ext in excluded_extensions]):
                    print(file, 'deleted')
                    file.unlink()
                elif file.name.strip() == 'MACOSX':
                    print(file, 'deleted')
                    rmtree(str(file))


def move_to_parent(root):
    for folder in root.iterdir():
        if len(list(folder.iterdir())) < 2:
            print('moving', folder)
            for sub_folder in folder.iterdir():
                for file in sub_folder.iterdir():
                    try:
                        move(str(file), str(folder / file.name))
                    except shutil.Error:
                        print(file, 'cartella duplicata')
                rmtree(str(sub_folder))


def delete_empty_subdirectories(root):
    for folder in root.iterdir():
        for subfolder in folder.iterdir():
            if subfolder.is_dir() and len(list(subfolder.iterdir())) == 0:
                try:
                    print('deleting empty folder', subfolder)
                    rmtree(str(subfolder))
                except PermissionError:
                    print(f'Error deleting {subfolder}, access_denied. Retrying with chmod.')
                    os.chmod(str(subfolder), stat.S_IWUSR)
                    rmtree(str(subfolder))


if __name__ == '__main__':
    root = Path('D:\\') / 'Musica' / 'Packki'

    clean_folders(root)
    move_to_parent(root)
    delete_empty_subdirectories(root)
