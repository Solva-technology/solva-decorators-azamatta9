# ЗАДАНИЕ 2: Кэширование результатов
# Напиши декоратор simple_cache, который:
# - запоминает результат функции при вызове с конкретными аргументами,
# - при повторном вызове с теми же аргументами — возвращает сохранённый
# - печатает "Из кэша" при использовании кэшированного значения.
# Подсказка: используй словарь для хранения результатов.

from functools import wraps


def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in cache:
            print("Из кэша")
            return cache[cache_key]
        else:
            result = func(*args, **kwargs)
            cache[cache_key] = result
            return result

    return wrapper
