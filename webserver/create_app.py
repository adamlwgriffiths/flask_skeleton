'''This file exists to enable uwsgi and flask to initialise the app using a method
They can only access variables, not call methods.
'''
from __future__ import absolute_import, print_function
from .app import app as create_app

app = create_app()
