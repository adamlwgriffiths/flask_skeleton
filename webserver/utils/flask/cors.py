from __future__ import absolute_import
from flask import request

CORS_MAX_AGE = 31556926

def cors_headers(response, origin=None, methods=None, max_age=CORS_MAX_AGE):
    origin = origin or request.headers.get('Origin')
    # jQuery 1.5.1 requires x-requested-with
    headers = {
        'Access-Control-Allow-Origin': origin,
        'Access-Control-Allow-Headers': 'Accept, Origin, Content-Type, x-requested-with',
    }
    if methods:
        headers['Access-Control-Allow-Methods'] = ','.join(methods)

    if max_age is not None:
        headers['Access-Control-Max-Age'] = str(max_age)

    for k, v in headers.items():
        response.headers.add(k, str(v))

    return response

def cors(methods=None, max_age=CORS_MAX_AGE):
    def outter(f):
        @functools.wraps(f)
        def view_func(*args, **kwargs):
            return cors_headers(f(*args, **kwargs), methods=methods, max_age=max_age)
        return view_func
    return outter
