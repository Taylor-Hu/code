#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Cups():
    color = "white"
    type = "round"
    brand = "ali"
    price = 8888

    def intro_cup(self):
        print("color=%s"%(self.color))

    @staticmethod
    def intro_cup_price():
        print("price=%s" % (Cups.price))


if __name__=='__main__':

    cup1 = Cups()
    cup1.color = "red"
    cup1.type = "雅诗兰黛"
    cup1.brand = "ali"
    cup1.price = 123
    cup1.intro_cup()

    cup2 = Cups()
    cup2.color = "green"
    cup2.type = "南极人"
    cup2.brand = "阿迪达斯"
    cup2.price = 123
    cup2.intro_cup()

    # 静态方法可以直接调用，不需要初始化对象
    Cups.intro_cup_price()  # price=8888



