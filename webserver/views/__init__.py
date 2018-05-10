from __future__ import absolute_import, print_function
from . import test

def register_blueprints(app):
    app.register_blueprint(test.blueprint)
    return app
