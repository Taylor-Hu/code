#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 优化：模拟真实环境中的缓存数据，
# 真实测试环境：第二次登录同一个页面的时候，缓存会起作用，不需要再重新下载资源文件了
# 1. 第一次下载后，将文件名保存在列表中；第二次访问时，先进行判断
# 2. 第一次下载后，将文件名保存在磁盘中，第二次访问时，先进行判断

import requests, re, os
from performance.common.CommonUtility import monitor, rt_home_list
import threading
# 正则表达式 非贪婪模式

iteration = 5
stime = 1
file_list = []

class WoniuDemo:
    def __init__(self):
        self.session = requests.session()

    @monitor('打开首页', iteration, stime)
    def home(self):
        resp = self.session.get(url='http://192.168.80.128:8080/woniusales/')
        self.download(resp.text)

    def download(self, text):
        global file_list
        # css和超链接
        list = re.findall('href="(.+?)"/>', text)

        # js、png、jpg、vcode
        list += re.findall('src="(.+?)"', text)

        # background jpg  注意转义符的使用
        list += re.findall("url\('(.+?)'\)", text)

        # 获取download目录下的资源文件, 将资源保存在硬盘
        down_list = os.listdir('./download')

        # 拼接网址
        for item in list:
            if not item.replace('/', '_') in down_list:
                if item.startswith('/'): # 根目录
                    url = 'http://192.168.80.128:8080' + item
                elif item.startswith('http'):    # 完整路径
                    url = item
                else:   # 没有‘/’，即是相对于当前目录的路径
                    url = 'http://192.168.80.128:8080/woniusales' + item

                resp = self.session.get(url)

                # 获取文件名
                # temp_list = item.split('/')
                # file_name = temp_list[len(temp_list) - 1]

                file_name = item.replace('/', '_')
                with open('./download/' + file_name, 'wb') as file:
                    file.write(resp.content)    # resp.text是str, resp.content是二进制字节


if __name__ == '__main__':
    print("########################################################主线程开始")
    for i in range(1):
        t1 = threading.Thread(target=WoniuDemo().home)
        t1.start()

    t1.join()
    print(rt_home_list)

    print("=========================================================主线程结束")
