#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 闭包：函数当中再定义函数，层次不限，至少两层，内部函数可以使用外部函数的变量

# def outer(func):
#     def inner():
#         print("装饰器内的调用.")
#         func()
#     return inner
#
# # 装饰器在使用时，如果装饰的是一个函数，则其调用方式类似于：outer(被装饰函数名)
# @outer
# def test():
#     print("这是test函数体")
#
# # 使用了装饰器之后的函数，还是正常调用即可。
# test()
# # 装饰器内的调用.
# # 这是test函数体



# # 利用装饰器对函数传参
# def outer(func):
#     def inner():
#         print("开始运行函数...")
#         func()
#         print("结束函数运行...")
#     return inner
#
# @outer
# def test():
#     print("==== test ====")
#
# test()
# # 开始运行函数...
# # ==== test ====
# # 结束函数运行...



# def outer(func):
#     def inner(x, y):
#         print("开始运行函数...")
#         func(x, y)
#         print("结束函数运行...")
#     return inner
#
# @outer
# def test(x, y):
#     print("==== %d ======= %d ====" % (x, y))
#
# test(10, 20)
# # 开始运行函数...
# # ==== 10 ======= 20 ====
# # 结束函数运行...



# def outer(func):
#     def inner(*args):
#         print("开始运行函数...")
#         func(*args)
#         print("结束函数运行...")
#     return inner
#
# @outer
# def test(x, y, z):
#     print("===== %d === %d === %d =====" % (x, y, z))
#
# test(10, 20, 30)
# # 开始运行函数...
# # ===== 10 === 20 === 30 =====
# # 结束函数运行...


# 给装饰器本身传递参数
# def outer(arg1, arg2):
#     def wrapper(func):
#         def inner(*args):
#             print("开始运行函数...")
#             print("装饰器参数的值为：%d, %d" % (arg1, arg2))
#             func(*args)
#             print("结束函数运行...")
#         return inner
#     return wrapper
#
# @outer(100, 200)
# def test(x, y, z):
#     print("==== %d ==== %d === %d ====" % (x, y, z))
#
# test(10, 20, 30)
