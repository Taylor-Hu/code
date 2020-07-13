#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 功能：实现随机发帖，从界面获取元素，而不是从数据库，因为显示环境中，不可以远程登录他人的数据库；


import random, time, re, threading
fid_list = []

import requests
from performance.common.common_phpwind import CommonUtility

class PhpwindDemo:
    def __init__(self):
        self.session = requests.session()

    def login(self):
        data = 'forward=&jumpurl=index.php&step=2&lgt=0&pwuser=perf_2&pwpwd=123456&hideid=0&cktime=31536000'
        format_data = CommonUtility().trans_string(data)
        resp = self.session.post(url='http://192.168.80.128/phpwind/login.php?', data=format_data)
        resp.encoding = 'utf-8'
        if '您已经顺利登录' in resp.text:
            print("login success")
        else:
            print("login failed")

    # 进入home界面，解析获取fid和tid, 而不是从数据库获取
    def home(self):
        resp = self.session.get(url='http://192.168.80.128/phpwind/')
        resp.encoding = 'utf-8'
        if 'PHPwind  - Powered by PHPWind.net' in resp.text:
            print("get home-page success")
        else:
            print("get home-page failed")

        global fid_list
        fid_list = re.findall('tr3 f_one" id="fid_(.+?)">', resp.text)
        # print(fid_list)
        self.fid = int(random.choice(fid_list))
        print("获取fid随机数值是：%d" % (self.fid))

    def PostBlog(self):
        resp = self.session.get('http://192.168.80.128/phpwind/post.php?fid=%d'%(self.fid))
        resp.encoding('utf-8')
        list = re.findall('verify" value="(.+?)" />', resp.text)
        print(list)

        num = random.randint(1000, 9999)
        data = 'magicname=&magicid=&verify=%s&atc_title=html界面获取fid发帖测试——%d&atc_iconid=0' \
               '&atc_content=代码实现发帖dddd&atc_autourl=1&atc_usesign=1&atc_convert=1&atc_rvrc=0' \
               '&atc_enhidetype=rvrc&atc_money=0&atc_credittype=money&atc_desc1=' \
               '&att_special1=0&att_ctype1=money&atc_needrvrc1=0&step=2&pid=&action=new&fid=%d' \
               '&tid=&article=0&special=0'%(list[0], num, self.fid)
        format_data = CommonUtility().trans_string(data)
        resp = self.session.post(url='http://192.168.80.128/phpwind/post.php?', data=format_data)
        resp.encoding = 'utf-8'
        # print(resp.text)
        if '发帖完毕点击进入主题列表' in resp.text:
            print("PostBlog success")
        else:
            print("PostBlog failed")

    def start(self):
        self.login()
        self.home()
        self.PostBlog()


if __name__ == '__main__':

    # pd = PhpwindDemo()
    # pd.login()
    # pd.home()
    # for i in range(1):
    #     pd.PostBlog()
    #     time.sleep(2)

    for i in range(5):
        threading.Thread(target=PhpwindDemo().start).start()

