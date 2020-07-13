#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, glob

# 2.打印当前文件夹及其子目录下的文件
def print_directory_contents(sPath):
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

# D:\pro\code\modules\SendEmail\attachment\report.zip
# D:\pro\code\modules\SendEmail\css_style\report.html
# D:\pro\code\modules\SendEmail\send_email.py
# D:\pro\code\modules\SendEmail\__init__.py

if __name__ == '__main__':
    print_directory_contents('D:\pro\code\modules\SendEmail')

    # # glob可以进行过滤，list可以直接获取资源，不需要带上目录
    # print(glob.glob('../SendEmail/*.py'))
    # # ['../SendEmail\\send_email.py', '../SendEmail\\__init__.py']
    #
    # print(os.listdir('../SendEmail'))
    # # ['attachment', 'css_style', 'send_email.py', '__init__.py']
    #
    # # 绝对路径
    # folder = os.path.abspath('../SendEmail/')
    # print(folder)
    # # D:\pro\code\modules\SendEmail\








