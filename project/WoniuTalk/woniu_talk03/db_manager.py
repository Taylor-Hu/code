#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pymysql

class DB_Manager:

    def __init__(self):
        # 数据库的名字是woniu_user
        self.conn = pymysql.connect("192.168.80.128", "root", "123456", "woniu_user")
        self.cur = self.conn.cursor()

    def db_dml(self, sql):
        self.cur.execute(sql)
        result = self.conn.commit()
        return result

    def db_dql(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def __delete__(self, instance):
        self.conn.close()
        self.cur.close()
