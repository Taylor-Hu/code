#! /usr/bin/env python
# -*- coding: utf-8 -*-

from framework.Kdt_demo.Agileone import AgileOne
import os
import csv

class KeywordDriven:
    # start_test_1的简化版本
    def start_test(self):
        agileone_test = AgileOne()
        keyword_file = os.path.join(os.getcwd(), './data/keyword.txt')
        # 文本保存格式是utf8, 如果是gdk就必须设置为gdk
        with open(keyword_file, 'r', encoding='utf-8') as f:
            for keyword_list in csv.reader(f):
                # 注意pop的用法，keyword_list=【open_browser, http://192.168.80.128/agileone】，open_browser只传入keyword_list[1]
                method_name = keyword_list.pop(0).lower().replace(' ', '_')
                if hasattr(agileone_test, method_name):
                    getattr(agileone_test, method_name)(*keyword_list)

    def start_test_1(self):
        agileone_test = AgileOne()
        keyword_file = os.path.join(os.getcwd(), './data/keyword.txt')
        with open(keyword_file, 'r', encoding='utf-8') as f:
            for line in csv.reader(f):
                keyword_list = line
                method_name = keyword_list[0].lower().replace(' ', '_')
                if hasattr(agileone_test, method_name):
                    method = getattr(agileone_test, method_name)
                    # keyword_list=【open_browser, http://192.168.80.128/agileone】，open_browser只传入keyword_list[1]
                    keyword_list.pop(0)
                    args = keyword_list
                    method(*args)

    def start_chinese_test(self):
        agileone_test = AgileOne()
        key_list = {'打开浏览器': 'open_browser', '输入文本': 'input_text',
                    '登录': 'click', '等待': 'wait', '关闭浏览器': 'close_browser'}
        keyword_file = os.path.abspath('.') + '/data/keyword_chinese.txt'
        # 文本保存格式是utf8, 如果是gdk就必须设置为gdk
        with open(keyword_file, 'r', encoding='utf-8') as f:
            for keyword_list in csv.reader(f):
                method_name = key_list[keyword_list.pop(0)]
                if hasattr(agileone_test, method_name):
                    getattr(agileone_test, method_name)(*keyword_list)

    def start_chinese_test_1(self):
        agileone_test = AgileOne()
        key_list = {'打开浏览器': 'open_browser', '输入文本': 'input_text',
                    '登录': 'click', '等待': 'wait', '关闭浏览器': 'close_browser'}
        keyword_file = os.path.abspath('.') + '/data/keyword_chinese.txt'
        with open(keyword_file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                # strip()方法去掉空格, ['打开浏览器', 'http://192.168.80.128/agileone']
                keyword_list = line.strip().split(',')
                # 注意字典取值的方法
                method_name = key_list[keyword_list[0]]
                if hasattr(agileone_test, method_name):
                    method = getattr(agileone_test, method_name)
                    args = []
                    # print(len(keyword_list)) keyword_list=['打开浏览器', 'http://192.168.80.128/agileone'],len(keyword_list)=2
                    for i in range(1, len(keyword_list)):
                        args.append(keyword_list[i])
                        # print(args)
                    method(*args)


if __name__ == '__main__':
    # KeywordDriven().start_test()
    # KeywordDriven().start_chinese_test()

    # KeywordDriven().start_test_1()
    KeywordDriven().start_chinese_test_1()
