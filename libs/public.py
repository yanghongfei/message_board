#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 11:17
# @Author  : Fred Yang
# @File    : public.py
# @Role    : 公共信息


import time
import re

now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

#检查邮箱格式

def check_mail_format(email):
    str=r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
    if re.match(str, email):
        print('邮箱格式正确！')
        return True
    else:
        print('邮箱格式不正确！')
        return False

