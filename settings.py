#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 9:32
# @Author  : Fred Yang
# @File    : settings.py
# @Role    : 配置文件

import os

debug = True
xsrf_cookies = False
expire_seconds = 365 * 24 * 60 * 60
cookie_secret = '61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2X6TP1o/Vo='
static_path = os.path.join(os.path.dirname(__file__), "static")
template_path = os.path.join(os.path.dirname(__file__), "templates")

# 邮箱信息
DEFAULT_EMAIL_HOST = os.getenv('DEFAULT_EMAIL_HOST', 'smtp.163.com')
DEFAULT_EMAIL_PORT = os.getenv('DEFAULT_EMAIL_PORT', '465')
DEFAULT_EMAIL_USER = os.getenv('DEFAULT_EMAIL_USER', 'yanghongfei97@163.com')
DEFAULT_EMAIL_PWD = os.getenv('DEFAULT_EMAIL_PWD', 'password')

# 数据库信息
DEFAULT_DB_DBHOST = os.getenv('DEFAULT_DB_DBHOST', '172.16.0.101')
DEFAULT_DB_DBPORT = os.getenv('DEFAULT_DB_DBPORT', '3306')
DEFAULT_DB_DBUSER = os.getenv('DEFAULT_DB_DBUSER', 'root')
DEFAULT_DB_DBPWD = os.getenv('DEFAULT_DB_DBPWD', 'shinezone2015')
DEFAULT_DB_DBNAME = os.getenv('DEFAULT_DB_DBNAME', 'messages_board')

DEFAULT_DB_INFO = {
    'DBHOST': DEFAULT_DB_DBHOST,
    'DBPORT': DEFAULT_DB_DBPORT,
    'DBUSER': DEFAULT_DB_DBUSER,
    'DBPWD': DEFAULT_DB_DBPWD,
    'DBNAME': DEFAULT_DB_DBNAME
}

try:
    from local_settings import *
except:
    pass

settings = dict(
    debug=debug,
    xsrf_cookies=xsrf_cookies,
    cookie_secret=cookie_secret,
    expire_seconds=expire_seconds,
    static_path=static_path,
    template_path=template_path
)
