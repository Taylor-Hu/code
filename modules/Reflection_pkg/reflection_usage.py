#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 主要介绍反射的概念
import random


class Student:
    def __init__(self):
        self._id = None
        self._name = None
        self._sex = None
        self._grade = None

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_sex(self):
        return self._sex

    def set_sex(self, sex):
        self._sex = sex

    def get_grade(self):
        return self._grade

    def set_grade(self, grade):
        self._grade = grade

    def set_student(self, id, name, sex, grade):
        pass


if __name__ == '__main__':
    # 传统的方法
    student = Student()
    student.set_id('001')
    # print(student.get_id())
    student._name = 'zhangsan'
    # print(student._name)
    student._sex = "female"
    student._grade = "大三"
    #
    # # 已知student类中的方法，hasattr, getattr, setattr
    # print(getattr(student, '_name'))
    # setattr(student, '_sex', 'male')
    # print(getattr(student, '_sex'))
    # print(hasattr(student, 'class'))    # false

    # if hasattr(student, 'get_id'):
    #     # print(getattr(student, 'get_id'))   # getattr(student, 'get_id')得到的是方法
    #     print(getattr(student, 'get_id')()) # getattr(student, 'get_id')()得到的是实例化的对象
    #     # 上面的调用等价于下面的用法
    #     method1 = getattr(student, 'get_id')
    #     print(method1())
    #
    # if hasattr(student, 'set_grade'):
    #     # 一定要注意这里是如何得到set方法的，传入多个参数可以用逗号分隔开
    #     setattr(student, 'set_grade')('3期班')
    #     print(getattr(student, 'get_grade')())

    print('*****************************************************************')
    # 如果根本不知道类中有什么方法
    dir_list = dir(student)
    # print(dir_list)
    # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__','__format__',
    #  '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
    #  '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
    #  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
    #  '_grade', '_id', '_name', '_sex',
    #  'get_grade', 'get_id', 'get_name', 'get_sex',
    #  'set_grade', 'set_id', 'set_name', 'set_sex', 'set_student']

    for method_name in dir_list:
        # print(method_name)
        if not (method_name.startswith('_')) and hasattr(student, method_name):
            # 首先需要获得方法的对象
            method_obj = getattr(student, method_name)
            if method_name.startswith('set'):
                # 然后通过下面这条语句来得到当前方法对象的参数个数
                count = method_obj.__code__.co_argcount - 1
                args = []
                for i in range(count):
                    # 利用随机数对参数进行随机赋值
                    args.append(random.randint(1, 100))
                # 调用并执行带有参数的方法
                method_obj(*args)
                print(method_name, args)
            else:
                print(method_name, method_obj())

