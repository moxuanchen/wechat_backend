# -*- coding: utf-8 -*-

import os


class Config(object):

    WECHAT_TOKEN = "wx123cainiao456yefengkuang"


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    pass


def get_config(env='dev'):
    if os.environ.get("WECHAT_BACKEND_ENV") == "prod":
        return ProdConfig()
    else:
        return DevConfig()
