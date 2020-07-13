#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 导入数据库连接
import pymysql

sql = "insert into person values('yfu', 50)"
sql1 = "select * from person where name='hulei'"
sql2 = "select * from person"
sql3 = "insert into person values('lilei', 12)" \
       ", ('hanmeimei', 12)"
# sql4 = "insert into person values('%s', '%d')"%(name, age)
# 1. 创建和mysql数据库的连接
conn = pymysql.connect("192.168.80.128", "root", "123456", "pms")

# 创建游标对象
cur = conn.cursor()

# 执行DML操作
cur.execute(sql3)
#
# 将数据库的变更写入数据库
conn.commit()
#
# 关闭数据库的连接
conn.close()

# cur.execute(sql1)
# cur.execute(sql2)

# 执行DQL数据，查询数据库的内容
# 提取结果集中的内容(一行)，返回的结果已元组的形式存取
# info = cur.fetchone()
# 提取结果集中的内容(所有)，返回的结果已元组的形式存取
# info1 = cur.fetchall()

# print(info)
# print(info1)

# if len(info1) != 0:
#     for i in info1:
#         print(i)
# else:
#     print("找不到用户信息")
#
# conn.close()

