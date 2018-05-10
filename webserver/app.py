from __future__ import absolute_import, print_function
import os
import logging
from flask import Flask
from .database import register_database
from .commands import register_commands
from .views import register_blueprints
from .utils.flask.response import internal_error
from .utils.flask.logging import LoggingMiddleware, error_printer
from .utils.memoize import memoize
from .utils.string import string_to_bool
from .commands import register_commands

def create_app():
    return Flask(__name__)

def configure_app(app):
    # errors here indicate the environment is missing values
    app.debug = os.environ['ENVIRONMENT'] in ['testing']
    app.secret_key = os.environ['FLASK_APP_SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = string_to_bool(os.environ['SQLALCHEMY_TRACK_MODIFICATIONS'])
    return app

def setup_logging(app):
    if app.debug:
        # verbosely log all wsgi requests and responses
        #app.wsgi_app = LoggingMiddleware(app.wsgi_app)
        pass
    else:
        # log info to stdout
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)
    return app

def register_error_handlers(app):
    app.register_error_handler(500, error_printer)
    return app

@memoize
def app():
    _app = create_app()
    configure_app(_app)
    setup_logging(_app)
    register_error_handlers(_app)
    register_blueprints(_app)
    register_commands(_app)
    register_database(_app)
    return _app
