#! /usr/bin/env python
# -*- coding: utf-8 -*-

class AgileOne:

    def open_browser(self, url):
        print('打开AgileOne主页。')

    def input_text(self, locator, text):
        print('在%s元素输入内容%s。' % (locator, text))

    def click(self, locator):
        print('单击%s元素一次。' % locator)

    def wait(self, sleep):
        print('等待%s秒时间。' % sleep)

    def close_browser(self):
        print('关闭浏览器。')
