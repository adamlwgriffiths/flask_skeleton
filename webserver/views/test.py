from __future__ import absolute_import, print_function
from flask import Blueprint, render_template
from ..models.test import User

blueprint = Blueprint('test', __name__)

@blueprint.route('/')
def index():
    return """Hello {}
        <a href="/template">Template Test</a>
        """.format(str(User.query.all()))


@blueprint.route('/template')
def template():
    return render_template('index.html')
