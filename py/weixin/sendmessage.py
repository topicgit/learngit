#!_*_ coding:utf-8

"""
作用：调用微信接口发送消息
时间：2015／01/05
传递参数：
APPID
APPSECRET
需要去公共号平台获取
examples：
test = weixin(APPID, APPSECRET)
app_tokent = test.get_token()
user_list = test.get_user_list(app_tokent)
test.send_message(app_tokent,user,'test message')
"""

import requests
import json


class weixin():

    def __init__(self, APPID, APPSECRET):
        self.APPID = APPID
        self.APPSECRET = APPSECRET

    def __check_result_error(self, data):
        """
        检查返回值是否有错误，如果有，打印错误
        """

        if data.get('errcode'):
            print "error code:%s\nerror message:%s" % (data.get('errcode'), data.get('errmsg'))
            return True
        else:
            return False

    def get_token(self):
        """
        获取tokent 用于发送消息和获取用户列表使用
        tokent 官方说明有效期2个小时，可以定时获取
        返回值
        {'access_token':'BldqUtWb8lkLxGrDq0dtlyVl8W','expires_in':7200}
        access_token 发送信息和列出用户列表需要用的tokent
        expires_in 过期时间7200分钟
        """
        TOKENT_URL = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (
            self.APPID, self.APPSECRET)
        APP_TOKENT = requests.get(TOKENT_URL, timeout=20).json()
        if self.__check_result_error(APP_TOKENT):
            return False
        return APP_TOKENT

    def get_user_list(self, app_tokent):
        """
        获取关注公共号用户列表
        """
        if not app_tokent:
            return False
        next_openid = ""
        openid_list = []

        while True:
            OPENID_URL = "https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s&next_openid=%s" % (
                app_tokent, next_openid)
            openid = requests.get(OPENID_URL, timeout=20).json()
            if self.__check_result_error(openid):
                return False
            openid_list.extend(openid['data']['openid'])
            if openid['next_openid']:
                break
        return openid_list

    def get_user_info(self, app_tokent, openid):
        """
        获取用户详细信息
        中文需要encode('utf-8')转码
        """
        get_user_url = "https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s&openid=%s&lang=zh_CN" % (
            app_tokent, openid)
        user_info = requests.get(get_user_url, timeout=20).json()
        if self.__check_result_error(user_info):
            return False
        return user_info

    def send_message(self, app_tokent, openid, message):
        """
        给用户发送客服消息
        """
        if not app_tokent or not openid or not message:
            return False
        SEND_URL = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=%s" % app_tokent
        post = {
            "touser": openid,
            "msgtype": "text",
            "text": {
                "content": message
            }
        }
        send_result = requests.post(
            SEND_URL, data=json.dumps(post, ensure_ascii=False)).json()
        if self.__check_result_error(send_result):
            return False
        return send_result['errmsg']

    def template_id_list(self, app_tokent):
        """
        暂时不支持
        """
        template_id_url = "https://api.weixin.qq.com/cgi-bin/template/api_add_template?access_token=%s" % app_tokent
        # requests.post(template_id_url,data=json.dumps({'template_id_short':'01'})).json()

    def send_template_message(self, app_tokent, post):
        template_message_url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s" % app_tokent
        result = requests.post(template_message_url,
                               data=json.dumps(post)).json()
        if self.__check_result_error(result):
            return False
        return result['errcode']
if __name__ == '__main__':
    APPID = "wx5089cd1fefd5d976"
    APPSECRET = "d4624c36b6795d1d99dcf0547af5443d"
    test = weixin(APPID, APPSECRET)
    # print test.get_user_list(test.get_token()['access_token'])
    message = {'first': '邮件服务无法收发邮件', 'performance': '目前无法收发邮件',
               'time': '2016/01/06', 'remark': '请尽快处理', 'to_target_url': 'http://wiki.golet.me'}
    post = {
        "touser": "ojTiSw7K7RXnv8_y9UEfGYX3CwB8",
        "template_id": "fLAJhWh95Zc0V2Gk6ZRaLBfeBlRusEF4mk5AW_nYWRk",
        "url": message['to_target_url'],
        "data": {
            "first": {
                "value": message['first'],
                "color": "#173177"
            },
            "performance": {
                "value": message['performance'],
                "color": "#FF0033"
            },
            "time": {
                "value": message['time'],
                "color": "#FF0033"
            },
            "remark": {
                "value": message['remark'],
                "color": "#173177"
            }
        }
    }
    if not test.send_template_message(test.get_token()['access_token'], post):
    	print "消息发送成功"
