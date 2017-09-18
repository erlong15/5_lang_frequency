# Частотный анализатор

скрипт используется для вывода первых 10 самых встречаемых слов в тексте. 


# Как использовать

Запускатьв консоли. Файл с текстом передается в качестве параметра. Вывод происходит в stdout. Можно подключать как библиотеку и передавать путь к файлу в функцию.


# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python3 lang_frequency.py  <path_to_file>
```

Пример подключения в качестве библиотеки
```

from lang_frequency import load_data, get_most_frequent_words

def example_of_use():
    words = load_data('test.txt')
    top_count = 2
    words = get_most_frequent_words(words, top_count)
```

# Пример работы

```bash
[lucky@lucky 5_lang_frequency]$ python3 lang_frequency.py README.md 
1: 6
в: 5
для: 4
как: 4
org: 3
3: 3
lang_frequency: 2
devman: 2
lucky: 2
https: 2

```

# Project Goals

тренировочная задача для проекта - [DEVMAN.org](https://devman.org)
