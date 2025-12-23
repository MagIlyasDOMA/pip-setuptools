import sys, os, shutil, time
from setuptools import setup, find_packages

__version__ = '1.0.3'
__all__ = ['setup', 'find_packages', 'clean', '__version__', 'requirements', 'readme']


def clean():
    if '--clean' in sys.argv:
        sys.argv.remove('--clean')
        # Удаляем build, dist и .egg-info директории
        dirs_to_remove = ['build', 'dist']
        # Добавляем .egg-info директории
        dirs_to_remove.extend([d for d in os.listdir('.')
                               if d.endswith('.egg-info')])

        for dir_name in dirs_to_remove:
            if os.path.exists(dir_name):
                shutil.rmtree(dir_name)
                print(f"Удалена директория {dir_name}")
        time.sleep(0.5)


def requirements(filename: str = 'requirements.txt'):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()


def readme(filename: str = 'README.md'):
    with open(filename, encoding='utf-8') as file:
        return file.read()

