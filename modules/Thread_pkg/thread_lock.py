#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/14 12:25
# software: PyCharm
import threading

balance = 0
lock = threading.Lock()
def change_money(money):
    global balance
    balance += money
    balance -= money

# 线程不安全
def run_thread(money):
    for i in range(100000):
        lock.acquire() #加锁
        try:
            change_money(money)
        finally:
            lock.release() #开锁
if __name__ == '__main__':
    #直接构造线程
    print('开始主线程。。。')
    t1 = threading.Thread(target=run_thread,args=(100,))
    t2 = threading.Thread(target=run_thread,args=(300,))
    t1.start()  #就绪状态
    t2.start()
    t1.join()
    t2.join()
    print(balance)
    print('结束主线程。。。')

