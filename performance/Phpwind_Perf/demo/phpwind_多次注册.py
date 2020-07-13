#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 今日作业：
# 1. 实现python代码注册200个账户     10min
# 2. 实现发帖功能     10min   ===========================
# 3. 向不同的版块随机发帖     10min
# 4. 利用python代码实现对一个帖子的回复   30min

import random, time

import requests
from performance.common.common_phpwind import CommonUtility

class PhpwindDemo:
    def __init__(self):
        self.session = requests.session()

    def register(self):
        # data = 'forward=&step=2&regname=perf_10&regpwd=123456&regpwdrepeat=123456&regemail=1234567c@qq.com&rgpermit=1'
        # format_data = CommonUtility().trans_string(data)
        # resp = self.session.post(url='http://192.168.80.128/phpwind/register.php? ', data=format_data)
        # resp.encoding = 'utf-8'
        # print(resp.text)

        num = random.randint(100, 2000)
        pwd = random.randint(100000, 110000)
        data = 'forward=&step=2&regname=perf_%d&regpwd=123456&regpwdrepeat=123456' \
               '&regemail=%d@qq.com&rgpermit=1'%(num, pwd)
        format_data = CommonUtility().trans_string(data)
        resp = self.session.post(url='http://192.168.80.128/phpwind/register.php? ', data=format_data)
        resp.encoding = 'utf-8'
        if '恭喜您！亲爱的会员，您已经注册成功' in resp.text:
            print("注册成功: %s"%format_data)
        elif '您已经是注册成员,请不要重复注册!' in resp.text:
            print("重复注册: %s"%format_data)
        else:
            print("其他未知错误：%s"%format_data)



if __name__ == '__main__':

    for i in range(5):
        # print("开始第%d次注册"%i)
        pd = PhpwindDemo()
        pd.register()
        time.sleep(3)



