#!/usr/bin/env python
#-*- coding:utf-8 -*-

from ddt import ddt, data, file_data, unpack
import unittest
from framework.Ddt_Demo.Calculator_class import Calculator as cl

@ddt
class TestCalculator(unittest.TestCase):

    @data([7, 8, -1], [2, 1, 1], [9.25, 7.25, 2])
    @unpack
    def test_add(self, excepted, num1, num2):
        self.assertEqual(excepted, cl.add(num1, num2))

    @data(*cl.csv_reader('./data/sub_data.csv'))
    @unpack
    def test_sub(self, excepted, num1, num2):
        self.assertEqual(excepted, cl.sub(num1, num2))

    @file_data('./data/multi_data.json')
    @unpack
    def test_multi(self, excepted, num1, num2):
        self.assertEqual(excepted, cl.multi(num1, num2))

    @file_data('./data/div_data.yaml')
    @unpack
    def test_div(self, excepted, num1, num2):
        self.assertEqual(excepted, cl.div(num1, num2))


if __name__ == '__main__':
    unittest.main(verbosity=1)
    unittest.main(verbosity=2)

