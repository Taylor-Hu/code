#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 使用http.client包
import http.client
import random

class WoniuSalesTest:
    def __init__(self):
        # 建立http client的连接，要传入header，同时后续连接需要cookie
        self.conn = http.client.HTTPConnection(host='192.168.80.128', port=8080)
        self.header = {'Content-Type':'application/x-www-form-urlencoded'}
        self.cookie = ''

    def access_homepage(self):
        self.conn.request(method='GET', url='/woniusales/')
        resp = self.conn.getresponse().read().decode()
        if '蜗牛进销存-首页' in resp:
            print('测试成功')
        else:
            print('测试失败')

    def do_login(self):
        body = 'username=admin&password=admin123&verifycode=0000'
        self.conn.request(method='POST', url='/woniusales/user/login', body=body, headers=self.header)
        resp = self.conn.getresponse()
        # print(resp.headers)     # 打印响应头
        # print(resp.getheaders())    # 以列表+元组的方式存储响应头
        # print(resp.getheader('Set-Cookie'))
        # 要将响应的cookie赋值给全局变量self.cookie
        self.cookie += resp.getheader('Set-Cookie')
        if resp.read().decode() == 'login-pass':
            print("登录成功")
        else:
            print("登录失败")

    def add_customer(self):
        # header是字典类型，新增字典按照key:keyvalue的形式
        # cookie欺骗，即使不登录只要知道了其他的sessionid就可以跳过登录的步骤
        # self.header['Cookie'] = 'JSESSIONID=646978386C8954BF7442AB0FA9ED65D4;'
        # body = 'customername=家人&customerphone=13111113333&childsex=男&childdate=2000-03-27&creditkids=0&creditcloth=0'
        # # body涉及到中文，所以使用body.encode()
        # self.conn.request(method='POST', url='/woniusales/customer/add', body=body.encode(), headers=self.header)
        # resp = self.conn.getresponse().read().decode()
        # # print(resp)
        # if resp == 'add-successful':
        #     print("新增会员成功")
        # else:
        #     print("新增会员失败")

        # 响应的header必须加上cookie
        self.header['Cookie'] = self.cookie
        rand_phone = random.randint(10000000, 99999999)
        body = 'customername=家人&customerphone=131%d&childsex=男&childdate=2000-03-27&creditkids=0&creditcloth=0'%rand_phone
        # body涉及到中文，所以使用body.encode()
        self.conn.request(method='POST', url='/woniusales/customer/add', body=body.encode(), headers=self.header)
        resp = self.conn.getresponse().read().decode()
        if resp == 'add-successful':
            print("新增会员成功")
        else:
            print("新增会员失败")


if __name__ == '__main__':
    test = WoniuSalesTest()
    test.access_homepage()
    test.do_login()
    test.add_customer()
