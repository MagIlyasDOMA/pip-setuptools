from setuptools import setup, find_packages

setup(
    name='pip-setuptools',
    version='1.0.1',
    author="Маг Ильяс DOMA (MagIlyasDOMA)",
    author_email='magilyas.doma.09@list.ru',
    url='https://github.com/MagIlyasDOMA/pip-setuptools',
    install_requires=[
        'setuptools>=75.8.0',
        'wheel>=0.45.1',
        'twine>=6.0.1'
    ],
    packages=find_packages(),
    license='MIT',
    description='setuptools-extensions for pip and wheel packages',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: 3 :: Only',
    ],
    entry_points={
        'console_scripts': [
            'package-compiler=pip_setuptools.package_compiler:main',
        ]
    }
)
