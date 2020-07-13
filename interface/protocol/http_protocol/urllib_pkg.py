#!/usr/bin/env python
# -*- coding:utf-8 -*-

# python爬虫之urllib模块

import urllib.request
import urllib
import urllib.parse

class WoniuSalesTest:

    def access_homepage(self):
        resp = urllib.request.urlopen(url='http://192.168.80.128:8080/woniusales/')
        html = resp.read().decode()
        if '蜗牛进销存-首页' in html:
            print('测试成功')
        else:
            print('测试失败')

    def do_login(self):
        url = 'http://192.168.80.128:8080/woniusales/user/login/'
        formData = {"username": "admin", "password": "admin123", "verifycode": "0000"}
        data = urllib.parse.urlencode(formData).encode()  # 将str类型转换为bytes类型
        # 头部信息要添加User-Agent
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        resp = urllib.request.Request(url=url, data=data, headers=header, method='POST')
        response = urllib.request.urlopen(resp)

        if response.read().decode() == 'login-pass':
            print("登录成功")
        else:
            print("登录失败")


if __name__ == '__main__':
    wn = WoniuSalesTest()
    wn.access_homepage()
    wn.do_login()

