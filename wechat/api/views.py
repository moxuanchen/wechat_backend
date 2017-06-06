# -*- coding: utf-8 -*-

import hashlib
from flask import request
from flask import Blueprint
from flask import current_app
from wechat import WeChatHelper
from flask import render_template


api = Blueprint("api", __name__, template_folder="templates", static_folder="static")


def check_wechat_request():
    timestamp = request.args.get("timestamp", "")
    nonce = request.args.get("nonce", "")
    wechat_token = current_app.config['WECHAT_TOKEN']

    sig_list = [wechat_token, timestamp, nonce]
    print sig_list
    sig_list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, sig_list)

    digest = sha1.hexdigest()
    print digest
    if digest == request.args.get("signature", ""):
        return request.args.get("echostr", "")
    return "INVALID REQUEST"


@api.route("/", methods=['GET'])
def index():
    return "Wechat backend."


@api.route("/callback", methods=['GET', 'POST'])
def wechat_callback():
    if request.method == 'GET':
        return check_wechat_request()

    return WeChatHelper().receive_and_response(request)


@api.route("/enrol", methods=['GET', "POST"])
def user_enrol():
    if request.method == 'POST':
        pass
    return render_template("enrol.html")
