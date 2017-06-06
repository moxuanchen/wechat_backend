# -*- coding: utf-8 -*-

import time
import requests
from flask import current_app
import xml.etree.ElementTree as ET


class WeChatException(Exception):
    pass


class WeChatBase(object):

    WX_TOKEN_API_URL = "https://api.weixin.qq.com/cgi-bin/token"


class Msg(object):
    pass


class TextMsg(Msg):
    def __init__(self, toUser, fromUser, content):
        self.__dict = dict()
        self.__dict["ToUserName"] = toUser
        self.__dict["FromUserName"] = fromUser
        self.__dict["CreateTime"] = int(time.time())
        self.__dict["Content"] = content

    def send(self):
	XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """

        return XmlForm.format(**self.__dict)

class WeChatHelper(WeChatBase):

    def get_access_token(self):
        url = "{0}?grant_type=client_credential&appid={1}&secret={2}".format(
            self.WX_TOKEN_API_URL,
            current_app.config['APPID'],
            current_app.config['APPSECRET']
        )
        resp = requests.get(url).json()
        if "errcode" in resp.keys():
            raise WeChatException(resp['errmsg'])
        return resp['access_token']

    def receive_text_msg_and_response(self, xmldata):
        fromUser = xmldata.find("FromUserName").text
        toUser = xmldata.find("ToUserName").text
        content = xmldata.find("Content").text
        print "Receive Text Msg: %s" % content
        return TextMsg(fromUser, toUser, "Hello, How are you ?").send()

    def receive_image_msg_and_response(self, xmldata):
        pass

    def receive_voice_msg_and_response(self, xmldata):
        pass

    def receive_video_msg_and_response(self, xmldata):
        pass

    def receive_shortvideo_msg_and_response(self, xmldata):
        pass

    def receive_location_msg_and_response(self, xmldata):
        pass

    def receive_link_msg_and_response(self, xmldata):
        pass

    def receive_and_response(self, request):
        print request.data
        xmldata = ET.fromstring(request.data)
        msg_type = xmldata.find("MsgType")
        print msg_type, msg_type.text
        if msg_type and msg_type.text == "text":
            self.receive_text_msg_and_response(xmldata)
        elif msg_type and msg_type.text == "image":
            self.receive_image_msg_and_response(xmldata)
        elif msg_type and msg_type.text == "image":
            self.receive_voice_msg_and_response(xmldata)
        elif msg_type and msg_type.text == "image":
            self.receive_video_msg_and_response(xmldata)
        elif msg_type and msg_type.text == "image":
            self.receive_shortvideo_msg_and_response(xmldata)
        elif msg_type and msg_type.text == "image":
            self.receive_location_msg_and_response(xmldata)
        elif msg_type and msg_type.text == "image":
            self.receive_link_msg_and_response(xmldata)
        else:
            print "Unknown msg type..."
