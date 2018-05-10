import traceback
from functools import partial

def eat_exception(fn, *args, **kwargs):
    print_exception = kwargs.get('_print_exception', False)
    if '_print_exception' in kwargs:
        del kwargs['_print_exception']

    try:
        return fn(*args, **kwargs)
    except Exception as e:
        if print_exception:
            print(traceback.format_exc())
        return e


# Decorator that prevents exceptions from propagating and will return ab Exception object on error
eat_print_exception = partial(eat_exception, _print_exception=True)
