#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 多进程通信：队列

from multiprocessing import Process,Queue
import time

def write(q):
    str = ['aa', 'bb', 'cc']
    for value in str:
        print("存入的数据：" + value)
        q.put(value)
        time.sleep(0.5)

def read(q):
    while True:
        if not q.empty():
            value = q.get()
            print("读取到的数据：" + value)
            time.sleep(0.5)
        else:
            break

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
