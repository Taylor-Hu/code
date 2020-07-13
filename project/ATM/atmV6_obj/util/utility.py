#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pymysql

class ConnUtil:

    def __init__(self):
        self.conn = pymysql.connect("192.168.80.128", "root", "123456", "account")
        self.cur = self.conn.cursor()

    # DML操作
    def db_dml(self, sql):
        result = self.cur.execute(sql)
        self.conn.commit()
        return result

    def db_dql(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def __del__(self):
        self.cur.close()
        self.conn.close()




















