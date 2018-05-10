from __future__ import absolute_import, print_function
import sys
import logging
try:
    import cStringIO as StringIO
except:
    from io import StringIO
import flask
from flask import Response
from .cors import cors_headers


class LoggingMiddleware(object):
    def __init__(self, app):
        self._app = app

    def __call__(self, env, resp):
        errorlog = sys.stdout

        i = env['wsgi.input'].read()
        env['POST_DATA'] = i
        env['wsgi.input'] = StringIO.StringIO(i)

        def encode(u):
            if isinstance(u, basestring):
                return u.encode('ascii', 'backslashreplace')
            return u

        def log_response(status, headers, *args):
            try:
                # remove any header key containing 'wsgi' or 'werkzeug'
                restricted_headers = ['wsgi', 'werkzeug']
                filtered_env = {
                    encode(k): encode(v)
                    for k, v in env.items() if not any(map(lambda key: key in k, restricted_headers))
                }
                print >> errorlog, [
                    {'RESPONSE': filtered_env, 'STATUS': status},
                    {'RESPONSE': headers, 'STATUS': status}
                ]
            except:
                # don't crash the app if we cannot log the request
                print >> errorlog, ["Error logging request", traceback.format_exc()]
            return resp(status, headers, *args)

        return self._app(env, log_response)


def error_printer(exception):
    flask.current_app.logger.error(exception)
    print(exception)
    # add cors so that errors don't cause javascript to fail
    # since any non-cors'ed response will break javascript
    # because cors exceptions are not catchable in javascript
    return cors_headers(Response(response='An error occurred', status=500))
