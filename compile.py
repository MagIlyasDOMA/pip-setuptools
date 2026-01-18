import os, shutil, time


def clean() -> None:
    # Удаляем build, dist и .egg-info директории
    dirs_to_remove = ['build', 'dist']

    dirs_to_remove.extend([d for d in os.listdir('.')
                           if d.endswith('.egg-info')])

    for dir_name in dirs_to_remove:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"Удалена директория {dir_name}")
    time.sleep(0.5)


clean()
os.system('python setup.py sdist bdist_wheel')
