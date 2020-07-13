#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests, re

# (.+?)贪婪模式：re.findall
def download(text):
    # list = []
    # css和超链接
    list = re.findall('href="(.+?)"/>', text)
    print(list)

    # js、png、jpg、vcode
    list += re.findall('src="(.+?)"', text)
    print(list)

    # background jpg 注意转义符的使用
    list += re.findall("url\('(.+?)'\)", text)
    print(list)

if __name__ == '__main__':
    session = requests.session()
    resp = session.get(url='http://192.168.80.128:8080/woniusales/')
    download(resp.text)
