# ЗАДАНИЕ 1: Логирование вызова функции
# Напиши декоратор log, который:
# - печатает имя вызываемой функции и переданные ей аргументы,
# - затем вызывает оригинальную функцию,
# - после этого печатает возвращённый результат.
# Пример:
# >>> @log
# >>> def add(a, b): return a + b
# >>> add(2, 3)
# Вывод:
# Вызов: add(2, 3)
# Результат: 5

from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        arg = [str(a) for a in args]
        kwarg = [f"{k}={v}" for k, v in kwargs.items()]
        arg_kwarg = ", ".join(arg + kwarg)
        print(f"Вызов: {func.__name__}({arg_kwarg})")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result

    return wrapper
