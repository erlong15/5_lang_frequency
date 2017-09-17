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
[lucky@lucky 5_lang_frequency]$ python3 lang_frequency.py  README.md 
[('в', 4), ('для', 3), ('org', 2), ('Как', 2), ('path_to_file', 1), ('3', 1), ('https', 1), ('анализатор', 1), ('Goals', 1), ('задача', 1)]
```

# Project Goals

тренировочная задача для проекта - [DEVMAN.org](https://devman.org)
