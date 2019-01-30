#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 11:00
# @Author  : Fred Yang
# @File    : startup.py
# @Role    : 启动脚本

from tornado.options import define
from libs.application import Application as myapplication
from settings import settings
from biz.handlers.messages_board_handler import MessagesBoardHandler
from biz.handlers.get_message_handler import GetMessageHandler


class Application(myapplication):
    def __init__(self, **settings):
        handlers = [
            (r'/messages_board', MessagesBoardHandler),
            (r'/get_message', GetMessageHandler),
        ]

        super(Application, self).__init__(handlers, **settings)


def main():
    app = Application(**settings)
    app.start_server()


if __name__ == '__main__':
    main()
