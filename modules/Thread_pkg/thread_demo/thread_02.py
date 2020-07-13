#!/usr/bin/env python
#-*- coding:utf-8 -*-

import threading,time

class Match(threading.Thread):

    def __init__(self):
        super(Match, self).__init__()
        self.name = input("请输入姓名：")

    def run(self):

        while 1:
            print(self.name+"领先了。。。")
            time.sleep(1)


if __name__ == '__main__':
    m1 = Match()
    m2 = Match()

    # start方法调用了线程的run方法
    m1.start()
    m2.start()
