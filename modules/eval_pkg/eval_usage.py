#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

# 1.可以进行数学运算
str = '3+5'
print(eval(str)) # 8

# 2.实现list、dict、tuple的转化
a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
b = eval(a)
print(type(b)) # <class 'list'>
print(b) # [[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]

a = "{1: 'a', 2: 'b'}"
b = eval(a)
print(type(b)) # <class 'dict'>
print(b) # {1: 'a', 2: 'b'}

a = "([1,2], [3,4], [5,6], [7,8], (9,0))"
b = eval(a)
print(type(b)) # <class 'tuple'>>
print(b) # ([1, 2], [3, 4], [5, 6], [7, 8], (9, 0))

# 3.正因为可执行这个特性，导致eval的不安全性
# 这样可以随意删除、篡改文件，导致系统的不安全性；
eval("__import__('os').system('dir D:\pro\web\hulei\python')")
# 等效于：
os.system('dir D:\pro\web\hulei\python')

# 4.执行字符串
def hello(x):
    print("你输入的值为: " + x)

str = "hello('" + '你好啊' + "')"
print(str)
eval(str)
# hello('你好啊')
# 你输入的值为: 你好啊