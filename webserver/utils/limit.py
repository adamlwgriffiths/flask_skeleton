from __future__ import absolute_import, print_function
import datetime
from systemalib.utils.retry import retry_fn, exponential_sleep


def _rate_limit(_data, fn, *args, **kwargs):
    '''Provides rate limiting logic, but permits shared rate limiting values.

    Pass in a dictionary as the first arguement with a value for the 'per_second' key.

    Example usage::

        from functools import partial
        rate_limit = partial(_rate_limit, _data={'per_second': 2})
        rate_limit(my_func, a, b)
        rate_limit(my_other_func, b, c)

    '''
    delay = 1.0 / float(_data.get('per_second'))
    if not _data.get('last_call'):
        _data['last_call'] = datetime.datetime.now() - datetime.timedelta(seconds=delay)
    retries = _data.get('retries', 3)

    def func(*args, **kwargs):
        _data['last_call'] = datetime.datetime.now()
        return fn(*args, **kwargs)

    retry_fn(retries, 2.0, exponential_sleep, func, *args, **kwargs)

    for retry_count in range(1, retries + 1):
        try:
            _data['last_call'] = datetime.datetime.now()
            return fn(*args, **kwargs)
        except Exception as e:
            time.sleep(delay)

            print('{}: Retry {} - {}'.format(fn.__name__, retry_count, str(e)))
            # double the wait time
            delay *= 2.0
    print('{}: Too many retries - {}'.format(fn.__name__, str(e)))
    raise e
