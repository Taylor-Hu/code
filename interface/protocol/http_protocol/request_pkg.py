#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 使用random包
import requests, time, random, threading

class WoniuDemo:
    def __init__(self):
        self.session = requests.session()

    def home(self):
        resp = self.session.get(url='http://192.168.80.128:8080/woniusales/')
        if '蜗牛进销存-首页' in resp.text:
            print('测试成功')
        else:
            print('测试失败')

    def login(self):
        data = {'username': 'admin', 'password': 'admin123', 'verifycode': '0000'}
        resp = self.session.post(url='http://192.168.80.128:8080/woniusales/user/login', data=data)
        if resp.text == 'login-pass':
            print("登录成功")
        else:
            print("登录失败")

    def add(self):
        phone = random.randint(10000000, 99999999)
        data = {'customername': '张三', 'customerphone': '131%d' % phone,
                'childsex': '女', 'childdate': '2003-05-26',
                'creditkids': 0, 'creditcloth': 0}
        resp = self.session.post(url='http://192.168.80.128:8080/woniusales/customer/add', data=data)
        if resp.text == 'add-successful':
            print("新增会员成功")
        else:
            print("新增会员失败")


if __name__ == '__main__':
    wn = WoniuDemo()
    wn.home()
    wn.login()
    wn.add()
