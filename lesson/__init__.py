# coding=utf-8

import os
from flask import Flask


def create_app():
    app = Flask(__name__)

    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    from . import lesson_url
    app.register_blueprint(lesson_url.bp)
    app.add_url_rule('/', endpoint='index')

    return app