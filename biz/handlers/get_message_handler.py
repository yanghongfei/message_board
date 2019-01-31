#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 16:36
# @Author  : Fred Yang
# @File    : get_message.py
# @Role    : 说明脚本功能


from database import db_session
from models.models import MessagesBoard
from tornado.web import RequestHandler
from libs.public import now_time


class GetMessageHandler(RequestHandler):
    def get(self, *args, **kwargs):
        name = self.get_argument('name')
        name_info = db_session.query(MessagesBoard).filter(MessagesBoard.name == name).all()
        # print(name_info[0].id)
        message = name_info[0].message
        resp = {
            'status': 0,
            'data': message,
            'datetime': now_time,
            'msg': '参数不能为空'
        }
        return self.write(resp)
