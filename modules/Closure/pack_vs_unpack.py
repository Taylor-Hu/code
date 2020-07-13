#!/usr/bin/env python
#-*- coding:utf-8 -*-

def pack_method(*args):
    # 当一个方法的形参前面有一个*号时，表示这是一个装包方法
    # 装包方法的含义：我们可以传入无限多的参数
    # 所传入的所有参数都会被放到一个元组变量中，每一个参数都是这个元组数据的一个元素
    # 无论你传入的参数是基本数据类型，还是列表、元组、字典
    # 装包方法常用于设计函数或方法需要不定长参数的场景
    print(type(args), args)

def unpack_method(v1, v2, v3):
    # 对于有参数的函数或方法在调用时，在实参前边加一个*这样的用法叫做拆包方法
    # 拆包方法在运用的时候，你的实参可以是元组，也可以是列表
    # 但是无论是哪个，一定要注意这个实参的元素个数一定要和被调用的函数或方法的参数个数保持一致，否则会报错
    print(type(v1), v1)
    print(type(v2), v2)
    print(type(v3), v3)


def dict_pack_method(**kwargs):
    # 对于形参含有两个*的方法属于字典的装包方法
    # 字典的装包方法，要求传入的参数必须是key=value的形式
    # 字典的装包方法也是常用于设计具有不定长参数的函数的方法
    # 假如想设计既有普通的不定长参数又有带键名的不定长参数的函数或者方法：
    # def function(name, *args, **kwargs)
    print(type(kwargs), kwargs)


def dict_unpack_method(name, age, sex):
    # 对于调用函数或者方法时传入一个字典类型的数据，并且字典类型数据前面使用了2个*的情况叫做字典的拆包方法；
    # 字典的拆包方法必须注意：传入的字典数据其键名必须和函数或方法的参数个数、名字一一对应，否则无法拆包成功
    print(type(name), name)
    print(type(age), age)
    print(type(sex), sex)


if __name__ == '__main__':

    v1 = 'a'
    v2 = 'b'
    v3 = 3
    v4 = ('c', 12)
    v5 = [1, 2, 3, 'm']
    v6 = [4, 5, 6]
    print("================pack method==============")
    # <class 'tuple'> ('a', 'b', 3, ('c', 12))
    pack_method(v1, v2, v3, v4)
    pack_method(v4)

    print("================unpack method==============")
    unpack_method(v1, v2, v3)
    # unpack_method(*v4)    会报错，因为拆包需要三个参数
    unpack_method(*v6)

    print("################pack method##############")
    # <class 'dict'> {'name': '张三', 'age': '26', 'sex': 'male', 'grade': '四年级'}
    dict_pack_method(name='张三', age='26', sex='male', grade='四年级')

    print("################unpack method##############")
    dict_unpack_method('谢谢', 23, 'female')
    dict_data = {'name':'长协', 'age':18, 'sex':'male'}
    dict_unpack_method(**dict_data)

