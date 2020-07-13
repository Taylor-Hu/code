#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/7 12:11
# software: PyCharm

import pymysql

PI = 3.14
def getConn(hostname='localhost',username='root',password='root',database='atm'):
    conn = pymysql.connect(hostname,username,password,database)
    return conn

def update_info(sql):
    conn = getConn()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    return True

#查询余额
def find_balance(sql):
    conn = getConn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchone()
    conn.close()
    return result

#查询所有信息
def find_all(sql):
    conn = getConn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    conn.close()
    return result