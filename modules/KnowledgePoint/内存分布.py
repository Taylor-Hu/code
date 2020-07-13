#!/usr/bin/env python
#-*- coding:utf-8 -*-

a = 100
b = a
a = 200
print(id(a))
print(id(b))
print("a = %d b = %d"%(a,b))

# 打印结果
# 2005200608
# 2005199008
# a = 200 b = 100

b = a
print(id(a))
print(id(b))
print("a = %d b = %d"%(a,b))
# 打印结果
# 2005199008
# 2005199008  b指向了a所指向的地址
# a = 200 b = 200


a = [1, 2, 3]
b = a
a[2] = 300
print(id(a))
print(id(b))
print("a = %s b = %s"%(a, b))

# 25165256
# 25165256
# a = [1, 2, 300] b = [1, 2, 300]