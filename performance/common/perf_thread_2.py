#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 目的：创建两个线程，test_thread循环，monitor随时监控CPU的运行状态；
# 要求主线程结束之后子线程必须立刻结束运行

import time, threading
import psutil

import threading, time
class CommonUtil:
    def test_thread(self):
        for i in range(3):
            print("子线程在运行: 第%d次"%i)
            time.sleep(1)

    def monitor(self):
        while True:
            cpu = psutil.cpu_percent()
            mem = psutil.virtual_memory()
            print("cpu:%.2f%%, mem:%.2f%%" % (cpu, mem.percent))
            time.sleep(1)


if __name__ == '__main__':
    print("########################################################主线程开始")
    for i in range(2):
        t1 = threading.Thread(target=CommonUtil().test_thread)
        t1.start()

    # t1.join()   # 不能加在这个地方，否则t2线程只会执行一次, 最后一个线程，join的目的是让主线程不会结束,,,同时也阻塞其他代码的运行

    t2 = threading.Thread(target=CommonUtil().monitor)
    t2.setDaemon(True)  # 主线程结束的时候，monitor监控也必须结束，要求一旦主线程结束，子线程就立刻结束
    t2.start()

    t1.join()   # 最后一个线程，join的目的是让主线程不会结束
    print("=========================================================主线程结束")


