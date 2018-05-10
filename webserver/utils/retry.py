from __future__ import absolute_import, print_function
import time
import logging
from functools import partial


def retry_fn(retries, sleep_increment, sleep_lambda, exceptions, fn, *args, **kwargs):
    '''Retry base function

    Not intended to be used directly, use the 'retry' function instead.
    '''
    for retry_count in range(1, retries + 1):
        try:
            return fn(*args, **kwargs)
        except exceptions as e:
            # call the sleep function
            sleep_lambda(sleep_increment, retry_count)
            print('{}: Retry {} - {}'.format(fn.__name__, retry_count, str(e)))
    print('{}: Too many retries - {}'.format(fn.__name__, str(e)))
    raise e


# sleep functions which alter the sleep delta for different purposes
constant_sleep = lambda sleep, count: time.sleep(sleep)
exponential_sleep = lambda sleep, count: time.sleep(sleep * count)

# implements the retry logic with a retry count of 3 and an exponential sleep
# of 1 second * retry count.
retry = partial(retry_fn, 3, 1.0, exponential_sleep, [StandardError])


def retriable(retries=3, sleep=1.0):
    '''Decorator which enables a function to be retried
    '''
    def outter(fn):
        def decorator(*args, **kwargs):
            return retry_fn(retries, sleep, exponential_sleep, fn, *args, **kwargs)
        return decorator
    return outter
