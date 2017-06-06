# -*- coding: utf-8 -*-

import os
import requests
from wechat.wechat import WeChatHelper
from flask_script import Command
from wechat.wechat import WeChatException


class CreateWeChatMenu(Command):
    """Create wechat menu"""

    menu_file = "../wechat_menu.json"
    create_menu_url_base = " https://api.weixin.qq.com/cgi-bin/menu/create?access_token={0}"

    def run(self):
        print "Create wechat menu..."
        menu_file_path = os.path.join(os.path.dirname(__file__), self.menu_file)

        with open(menu_file_path, "r") as fp:
            data = fp.read()
            access_token = WeChatHelper().get_access_token()
            create_menu_url = self.create_menu_url_base.format(access_token)
            resp = requests.post(create_menu_url, data=data).json()
            if resp['errcode'] != 0:
                raise WeChatException(resp['errmsg'])
            print "Create Wechat menu done..."
