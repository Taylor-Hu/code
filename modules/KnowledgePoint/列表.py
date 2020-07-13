#!/usr/bin/env python
#-*- coding:utf-8 -*-


# li1 = [1,2,3]
# print(li1)
#
# li2 = ["a", "sdf", li1, [6,7,8]]
# print(li2)
#
# li2[0]
#
# li2.append("world")
# print(li2)
#
# li2.remove("sdf")
# print(li2)
#
# del li2[0]
# print(li2)
#
# li1
# del li1
# #li1
#
# li1 = [1,2,3]
# li1
# li1.clear() #清空列表，列表为空但是仍存在
# li1

# #list1 = [1, 2, 3, 4, 5]
# list1 = [[1,2],3,4,[5,6,7]]
# print(type(list1))
# print(type(list1[0]))
# for i in list1:
#     if type(i) == list:
#         for j in i:
#             print(j)
#     else:
#         print(i)

#列表反转
# list2 = [1, 2, 3, 4, 5]
# list2.reverse()
# print(list2)
# print(list2[::-1])  #反转

# 冒泡排序：最小数往下沉
# list1 = [1, 45, 3, 7, 2]
# for i in range(0, len(list1)-1):# 外层循环len(list1)-1次
#     for j in range(0, len(list1)-i-1):#内层循环i+j=len(list1)-1
#         if list1[j] < list1[j+1]:
#             list1[j], list1[j+1] = list1[j+1], list1[j]
# print(list1)

#两种for循环是不一样的
# for i in list (i代表数据元素)
# for i in range(0, len(list)-1)  (i代表的是下标)
list1 = [1001, 123, 1000]
list1.sort()














