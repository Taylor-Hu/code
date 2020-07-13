#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests, time, random, threading
import psutil

class WoniuDemo:
    def __init__(self):
        self.session = requests.session()

    def home(self):
        start_time = int(time.time() * 1000)
        resp = self.session.get(url='http://192.168.80.128:8080/woniusales/')
        end_time = int(time.time() * 1000)
        print("get homepage time=%dms"%(end_time-start_time))
        print("get homepage len=%dbytes" %len(resp.text))
        # print(resp.text)
        # if '蜗牛进销存-首页' in resp.text:
        #     print('get homepage-successful')
        # else:
        #     print('get homepage-fail')

    def login(self):
        data = {'username': 'admin', 'password': 'admin123', 'verifycode': '0000'}
        start_time = int(time.time() * 1000)
        resp = self.session.post(url='http://192.168.80.128:8080/woniusales/user/login', data=data)
        end_time = int(time.time() * 1000)
        print("login-in time=%dms" % (end_time - start_time))
        print("login-in len=%dbytes" % len(resp.text))
        # print(resp.text)

    def sell(self):
        resp = self.session.get(url='http://192.168.80.128:8080/woniusales/sell')
        # print(resp.text)
        # if '蜗牛进销存-销售出库' in resp.text:
        #     print('skip sell-successful')
        # else:
        #     print('skip sell-fail')

    def customer(self):
        resp = self.session.get(url='http://192.168.80.128:8080/woniusales/customer')
        # print(resp.text)
        # if '蜗牛进销存-会员管理' in resp.text:
        #     print('skip customer-successful')
        # else:
        #     print('skip customer-fail')

    def add(self):
        phone = random.randint(10000000, 99999999)
        data = {'customername': '张三', 'customerphone': '187%d'%phone,
                'childsex': '女', 'childdate': '2003-05-26',
                'creditkids': 0, 'creditcloth': 0}
        start_time = int(time.time() * 1000)
        resp = self.session.post(url='http://192.168.80.128:8080/woniusales/customer/add', data=data)
        end_time = int(time.time() * 1000)
        print("add-customer time=%dms" % (end_time - start_time))
        print("add-customer len=%dbytes" % len(resp.text))
        # print(resp.text)

    def monitor(self):
        while True:
            cpu = psutil.cpu_percent()
            mem = psutil.virtual_memory()
            print("cpu:%.2f%%, mem:%.2f%%" % (cpu, mem.percent))
            time.sleep(2)


    def start(self):
        for i in range(2):
            self.home()
            time.sleep(2)
            self.login()
            self.sell()
            time.sleep(1)
            self.customer()
            time.sleep(3)   # 一般操作的时候会休息一下
            self.add()

if __name__ == '__main__':
    print("########################################################主线程开始")
    for i in range(2):
        t1 = threading.Thread(target=WoniuDemo().start)
        t1.start()
    # t1.join()  # 最后一个线程，join的目的是让主线程不会结束,,,同时也阻塞其他代码的运行

    t2 = threading.Thread(target=WoniuDemo().monitor)
    t2.setDaemon(True)  # 主线程结束的时候，monitor监控也必须结束
    t2.start()
    # 一旦主线程结束，子线程就立刻结束

    t1.join()  # 最后一个线程，join的目的是让主线程不会结束
    print("=========================================================主线程结束")



# 1. 完成上述代码，实现基本基于python的性能测试脚本，并利用数据库、csv或全局变量统计数据
# 2. 安装xmapp+phpwind

