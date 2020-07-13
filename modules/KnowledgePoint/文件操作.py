#!/usr/bin/env python
#-*- coding:utf-8 -*-


# fp1 = open("D:\\pro\\web\\hulei\\python\\test_doc\\test01.txt", 'r')

# 读取所有文本内容，但是不好处理
# content = fp1.read()
# 1001,zhangsan,abc
# 1002,lisi,abc
# 1003,wangwu,abc

# 读取一行内容
# content = fp1.readline()
# 1001,zhangsan,abc

# 获取多行内容，返回一个列表
# content = fp1.readlines()
# print("%s" %(content))  # ['1001,zhangsan,abc\n', '1002,lisi,abc\n', '1003,wangwu,abc']
# for con in content:
#     print("%s" %(con), end='')
# fp1.close()

# fp1 = open("D:\\pro\\web\\hulei\\python\\test_doc\\test01.txt", 'a+')
# str = "1004,zhaoliu,abc"
# fp1.write(str)
# fp1.close()

with open("D:\\pro\\web\\hulei\\python\\test_doc\\test01.txt", 'r') as fp:
    context = fp.read()
    print(type(context))        # <class 'str'>
