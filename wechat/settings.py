# -*- coding: utf-8 -*-

import os


class Config(object):

    WECHAT_TOKEN = "wx123cainiao456yefengkuang"
    APPID = "wx99389dce6ef8f80a"
    APPSECRET = "23f42951f6586b0fbdbbf5bffe437e85"


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    pass


def get_config(env='dev'):
    if os.environ.get("WECHAT_BACKEND_ENV") == "prod":
        return ProdConfig()
    else:
        return DevConfig()
