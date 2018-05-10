from __future__ import absolute_import, print_function

def string_to_bool(s):
    return {
        '1': True,
        'true': True,
        'yes': True,
        '0': False,
        'false': False,
        'no': False,
    }.get(s.lower(), None)
