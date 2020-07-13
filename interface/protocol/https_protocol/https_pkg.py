#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib3, random, requests

# 忽略警告信息
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.SubjectAltNameWarning)

# 1.使用https协议进行连接的时候，必须使用证书，证书目录 C:\\Tools\\localhost2.crt
# 2.tomcat中必须将localhost https的端口配置为8443，默认端口是443
# 登录
session = requests.session()
data = {'username':'admin','password':'admin123', 'verifycode':'0000'}
resp = session.post('https://localhost:8443/woniusales/user/login', data=data, verify='C:\\Tools\\localhost2.crt')
# resp = session.post('https://localhost:8443/woniusales/user/login', data=data, verify=False)
print(resp.text)

# add添加会员
rand_phone = random.randrange(10000000, 99999999)
data = {'customername':'李四','customerphone':'188%d' % rand_phone,'childsex':'男',
        'childdate':'2018-01-12','creditkids':202,'creditcloth':33}
resp = session.post('https://localhost:8443/woniusales/customer/add', data=data, verify=False)
print(resp.text)