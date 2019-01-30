#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 10:36
# @Author  : Fred Yang
# @File    : application.py
# @Role    : 定制Application

from shortuuid import uuid
from tornado import httpserver, ioloop
from tornado import options as tnd_options
from tornado.options import options, define
from tornado.web import Application as tornadoApp
from .web_logs import ins_log


define("addr", default='0.0.0.0', help="run on the given ip address", type=str)
define("port", default=8000, help="run on the given port", type=int)
define("progid", default=str(uuid()), help="tornado progress id", type=str)


class Application(tornadoApp):
    """ 定制 Tornado Application 集成日志"""

    def __init__(self, handlers=None, default_host="", transforms=None, **settings):
        tnd_options.parse_command_line()
        ins_log.read_log('info', '%s' % options.progid)
        super(Application, self).__init__(handlers, default_host, transforms, **settings)
        http_server = httpserver.HTTPServer(self)
        http_server.listen(options.port, address=options.addr)
        self.io_loop = ioloop.IOLoop.instance()

    def start_server(self):
        """
        启动 tornado 服务
        :return:
        """
        try:
            ins_log.read_log('info', 'progressid: %(progid)s' % dict(progid=options.progid))
            ins_log.read_log('info', 'server address: %(addr)s:%(port)d' % dict(addr=options.addr, port=options.port))
            ins_log.read_log('info', 'web server start sucessfuled.')
            self.io_loop.start()
        except KeyboardInterrupt:
            self.io_loop.stop()
        except:
            import traceback
            ins_log.read_log('error', '%(tra)s' % dict(tra=traceback.format_exc()))


if __name__ == '__main__':
    pass
