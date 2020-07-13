#!/usr/bin/env python
#-*- coding:utf-8 -*-

# import time
# time.time() 获取当前时间戳的函数
# print(time.time())  # 1578725670.7939212 从1970年1月1日到当前时间的浮点秒数
# time.localtime() 获取当前时间对象
# t = time.localtime()
# year = t.tm_year
# month = t.tm_mon
# day = t.tm_mday
# print("%s年%s月%s日" % (year, month, day)) # 2020年1月11日
#
# print(time.strftime("%y-%m-%d %H:%M:%S", time.localtime())) # 20-01-11 14:54:30

# dict1 = {1:2, 3:4, 5:[1,2,3]}
# print(dict1) # {1: 2, 3: 4, 5: [1, 2, 3]}
# dict2 = dict1.copy()
# print(dict2) # {1: 2, 3: 4, 5: [1, 2, 3]}
# dict3 = dict1
# print(dict3) # {1: 2, 3: 4, 5: [1, 2, 3]}
#
# dict1[3] = 10 # {1: 2, 3: 10, 5: [1, 2, 3]}
# print(dict1)
# dict1[5][2] = 100 # {1: 2, 3: 10, 5: [1, 2, 100]}
# print(dict1)
#
# print(dict1.get(3)) # 10
# dict1.clear()
# print(dict1)        # {} 清空字典

dict1 = {1:2,2:3,3:4,4:5}
list_values = dict1.values()
list_keys = dict1.keys()

for i in list_keys:
    value = dict1.get(i)
    print("%d:%d"%(i,value))

# 添加元素到字典
dict1[7] = 100
print(dict1)     # {1: 2, 2: 3, 3: 4, 4: 5, 7: 100}













