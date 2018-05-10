'''File is here to avoid circular imports (app/db -> model -> app/db)
'''
from __future__ import absolute_import, print_function
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def register_database(app):
    db.init_app(app)
    return app
