#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 今日作业：
# 1. 实现python代码注册200个账户     10min
# 2. 实现发帖功能     10min ==============================
# 3. 向不同的版块随机发帖     10min
# 4. 利用python代码实现对一个帖子的回复   30min

# 获取fid和tid必须从界面元素中获取，解析html界面就可以，不可以直接从数据库中取值
# 真实应用场景中是不可以直接操作数据库的，这个涉及到安全知识

import random, time, re, threading

import requests
from performance.common.common_phpwind import CommonUtility

is_post = True

class PhpwindDemo:
    def __init__(self):
        self.session = requests.session()

    def login(self):
        data = 'forward=&jumpurl=index.php&step=2&lgt=0&pwuser=perf_10&pwpwd=123456&hideid=0&cktime=31536000'
        format_data = CommonUtility().trans_string(data)
        resp = self.session.post(url='http://192.168.80.128/phpwind/login.php?', data=format_data)
        resp.encoding = 'utf-8'
        if '您已经顺利登录' in resp.text:
            print("login success")
        else:
            print("login failed")

    # 进入home界面获取fid
    def home(self):
        resp = self.session.get(url='http://192.168.80.128/phpwind/')
        resp.encoding = 'utf-8'
        if 'PHPwind  - Powered by PHPWind.net' in resp.text:
            print("get home-page success")
        else:
            print("get home-page failed")

        fid_list = []
        fid_list = re.findall('tr3 f_one" id="fid_(.+?)">', resp.text)
        # print(fid_list)
        self.fid = int(random.choice(fid_list))
        print("获取fid随机数值是：%d" % (self.fid))

    # 根据fid进入发帖页面获取tid
    def post_page(self):
        resp = self.session.get(url='http://192.168.80.128/phpwind/thread.php?fid=%d' %(self.fid))
        resp.encoding = 'utf-8'
        if '- PHPwind  - Powered by PHPWind.net' in resp.text:
            print("get post-page success")
        else:
            print("get post-page failed")

        global is_post  # 标记是否可以有帖子
        tid_list = []
        tid_list = re.findall('href="read\.php\?tid=(.+?)" target', resp.text)
        print(tid_list)
        if tid_list:
            self.tid = int(random.choice(tid_list))
            print("回帖tid=%d"%(self.tid))
        else:
            is_post = False
            print("fid=%d的界面没有帖子"%(self.fid))


    def ReplyBlog(self):
        # 如果没有帖子就无法进行回帖操作
        if is_post == False:
            print("fid=%d 界面没有帖子，无法回帖"%(self.fid))
            return

        # 进入回帖界面获取verify
        resp = self.session.get('http://192.168.80.128/phpwind/read.php?tid=%d'%(self.tid))
        resp.encoding = 'utf-8'
        list = re.findall('verify" value="(.+?)" />', resp.text)
        print(list)

        # 进入回帖界面获取需要回帖的标题
        re_title = re.findall('name="atc_title" value="(.+?)" ', resp.text)
        print(re_title[0])

        # 请求里面不要包含特殊字符&
        data = 'magicname=&magicid=&verify=%s&atc_title=%s&atc_iconid=0&atc_content=回复帖子而已-666' \
               '&atc_autourl=1&atc_usesign=1&atc_convert=1&atc_rvrc=0&atc_enhidetype=rvrc' \
               '&atc_money=0&atc_credittype=money&atc_desc1=&att_special1=0&att_ctype1=money' \
               '&atc_needrvrc1=0&step=2&pid=&action=reply&fid=%d&tid=%d&article=&special=0'\
               %(list[0], re_title[0], self.fid, self.tid)
        format_data = CommonUtility().trans_string(data)
        resp = self.session.post(url='http://192.168.80.128/phpwind/post.php?', data=format_data)
        resp.encoding = 'utf-8'
        # print(resp.text)

        if '发帖完毕点击进入主题列表' in resp.text:
            print("ReplyBlog success")
        else:
            print("ReplyBlog failed")

    def start(self):
        self.login()
        self.home()
        self.post_page()
        self.ReplyBlog()

if __name__ == '__main__':

    for i in range(1):
        threading.Thread(target=PhpwindDemo().start).start()



