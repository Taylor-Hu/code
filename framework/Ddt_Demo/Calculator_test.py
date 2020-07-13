#!/usr/bin/env python
#-*- coding:utf-8 -*-

#! /usr/bin/env python
# -*- coding: utf-8 -*-

from framework.Ddt_Demo.Calculator_class import Calculator

class CalculatorTest:

    def test_add(self):
        result = Calculator().add(3, 5)
        if result == 8:
            print("5+3=8 test ok!")
        else:
            print("5+3=8 test nok!")

    def test_sub(self):
        result = Calculator().sub(5, 3)
        if result == 2:
            print("5-3=2 test ok!")
        else:
            print("5-3=2 test nok!")

if __name__ == '__main__':
    ct = CalculatorTest()
    dir_list = dir(ct)
    print(dir_list)

    for module_name in dir_list:
        if module_name.startswith("test") and hasattr(ct, module_name):
            getattr(ct, module_name)()

