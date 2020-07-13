#!/usr/bin/env python
#-*- coding:utf-8 -*-

# python协程
# 可以在协程任务阻塞时立刻切换提高效率
# pip install gevent
import gevent,time

from gevent import monkey
# 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块
monkey.patch_all() # 添加这句话就可以在代码中使用以前的耗时模块

def fun1(num):
    for i in range(num):
        print("函数1中的循环次数：" + str(i))
        time.sleep(0.2)

def fun2(num):
    for i in range(num):
        print("函数2中的循环次数：" + str(i))
        time.sleep(0.2)

if __name__ == '__main__':
    print("创建协程g1")
    g1 = gevent.spawn(fun1, 3)
    print("创建协程g2")
    g2 = gevent.spawn(fun2, 3)
    g1.join()   # 阻塞主线程，确保子线程在主线程结束前运行完
    g2.join()
    print("创建协程完成")


# 创建协程g1
# 创建协程g2
# 函数1中的循环次数：0
# 函数2中的循环次数：0
# 函数1中的循环次数：1
# 函数2中的循环次数：1
# 函数1中的循环次数：2
# 函数2中的循环次数：2
# 创建协程完成

