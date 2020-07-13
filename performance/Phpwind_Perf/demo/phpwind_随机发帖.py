#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 今日作业：
# 1. 实现python代码注册200个账户     10min
# 2. 实现发帖功能     10min ==============================
# 3. 向不同的版块随机发帖     10min
# 4. 利用python代码实现对一个帖子的回复   30min

import random, time, re

import requests
from performance.common.common_phpwind import CommonUtility

class PhpwindDemo:
    def __init__(self):
        self.session = requests.session()

    def login(self):
        data = 'forward=&jumpurl=index.php&step=2&lgt=0&pwuser=perf_6&pwpwd=123456&hideid=0&cktime=31536000'
        format_data = CommonUtility().trans_string(data)
        resp = self.session.post(url='http://192.168.80.128/phpwind/login.php?', data=format_data)
        resp.encoding = 'utf-8'
        if '您已经顺利登录' in resp.text:
            print("login success")
        else:
            print("login failed")

        # list = re.findall('verify=(.+)">', resp.text)
        # print(list)
        # return resp.text


    def PostBlog(self):
        # tid = CommonUtility().get_tid()
        # print("当前获取的tid：%d"%tid)
        # resp = self.session.get('http://192.168.80.128/phpwind/read.php?tid=%d'%(tid))
        # list = re.findall('verify" value="(.+?)" />', resp.text)
        # print(list)

        fid_list = CommonUtility().get_fid()
        index = random.randint(0, len(fid_list) - 1)
        print("当前获取fid下标是：%d" % (index))

        resp = self.session.get('http://192.168.80.128/phpwind/post.php?fid=%d'%(fid_list[index]))
        list = re.findall('verify" value="(.+?)" />', resp.text)
        print(list)

        data = 'magicname=&magicid=&verify=%s&atc_title=这是一个发帖测试的帖子——ccccc&atc_iconid=0' \
               '&atc_content=代码实现发帖ccccc&atc_autourl=1&atc_usesign=1&atc_convert=1&atc_rvrc=0' \
               '&atc_enhidetype=rvrc&atc_money=0&atc_credittype=money&atc_desc1=' \
               '&att_special1=0&att_ctype1=money&atc_needrvrc1=0&step=2&pid=&action=new&fid=%d' \
               '&tid=&article=0&special=0'%(list[0], fid_list[index])
        format_data = CommonUtility().trans_string(data)
        resp = self.session.post(url='http://192.168.80.128/phpwind/post.php?', data=format_data)
        resp.encoding = 'utf-8'
        # print(resp.text)
        if '发帖完毕点击进入主题列表' in resp.text:
            print("PostBlog success")
        else:
            print("PostBlog failed")


if __name__ == '__main__':

    pd = PhpwindDemo()
    pd.login()
    for i in range(3):
        pd.PostBlog()
        time.sleep(2)

