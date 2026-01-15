import sys, os, shutil, time
from typing import Sequence, Mapping, Any
from setuptools import setup, find_packages, Extension, Distribution
from setuptools._distutils.cmd import Command

__version__ = '1.1.3'
__all__ = ['setup', 'find_packages', 'clean', '__version__', 'requirements', 'readme', 'clean_and_setup']


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


def requirements(filename: str = 'requirements.txt') -> list[str]:
    try:
        with open(filename, encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def readme(filename: str = 'README.md') -> str:
    try:
        with open(filename, encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return ''


def clean_and_setup(
    *,
    name: str = ...,
    version: str = ...,
    description: str = ...,
    long_description: str = ...,
    long_description_content_type: str = ...,
    author: str = ...,
    author_email: str = ...,
    maintainer: str = ...,
    maintainer_email: str = ...,
    url: str = ...,
    download_url: str = ...,
    packages: list[str] = ...,
    py_modules: list[str] = ...,
    scripts: list[str] = ...,
    ext_modules: Sequence[Extension] = ...,
    classifiers: list[str] = ...,
    distclass: type[Distribution] = ...,
    script_name: str = ...,
    script_args: list[str] = ...,
    options: Any = ...,
    license: str = ...,
    keywords: list[str] | str = ...,
    platforms: list[str] | str = ...,
    cmdclass: Mapping[str, type[Command]] = ...,
    data_files: list[tuple[str, list[str]]] = ...,
    package_dir: Mapping[str, str] = ...,
    obsoletes: list[str] = ...,
    provides: list[str] = ...,
    requires: list[str] = ...,
    command_packages: list[str] = ...,
    command_options: Mapping[str, Mapping[str, tuple]] = ...,
    package_data: Mapping[str, list[str]] = ...,
    include_package_data: bool = ...,
    libraries: list[str] = ...,
    headers: list[str] = ...,
    ext_package: str = ...,
    include_dirs: list[str] = ...,
    password: str = ...,
    fullname: str = ...,
    **attrs,
) -> Distribution:
    clean()
    return setup(
        name=name,
        version=version,
        author=author,
        author_email=author_email,
        maintainer=maintainer,
        maintainer_email=maintainer_email,
        url=url,
        download_url=download_url,
        description=description,
        long_description=long_description,
        long_description_content_type=long_description_content_type,
        classifiers=classifiers,
        keywords=keywords,
        platforms=platforms,
        cmdclass=cmdclass,
        data_files=data_files,
        package_dir=package_dir,
        obsoletes=obsoletes,
        provides=provides,
        requires=requires,
        packages=packages,
        py_modules=py_modules,
        ext_modules=ext_modules,
        scripts=scripts,
        distclass=distclass,
        script_name=script_name,
        script_args=script_args,
        options=options,
        license=license,
        command_packages=command_packages,
        package_data=package_data,
        include_package_data=include_package_data,
        include_dirs=include_dirs,
        command_options=command_options,
        libraries=libraries,
        headers=headers,
        ext_package=ext_package,
        password=password,
        fullname=fullname,
        **attrs
    )

