#!/usr/bin/env python
#-*- coding:utf-8 -*-

# str = "hello " \
#       "world"
#
# str1 = '''
# hello
# world
# hulei'''
# print(str)
# print(str1)
#
# str2 = "123456789"
# print(len(str2))
# print(str2[0:])
# print(str2[2:6])
# print(str2[2::3]) #369
# print(str2[0:8:2]) #1357
#
# print(str2[-3])         #7
# print(str2[::-1])       #倒序输出  987654321
# print(str2[3::-1])      #4321
# print(str2[6:2:-1])     #7654

# str3 = "aabbccaaccdaaaddccc"
# print(str3.count("aa", 3, 10))
#
# print(str3.capitalize())
#
# #用来做console控制台输出
# print(str3.center(40, '*'))        #**********aabbccaaccdaaaddccc***********
# print(str3.center(len(str3)+10, '='))     #=====aabbccaaccdaaaddccc=====
#
# #查找位置，找不到返回-1
# print(str3.find("bb"))        #2  第一次查找到该字符串的下标
#
# print(str3.replace("a", "k")) #kkbbcckkccdkkkddccc
# print(str3.replace("a", "k", 3))    #kkbbcckaccdaaaddccc

#字符串切割，返回一个列表
str = "sso.changhong.com"
newstr = str.split(".")
print(newstr)           #['sso', 'changhong', 'com']

newstr = str.split(".", 0)    #['sso.changhong.com']
print(newstr)
newstr = str.split(".", 1)    #['sso', 'changhong.com']
print(newstr)
newstr = str.split(".", 2)    #['sso', 'changhong', 'com']
print(newstr)
newstr = str.split(".", 3)    #['sso', 'changhong', 'com']
print(newstr)

# print(str.isalnum())    #False
#
# #判断字符串是否都是字母
# print(str.isalpha())    #False
#
# #判断字符串是否都是数字
# print(str.isdigit())    #False
#
# phone = "13147201352"
# print(phone.isdigit())  #True
#
# str1 = "Hello"
# #转换成小写字母
# print(str1.islower())
# #转换成大写字母
# print(str1.isupper())
# #判断是否是标题
# print(str1.istitle())
#
# print(max(str1))        #o
# #print(str1.startswith())



