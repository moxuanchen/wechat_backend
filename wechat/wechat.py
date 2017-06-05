# -*- coding: utf-8 -*-

import requests
from flask import current_app


class WeChatBase(object):

    WX_TOKEN_API_URL = "https://api.weixin.qq.com/cgi-bin/token"


class WeChatHelper():

    def get_access_token(self):
        url = "{0}?grant_type=client_credential&appid={1}&secret={2}".format(
            self.WX_TOKEN_API_URL,
            current_app.config['APPID'],
            current_app.config['APPSECRET']
        )
        print url
        resp = requests.get(url).json()
        print resp

    def send_request(self, url, data):
        pass
