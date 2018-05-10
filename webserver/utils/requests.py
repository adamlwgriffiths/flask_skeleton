from __future__ import absolute_import
import requests
from systemalib.utils.functional import dmerge
from systemalib.utils import json


def response_status(response):
    return response.status_code


def response_json(response):
    return json.loads(response.content)


def response_header(key, response):
    return response.headers[key]


def json_data(data, **kwargs):
    return dmerge(kwargs, {
        'data': json.dumps(data) if data else None,
        'headers': {'content-type': 'application/json'}
    })

def headers(data, **kwargs):
    return dmerge(kwargs, {
        'headers': data,
    })

def raise_status(response):
    response.raise_for_status()
    return response

def request(verb, url, **kwargs):
    method = getattr(requests, verb.lower())
    response = method(url, **kwargs)
    return response
