import os, shutil, time


def clean(dont_remove_dist: bool = False) -> None:
    # Удаляем build, dist и .egg-info директории
    dirs_to_remove = ['build']

    if not dont_remove_dist:
        dirs_to_remove.append('dist')

    dirs_to_remove.extend([d for d in os.listdir('.')
                           if d.endswith('.egg-info')])

    for dir_name in dirs_to_remove:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"Удалена директория {dir_name}")
    time.sleep(0.5)


os.system('python setup.py sdist bdist_wheel')
