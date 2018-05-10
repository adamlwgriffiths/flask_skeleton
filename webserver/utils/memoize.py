from __future__ import absolute_import
from functools import wraps
from .time import now_milliseconds


def memoize(fn):
    fn._cache = {}

    @wraps(fn)
    def inner(*args, **kwargs):
        cache = fn._cache
        key = str(args) + str(kwargs)
        if key in cache:
            result = cache[key]
        else:
            result = fn(*args, **kwargs)
            cache[key] = result
        return result
    return inner


def timed_memoize(cache_time):
    def outter(fn):
        fn._cache = {}

        @wraps(fn)
        def inner(*args, **kwargs):
            cache = fn._cache
            key = str(args) + str(kwargs)
            # check if the cache has expired
            # if so, delete the cache
            if key in cache:
                result, time = cache[key]
                if (time + cache_time) > now_milliseconds():
                    return result

            # check if the key is in the cache
            # if not, get the value and store it again
            result = fn(*args, **kwargs)
            time = now_milliseconds()
            cache[key] = (result, time)
            return result
        return inner
    return outter


def clear_memoize_cache(fn):
    fn._cache.clear()
