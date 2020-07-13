#!/usr/bin/env python
#-*- coding:utf-8 -*-

#!/usr/bin/env python
#-*- coding:utf-8 -*-

import threading, time
class CommonUtil:
    def test_thread(self):
        for i in range(5):
            print("子线程在运行: 第%d次"%i)
            time.sleep(1)


if __name__ == '__main__':
    print("主线程开始运行")
    t = threading.Thread(target=CommonUtil().test_thread)
    t.setDaemon(True)   # setDaemon必须在start之前调用
    t.start()
    t.join()   # join必须在start之后调用
    print("主线程结束运行")

    # t.join() 将子线程合并到主线程，子线程结束之后主线程才结束
    # t.setDaemon(True) 将子线程设置为守护进程, 主线程结束之后子线程必须结束，必须在start之前调用


