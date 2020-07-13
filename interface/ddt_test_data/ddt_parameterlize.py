#!/usr/bin/env python
#-*- coding:utf-8 -*-

from interface.ddt_test_data.common.function import Fun

import unittest
from parameterized import parameterized    # 导包

# https://blog.csdn.net/NoamaNelson/article/details/103669251

class TestDemo(unittest.TestCase):
    @classmethod
    # 重写父类的方法setUpClass，每次执行一个测试类时，会调用一次;
    def setUpClass(cls):
        cls.func = Fun()
        print("每次执行一个测试类时，会调用一次")

    @classmethod
    def tearDownClass(cls):
        cls.func = None
        print("每次执行一个测试类后，会调用一次")

    # 只有unittest才可以进行参数化使用，特殊用法，读出excel表格的数据进行参数化，这是常用的做法
    @parameterized.expand([('12345', True), ('123T5', False), ('-123.45', True), ('123-5', False), ('-.', False)])
    def test_01(self, number, expect):
        actual = self.func.str_2_num(number)
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main()