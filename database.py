#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 9:38
# @Author  : Fred Yang
# @File    : database.py
# @Role    : 初始化数据库

from models.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from settings import DEFAULT_DB_INFO as MYSQL_CONFIG

engine = create_engine(
    f'mysql+mysqlconnector://{MYSQL_CONFIG["DBUSER"]}:{MYSQL_CONFIG["DBPWD"]}@{MYSQL_CONFIG["DBHOST"]}/{MYSQL_CONFIG["DBNAME"]}?charset=utf8')

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


def init_db():
    Base.metadata.create_all(engine)
    print('[Success] 表结构创建成功!')


if __name__ == '__main__':
    init_db()  # 创建表结构
