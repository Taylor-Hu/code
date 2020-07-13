#!/usr/bin/env python
#-*- coding:utf-8 -*-

from performance.common.database import DB_Manager
import random, os, time, psutil, re

class CommonUtility:

    # 转化之前：data = 'username=admin&password=admin123&verifycode=0000'
    # 转化之后：data = {'username': 'admin', 'password': 'admin123', 'verifycode': '0000'}
    # 返回字典类型的参数
    def trans_string(self, string):
        format_data = {}
        data1 = string.split('&')
        for info in data1:
            data2 = info.split('=')
            format_data[data2[0]] = data2[1]

        return format_data

    # 获取fid select fid from pw_forums ORDER BY RAND() limit 0,1 where type='forum'
    # 数据库语句：随机获取一个数值
    def get_fid(self):
        fid_list = []
        sql = "select fid from pw_forums where type='forum'"
        result = DB_Manager().db_dql(sql)
        # ((2,), (3,), (4,), (5,), (7,), (8,), (9,), (10,), (11,), (12,))
        # print(type(result)) # <class 'tuple'> 元组类型，要将获取的数据转成列表使用
        if result:
            for i in range(len(result)):
                fid_list.append(result[i][0])
        else:
            print("查询数据为空")
        # [2, 3, 4, 5, 7, 8, 9, 10, 11, 12]
        # print(fid_list)
        return fid_list

    def get_tid(self):
        sql = "select max(tid) from pw_threads"
        result = DB_Manager().db_dql(sql)
        if result:
            # print(result)
            return result[0][0]
        else:
            print("获取tid为空")
            return None

    def test_random(self):
        # 随机值包括边界值3
        num = random.randint(0, 3)
        print(num)


if __name__ == '__main__':
    cu = CommonUtility()
    # fid_list = cu.get_fid()
    # print(fid_list)
    # tid = cu.get_tid()
    # print(tid)

    # for i in range(10):
    #     cu.test_random()

    list = []
    print(random.choice(list))


