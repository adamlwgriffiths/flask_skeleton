from __future__ import absolute_import
from flask import Response


def ok(*args, **kwargs):
    kwargs['status'] = 200
    return Response(*args, **kwargs)

def bad_request(*args, **kwargs):
    kwargs['status'] = 400
    return Response(*args, **kwargs)

def unauthenticated(*args, **kwargs):
    kwargs['status'] = 401
    return Response(*args, **kwargs)

def unauthorised(*args, **kwargs):
    kwargs['status'] = 403
    return Response(*args, **kwargs)

def not_found(*args, **kwargs):
    kwargs['status'] = 404
    return Response(*args, **kwargs)

def not_acceptable(*args, **kwargs):
    kwargs['status'] = 406
    return Response(*args, **kwargs)

def conflict(*args, **kwargs):
    kwargs['status'] = 409
    return Response(*args, **kwargs)

def unprocessable(*args, **kwargs):
    kwargs['status'] = 422
    return Response(*args, **kwargs)

def unsatisfied_dependency(*args, **kwargs):
    kwargs['status'] = 424
    return Response(*args, **kwargs)

def internal_error(*args, **kwargs):
    kwargs['status'] = 500
    return Response(*args, **kwargs)

def not_implemented(*args, **kwargs):
    kwargs['status'] = 501
    return Response(*args, **kwargs)
