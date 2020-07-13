#!/usr/bin/env python
#-*- coding:utf-8 -*-

def outer(argv1, argv2):
    def wrapper(func):
        def inner(*args):
            print("开始运行函数---")
            print("装饰器参数的值：%d, %d"%(argv1, argv2))
            func(*args)
            print("结束函数运行---")
        return inner
    return wrapper


@outer(100, 200)
def test(x, y, z):
    print("=== %d === %d === %d ==="%(x, y, z))

if __name__ == '__main__':
    test(10, 20, 30)


# 开始运行函数---
# 装饰器参数的值：100, 200
# === 10 === 20 === 30 ===
# 结束函数运行---









