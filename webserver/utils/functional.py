from __future__ import absolute_import
from copy import deepcopy

def dfilter(filter, d):
    '''Apply a filter to a dictionary
    '''
    f = filter
    if not f:
        f = lambda x: x is not None

    return {k: v for k, v in d.items() if f(v)}


def dmerge(a, b):
    '''Deep merge two dictionaries

    Doesn't modify the dictionaries
    '''
    d = deepcopy(a)
    for k, v in b.items():
        if isinstance(v, dict) and k in d:
            dmerge(d[k], v)
        else:
            d[k] = v
    return d


def pick(d, keys):
    '''Project a dictionary and only permit specific keys through.

    This is the opposite of omit.
    From javascript's lodash.
    '''
    return {k: v for k, v in d.items() if k in keys}


def omit(d, keys):
    '''Project a dictionary and drop specific keys through.

    This is the opposite of pick.
    From javascript's lodash.
    '''
    return {k: v for k, v in d.items() if k not in keys}
