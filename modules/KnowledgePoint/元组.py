#!/usr/bin/env python
#-*- coding:utf-8 -*-

# <class 'tuple'>
# tup1 = ("abc", 123, [1, 2, 3], (7, 8, 9))
# print(type(tup1))
#
# tup1 = ('Google', 1997, 'woniuxy', 2000)
# tup2 = (1, 2, 3, 4, 5)
# tup3 = tup1 + tup2
#
# print("tup1[0]:", tup1[0])
# print("tup2[1:5]:", tup2[1:5])
# print(tup3)
# print(tup3[3:])

# tup = [2, 34, 56, 4, 8]
# print(max(tup))
# print(min(tup))
# print(tup.index(4))

# string1 = "abcdefg"
# print(len(string1))         # 7
# print(list(string1))        # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(len(list(string1)))   # 7
#
# print(tuple(string1))       # ('a', 'b', 'c', 'd', 'e', 'f', 'g')
# print(len(tuple(string1)))  # 7

# list1 = [1, 2, 3]
# print(str(list1))       # [1, 2, 3]
# print(len(list1))       # 3
# print(len(str(list1)))  # 9
#
# print(tuple(list1))     # (1, 2, 3)
# print(len(list1))       # 3
# print(len(tuple(list1)))  # 3

tup2 = (10, 20, 30)
print(len(tup2))            # 3
print(str(tup2))            # (10, 20, 30)
print(len(str(tup2)))       # 12

print(list(tup2))            # [10, 20, 30]
print(len(list(tup2)))       # 3

# 元组知识点：
# 1. 元组一旦定义，长度不可变，且元组中的元素不可修改
# 2. 元组中的元素如果是列表，则可以修改列表中的值
# 3. 元组的函数只要不改变长度及元素的值，其他和list一样；tuple[index] tuple.index(obj)

# 序列：字符串、列表、元组；
# 对序列的统一操作: 1. 切片 str[index1:index2:length]
#                 2. 数据类型转换 str(list[tuple]) list(str[tuple]) tuple(list[str])










