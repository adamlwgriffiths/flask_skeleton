from __future__ import absolute_import
from urllib import unquote
from flask import request, Response
from systemalib.utils import json


def json_response(response, **kwargs):
    kwargs['mimetype'] = kwargs.get('mimetype', None) or request.headers.get('Content-Type', 'application/json; charset=UTF-8')
    kwargs['response'] = json.dumps(response)
    return kwargs


def json_querystring(request):
    qs = request.query_string.split('&')
    uq = map(unquote, qs)
    kv = map(lambda s: s.split('='), uq)
    d = {k: v for k, v in kv}
    return d
    #return json.loads(unquote(request.query_string.partition('&')[0]))
