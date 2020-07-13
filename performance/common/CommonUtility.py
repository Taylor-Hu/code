#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time, psutil, threading
import math

class CommonUtil:

    def test_psutil(self):
        # 获取cpu信息，这里监控的是负载机的cpu，无意义的做法，我们主要是监控服务器的cpu
        # cpu = psutil.cpu_percent(interval=1, percpu=True)
        cpu = psutil.cpu_percent()
        # print(cpu)

        # 获取内存信息
        mem = psutil.virtual_memory()
        # print(mem)

        # cpu:0.00%, mem:84.00%
        print("cpu:%.2f%%, mem:%.2f%%"%(cpu, mem.percent))

        # 获取磁盘信息
        # disk = psutil.disk_partitions()
        # print(disk)

        # # 获取进程pid
        # process = psutil.pids()
        # print(process)
        # # 获取指定进程pid=1380的进程名
        # p = psutil.Process(1380)  # 获取指定进程ID=0
        # print(p.name())

    def test_time(self):
        stime = int(time.time() * 1000)
        print("打印当前时间：%d" % stime)

    def test_thread(self):
        for i in range(10):
            print("子线程在运行")
            time.sleep(1)


rt_home_list = []
rt_login_list = []
# 利用三层包，解决装饰器本身传参的问题
def monitor(name, iteration, stime):
    def wrapper(func):
        def inner(*args):
            for i in range(iteration):
                start_time = int(time.time()*1000)
                func(*args)
                end_time = int(time.time()*1000)
                time.sleep(stime)
                print("请求：%s 响应时间是%d毫秒"%(name, end_time-start_time))
                global rt_home_list
                global rt_login_list
                if name == '打开首页':
                    rt_home_list.append(end_time-start_time)
                else:
                    rt_login_list.append(end_time-start_time)

        return inner
    return wrapper


if __name__ == '__main__':

    print("主线程开始运行")
    t = threading.Thread(target=CommonUtil().test_thread)
    t.setDaemon(True)   # setDaemon必须在start之前调用
    t.start()
    t.join()   # join必须在start之后调用
    print("主线程结束运行")

    # t.join() 将子线程合并到主线程，子线程结束之后主线程才结束
    # t.setDaemon(True) 将子线程设置为守护进程, 主线程结束之后子线程必须结束，必须在start之前调用

