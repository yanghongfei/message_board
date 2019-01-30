#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 10:42
# @Author  : Fred Yang
# @File    : messages_board_handler.py
# @Role    : 留言板Handler

import json
from database import db_session
from models.models import MessagesBoard
from tornado.web import RequestHandler
from libs.public import now_time


class MessagesBoardHandler(RequestHandler):
    """ Falut故障管理路由"""

    def get(self, *args, **kwargs):
        self.render("board.html")

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body.decode("utf-8"))
        title = data.get('title', None)
        email = data.get('email', None)
        message = data.get('message', None)

        if not title and not email and not message:
            resp = {
                'status': -1,
                'data': data,
                'datetime': now_time,
                'msg': '参数不能为空'
            }
            return self.write(resp)

        else:
            try:
                name_info = db_session.query(MessagesBoard).filter(MessagesBoard.title == title).first()
                if name_info:
                    resp = {
                        'status': -2,
                        'data': data,
                        'datetime': now_time,
                        'msg': '标题不可重复: {} 已经存在'.format(title)
                    }
                    return self.write(resp)
                else:
                    db_session.add(
                        MessagesBoard(title=title, email=email, message=message))
                    db_session.commit()

                    resp = {
                        'status': 0,
                        'data': data,
                        'datetime': now_time,
                        'msg': 'Name: {} 添加成功'.format(title)
                    }
                    return self.write(resp)

            except Exception as e:
                db_session.rollback()
                error = repr(e)
                resp = {
                    'status': -3,
                    'data': data,
                    'datetime': now_time,
                    'msg': error
                }

                return self.write(resp)

    def put(self, *args, **kwargs):
        data = json.loads(self.request.body.decode("utf-8"))
        title = data.get('title', None)
        email = data.get('email', None)
        message = data.get('message', None)

        try:
            update_info = {
                "title": title,
                "email": email,
                "message": message
            }
            db_session.query(MessagesBoard).filter(MessagesBoard.title == title).update(update_info)
            db_session.commit()
            resp = {
                'status': 0,
                'data': data,
                'datetime': now_time,
                'msg': '更新成功'
            }
            return self.write(resp)

        except Exception as e:
            db_session.rollback()
            error = repr(e)
            resp = {
                'status': -3,
                'data': data,
                'datetime': now_time,
                'msg': error
            }

            return self.write(resp)

    def delete(self, *args, **kwargs):
        data = json.loads(self.request.body.decode("utf-8"))
        title = data.get('title', None)

        if not title:
            resp = {
                'status': -1,
                'data': data,
                'datetime': now_time,
                'msg': '参数不能为空'
            }
            return self.write(resp)
        else:
            try:
                db_session.query(MessagesBoard).filter(MessagesBoard.title == title).delete(
                    synchronize_session=False)
                db_session.commit()
                resp = {
                    'status': 0,
                    'data': data,
                    'datetime': now_time,
                    'msg': '删除成功'
                }
                return self.write(resp)

            except Exception as e:
                db_session.rollback()
                error = repr(e)
                resp = {
                    'status': -3,
                    'data': data,
                    'datetime': now_time,
                    'msg': error
                }

                return self.write(resp)
