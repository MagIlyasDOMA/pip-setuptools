# `pip-setuptools` — документация
## Описание
`pip-setuptools` — это набор расширений и утилит для упрощения работы с `pip`, `setuptools`, `wheel` и `twine` 
при сборке, упаковке и публикации Python-пакетов. Пакет включает в себя:
- Автоматическую очистку временных файлов перед сборкой.
- Упрощённый интерфейс для настройки setup.py.
- Консольную утилиту для сборки дистрибутивов (sdist и wheel).
- Поддержку современных версий setuptools, wheel и twine.

---

## Установка
Установите пакет через `pip`:
```shell
pip install pip-setuptools
```

Или добавьте в `requirements.txt`:
```requirements
pip-setuptools>=1.1.5
```

---

## Использование
### 1. Создание `setup.py` с помощью `clean_and_setup`
Пример использования в `setup.py`:
```python
from pip_setuptools import clean_and_setup, requirements, readme

clean_and_setup(
    name='my-package',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='My awesome package',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/you/my-package',
    packages=['my_package'],
    install_requires=requirements(),
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
```

### 2. Ручной вызов очистки перед сборкой
```python
from pip_setuptools import clean

# Удаляет build, dist и *.egg-info
clean()

# Только удаляет build и *.egg-info (не трогает dist)
clean(dont_remove_dist=True)

# С задержкой после удаления
clean(pause=1.0)
```

### 3. Консольная утилита `package-compiler`
После установки пакета доступна команда:
```shell
package-compiler
```

#### Опции:
- `--no-sdist` или `-s` — не создавать source distribution.
- `--no-wheel` или `-w` — не создавать wheel.

#### Примеры:
```shell
# Создать и sdist, и wheel
package-compiler

# Только wheel
package-compiler --no-sdist

# Только sdist
package-compiler --no-wheel
```

---

## Функции и классы
### `clean(dont_remove_dist: bool = False, pause: float = 0.5) -> None`
Удаляет временные директории (`build`, `dist`, `*.egg-info`).
Вызывается автоматически в `clean_and_setup`, если в `sys.argv` есть `sdist` или `bdist*`.

### `requirements(filename: str = 'requirements.txt') -> list[str]`
Читает файл зависимостей и возвращает список строк.

### `readme(filename: str = 'README.md') -> str`
Читает README-файл и возвращает его содержимое.

### `clean_and_setup(**kwargs) -> Distribution`
Обёртка над `setuptools.setup`, которая автоматически вызывает clean() перед сборкой.
Принимает все те же аргументы, что и стандартный setup().

### `package_compiler.main()`
Точка входа для консольной утилиты `package-compiler`.

---

## Пример полного `setup.py`
```python
from pip_setuptools import clean_and_setup, requirements, readme

clean_and_setup(
    name='example-package',
    version='0.1.0',
    author='John Doe',
    author_email='john@example.com',
    description='A small example package',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/johndoe/example-package',
    packages=['example'],
    install_requires=requirements(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'example-cli=example.cli:main',
        ],
    },
)
```

---

## Требования
- `Python >= 3.6`
- `setuptools >= 75.8.0`
- `wheel >= 0.46.2`
- `twine >= 6.0.1`

---

## Лицензия
MIT License.
Автор: Маг Ильяс DOMA (MagIlyasDOMA)
GitHub: [MagIlyasDOMA/pip-setuptools](https://github.com/MagIlyasDOMA/pip-setuptools)

---

## Поддержка Python
Пакет поддерживает все версии Python от 3.6 до 3.14.

---

## Примечание
Этот пакет предназначен для разработчиков Python, которые хотят упростить процесс сборки и публикации своих пакетов. Он не заменяет `setuptools`, а расширяет его удобными утилитами.
