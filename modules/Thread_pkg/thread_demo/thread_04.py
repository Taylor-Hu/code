#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 线程调度、守护线程、join()阻塞线程的用法

import threading,time

class Guest:
    def eat(self):
        for i in range(10):
            print(threading.current_thread().getName()+"再吃第"+str((i+1))+"锅鱼")
            time.sleep(1)   # 必须添加一点延时，要不然线程一直占用着，别的线程得不到资源
        print(threading.current_thread().getName()+"已经吃完了")


if __name__ == '__main__':

    g = Guest()
    # g.eat()返回的是函数调用的结果，此时线程并没有创建成功；g.eat是一个函数句柄，创建线程需要一个函数句柄的传参
    t1 = threading.Thread(target=g.eat, name="张三")
    t2 = threading.Thread(target=g.eat, name="李四")
    t1.setDaemon(True)  # 守护进程必须设置在start之前，主线程结束之后子线程也必须结束
    t2.setDaemon(True)  # 守护进程必须设置在start之前
    t1.start()
    t2.start()

    for i in range(5):
        print("主人在吃第" + str((i + 1)) + "锅鱼")
        time.sleep(1)

    print("主人已吃完。。。")


