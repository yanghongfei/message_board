#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 9:24
# @Author  : Fred Yang
# @File    : sendmail_handler.py
# @Role    : 发送邮件Handler


import json
import tornado.web
from settings import DEFAULT_EMAIL_HOST, DEFAULT_EMAIL_PORT, DEFAULT_EMAIL_USER, DEFAULT_EMAIL_PWD
from libs.sendmail import MailAPI as SendMailAPI
from libs.public import check_mail_format, now_time


class SendMailHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        return self.write('hello mail..')

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body.decode('utf-8'))
        to_list = data.get('to_list', None)
        # subject = data.get('subject', None)
        # content = data.get('content', None)
        # subtype = data.get('subtype', None)
        # att = data.get('att', None)

        if not to_list:
            resp = {
                'status': -1,
                'msg': '收件人不能为空'
            }
            return self.write(resp)

        if not check_mail_format(to_list):
            resp = {
                'status': -10,
                'data': data,
                'datetime': now_time,
                'msg': '邮箱格式不正确，请检查邮箱格式！'
            }
            return self.write(resp)

        try:
            obj = SendMailAPI(mail_host=DEFAULT_EMAIL_HOST, mail_port=DEFAULT_EMAIL_PORT, mail_user=DEFAULT_EMAIL_USER,
                              mail_passwd=DEFAULT_EMAIL_PWD,
                              mail_ssl='true')

            r_send = obj.send_mail(to_list, 'opendevops message board', '我们已经收到你的留言，感谢你的反馈，谢谢!', subtype='plain',
                                   att='None')
            if r_send:
                resp = {
                    'status': 0,
                    'data': data,
                    'msg': '发送成功'
                }
                return self.write(resp)
            else:
                resp = {
                    'status': -3,
                    'data': data,
                    'msg': '发送失败，请检查邮箱账户密码等信息是否正确！'
                }
                return self.write(resp)
        except Exception as e:
            print(e)
