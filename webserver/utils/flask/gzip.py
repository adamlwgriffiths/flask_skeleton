from __future__ import absolute_import
from contextlib import contextmanager
from flask import request
from cStringIO import StringIO as IO
import gzip
import functools


@contextmanager
def gzip_context():
    gzip_buffer = IO()
    gzip_file = gzip.GzipFile(mode='wb', fileobj=gzip_buffer)
    yield gzip_file, gzip_buffer
    gzip_file.close()


def gzip_data(data):
    with gzip_context() as (gz_f, gz_buffer):
        gz_f.write(data)
    return gz_buffer.getvalue()


def gzip_response(response):
    accept_encoding = request.headers.get('Accept-Encoding', '')

    if 'gzip' not in accept_encoding.lower():
        return response

    response.direct_passthrough = False

    if (
        response.status_code < 200 or
        300 <= response.status_code or
        'Content-Encoding' in response.headers
    ):
        return response

    response.data = gzip_data(response.data)
    response.headers['Content-Encoding'] = 'gzip'
    response.headers['Vary'] = 'Accept-Encoding'
    response.headers['Content-Length'] = len(response.data)

    return response


def gzipped(f):
    @functools.wraps(f)
    def view_func(*args, **kwargs):
        return gzip_response(f(*args, **kwargs))
    return view_func
