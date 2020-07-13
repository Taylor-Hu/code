#!/usr/bin/env python
#-*- coding:utf-8 -*-

import threading, time

def add():
    sum = 0
    for i in range(50000):
        sum += i
    print(threading.current_thread().getName()+"完后加法，总合是："+str(sum))


def sub(max):
    while max > 0:
        max -= 1
    print(threading.current_thread().getName()+"完成减法")


if __name__ == '__main__':

    # start_time = time.time()
    # add()
    # sub()
    # end_time = time.time()
    # print("总共耗时：%f"%(end_time-start_time))
    # 总共耗时：0.090715


    t1 = threading.Thread(target=add, name="add_thread")
    # 以元组的形式传参
    t2 = threading.Thread(target=sub, args=((999999,)), name="sub_thread")
    start_time = time.time()
    t1.start()
    t2.start()
    end_time = time.time()
    print("总共耗时：%f"%(end_time-start_time))
    # 0.010936
