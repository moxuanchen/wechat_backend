# -*- coding: utf-8 -*-

from flask import Flask
from api import api
from settings import get_config


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())
    app.register_blueprint(api)
    return app
