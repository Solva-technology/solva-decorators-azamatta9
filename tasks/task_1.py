from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v}" for k, v in kwargs.items()]
        arg_kwarg = ", ".join(args_repr + kwargs_repr)
        print(f"Вызов: {func.__name__}({arg_kwarg})")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result

    return wrapper
