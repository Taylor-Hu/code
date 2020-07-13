#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/14 11:23
# software: PyCharm
import threading, random,time

'''
1.创建两个类，一个类是Person，属性包括hp,att,方法包括(攻击)，每次攻击可以产生不同的伤害
另一个类是tiger,属性也是hp,att，方法也是（攻击）

2.攻击方法使用run方法重写，人攻击5次，tiger攻击8次；

3.执行完毕后输出各自剩余的hp

'''

class Person(threading.Thread):

    def __init__(self,hp,att):
        threading.Thread.__init__(self,target=self.run,args=())
        self.hp = hp
        self.att = att

    def run(self):
        #创建老虎对象
        tiger = Tiger(1500, 40)
        tiger.setName('大老虎')
        for i in range(5):
            atts = random.randint(0, self.att)
            time.sleep(1)
            print('%s产生的攻击力是%d'%(threading.current_thread().getName(),atts))
            tiger.hp -= atts
            print('%s受到了%d点伤害'%(tiger.getName(),atts))
        print('%s的生命值为%d'%(tiger.getName(),tiger.hp))

        for j in range(8):
            atts = random.randint(0, self.att)
            time.sleep(2)
            print('%s产生的攻击力是%d' % (tiger.getName(), atts))
            self.hp -= atts
            print('%s受到了%d点伤害' % (self.getName(), atts))
        print('%s的生命值为%d' % (self.getName(), tiger.hp))

    def __str__(self):
        return '生命力%d攻击力%d'%(self.hp,self.att)

class Tiger(threading.Thread):

    def __init__(self,hp,att):
        threading.Thread.__init__(self, target=self.run, args=())
        self.hp = hp
        self.att = att

    def run(self):
        for i in range(8):
            atts = random.randint(0, self.att)
            time.sleep(2)
            print('%s产生的攻击力是%d' % (threading.current_thread().getName(), atts))

    def __str__(self):
        return '生命力%d攻击力%d'%(self.hp,self.att)

if __name__ == '__main__':
    wusong = Person(1200,60)
    wusong.setName('武松')
    wusong.start()