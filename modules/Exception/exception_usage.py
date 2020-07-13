#!/usr/bin/env python
#-*- coding:utf-8 -*-

class BasicDemo:
    # @classmethod
    # def __new__(cls, *args, **kwargs):
    #     print("这是一个类被实例化时最优先调用的方法.")

    def __init__(self):
        print("这是一个实例化会被调用的方法：构造方法.")

    def __del__(self):
        print("这是一个析构方法，在类实例被销毁时执行。")

    def __enter__(self):
        print("这是with子句开始执行时调用。")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("这是with子句所负责的范围结束运行被调用。")
        return True     # 返回True表示屏蔽异常，否则正确抛出异常

    def test(self, value):
        if value > 10:
            raise NumberIsToBigError("抛出异常，数字太大了")
        else:
            print("这是正确的数字")

# 自定义异常
class NumberIsToBigError(Exception):
    pass

# if __name__ == '__main__':  # 当别的模块引入该模块或类时，该分支下面的语句将不会随着import而执行
    # extend = BasicDemo()
    # try:
    #     extend.test(15)
    # except NumberIsToBigError as e:
    #     print(e)

    # 这是一个实例化会被调用的方法：构造方法.
    # 抛出异常，数字太大了
    # 这是一个析构方法，在类实例被销毁时执行。



    # with BasicDemo() as extend:
    #     extend.test(100)

    # 这是一个实例化会被调用的方法：构造方法.
    # 这是with子句开始执行时调用。
    # 这是with子句所负责的范围结束运行被调用。
    # 这是一个析构方法，在类实例被销毁时执行。



    with BasicDemo() as extend:
        extend.test(5)

    # 这是一个实例化会被调用的方法：构造方法.
    # 这是with子句开始执行时调用。
    # 这是正确的数字
    # 这是with子句所负责的范围结束运行被调用。
    # 这是一个析构方法，在类实例被销毁时执行。