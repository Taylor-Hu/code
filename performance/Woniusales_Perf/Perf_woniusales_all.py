#!/usr/bin/env python
#-*- coding:utf-8 -*-

from performance.common.Data_analysis import DataAnaly
import requests, time, random, threading
import psutil

# 用装饰器实现！！！！！！
# 利用全局变量收集性能测试数据
home_list = []
login_list = []
add_list = []

cpu_list = []
mem_list = []

class WoniuDemo:
    def __init__(self):
        self.session = requests.session()
        global home_list
        global login_list
        global add_list
        global cpu_list
        global mem_list

    def home(self):
        start_time = int(time.time() * 1000)
        resp = self.session.get(url='http://192.168.80.128:8080/woniusales/')
        end_time = int(time.time() * 1000)
        print("get homepage time=%dms"%(end_time-start_time))
        home_list.append(end_time-start_time)


    def login(self):
        data = {'username': 'admin', 'password': 'admin123', 'verifycode': '0000'}
        start_time = int(time.time() * 1000)
        resp = self.session.post(url='http://192.168.80.128:8080/woniusales/user/login', data=data)
        end_time = int(time.time() * 1000)
        print("login-in time=%dms" % (end_time - start_time))
        login_list.append(end_time - start_time)

    def sell(self):
        resp = self.session.get(url='http://192.168.80.128:8080/woniusales/sell')

    def customer(self):
        resp = self.session.get(url='http://192.168.80.128:8080/woniusales/customer')


    def add(self):
        phone = random.randint(10000000, 99999999)
        data = {'customername': '张三', 'customerphone': '187%d'%phone,
                'childsex': '女', 'childdate': '2003-05-26',
                'creditkids': 0, 'creditcloth': 0}
        start_time = int(time.time() * 1000)
        resp = self.session.post(url='http://192.168.80.128:8080/woniusales/customer/add', data=data)
        end_time = int(time.time() * 1000)
        print("add-customer time=%dms" % (end_time - start_time))
        add_list.append(end_time - start_time)

    def monitor(self):
        while True:
            cpu = psutil.cpu_percent()
            mem = psutil.virtual_memory()
            print("cpu:%.2f%%, mem:%.2f%%" % (cpu, mem.percent))
            time.sleep(2)
            cpu_list.append(cpu)
            mem_list.append(mem.percent)

    def start(self):
        for i in range(2):
            self.home()
            time.sleep(2)
            self.login()
            self.sell()
            time.sleep(1)
            self.customer()
            time.sleep(2)   # 一般操作的时候会休息一下
            self.add()

if __name__ == '__main__':
    print("########################################################主线程开始")
    for i in range(1):
        t1 = threading.Thread(target=WoniuDemo().start)
        t1.start()

    # t1.join()   # 最后一个线程，join的目的是让主线程不会结束,,,同时也阻塞其他代码的运行

    t2 = threading.Thread(target=WoniuDemo().monitor)
    t2.setDaemon(True)  # 主线程结束的时候，monitor监控也必须结束
    t2.start()
    # 一旦主线程结束，子线程就立刻结束

    t1.join()
    # print(home_list)
    # print(login_list)
    print(add_list)
    # print(cpu_list)
    print(mem_list)

    # 对数据进行分析
    da = DataAnaly()
    print("新增客户的响应时间：平均值：%.2fms, 最大值：%.2fms, 最小值：%.2fms, 90%%的值小于：%.2f, 中位数：%.2f"
          %(da.average(add_list), da.min_max(add_list)[0], da.min_max(add_list)[1], da.percent(add_list, 90), da.median(add_list)))



    # t1.join()    print一开始就全部打印，里面全部是空值
    print("=========================================================主线程结束")
