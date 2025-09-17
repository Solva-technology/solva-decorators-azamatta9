from collections import OrderedDict
from collections.abc import Hashable
from functools import partial, wraps


def simple_cache(func=None, *, max_size=128):
    if func is None:
        return partial(simple_cache, max_size=max_size)

    cache = OrderedDict()

    def make_hashable(obj):
        if isinstance(obj, Hashable):
            return obj
        if isinstance(obj, (list, tuple)):
            return tuple(make_hashable(item) for item in obj)
        if isinstance(obj, dict):
            return tuple(sorted((k, make_hashable(v)) for k, v in obj.items()))
        raise TypeError(f"Нехешируемый тип: {type(obj)}")

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            hashable_args = make_hashable(args)
            hashable_kwargs = make_hashable(kwargs)
            cache_key = (hashable_args, hashable_kwargs)
        except TypeError as e:
            print(f"Нехешируемый аргумент. {e}")
            return func(*args, **kwargs)

        if cache_key in cache:
            print("Из кэша")
            cache.move_to_end(cache_key)
            return cache[cache_key]
        else:
            if len(cache) >= max_size:
                oldest_key = next(iter(cache))
                del cache[oldest_key]

            result = func(*args, **kwargs)
            cache[cache_key] = result
            return result

    return wrapper
