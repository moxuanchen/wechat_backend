# -*- coding: utf-8 -*-

from wechat.app import create_app
from flask_script import Manager
from wechat.commands import CreateWeChatMenu


app = create_app()
manager = Manager(app)


if __name__ == "__main__":
    manager.add_command("create_wechat_menu", CreateWeChatMenu())
    manager.run()
