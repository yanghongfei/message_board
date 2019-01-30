#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 9:53
# @Author  : Fred Yang
# @File    : models.py
# @Role    : ORM

from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, DateTime, TIMESTAMP
from sqlalchemy.dialects.mysql import LONGTEXT

Base = declarative_base()

class MessagesBoard(Base):
    __tablename__ = 'messages_board'  # ITSM故障管理

    # 项目表结构
    id = Column(Integer, primary_key=True, autoincrement=True)  # ID 自增长
    title = Column(String(100), nullable=False)  #标题
    email = Column(String(100), nullable=False)  #邮件
    message = Column(LONGTEXT, nullable=True)    #内容
    create_at = Column(DateTime, nullable=False, default=datetime.now())  # 记录创建时间
    update_at = Column(TIMESTAMP, nullable=False, default=datetime.now())  # 记录更新时间
