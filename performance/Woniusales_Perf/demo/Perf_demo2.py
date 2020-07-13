#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests, time, random, threading

class WoniuDemo:
    def __init__(self):
        self.session = requests.session()

    def home(self):
        resp = self.session.get(url='http://192.168.80.128:8080/woniusales/')
        # print(resp.text)

    def login(self):
        data = {'username': 'admin', 'password': 'admin123', 'verifycode': '0000'}
        resp = self.session.post(url='http://192.168.80.128:8080/woniusales/user/login', data=data)
        print(resp.text)

    def add(self):
        phone = random.randint(10000000, 99999999)
        data = {'customername': '张三', 'customerphone': '131%d'%phone,
                'childsex': '女', 'childdate': '2003-05-26',
                'creditkids': 0, 'creditcloth': 0}
        resp = self.session.post(url='http://192.168.80.128:8080/woniusales/customer/add', data=data)
        print(resp.text)

    def start(self):
        for i in range(20):
            # self.home()
            self.login()
            time.sleep(3)   # 一般操作的时候会休息一下
            self.add()

if __name__ == '__main__':
    wn = WoniuDemo()
    for i in range(100):
        threading.Thread(target=wn.start).start()
