#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, csv
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def multi(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b

    @staticmethod
    def str_to_num(num):
        if isinstance(num, str):
            try:
                return int(num)
            except ValueError:
                return float(num)
        return num

    # csv：解析的时候只要返回列表类型的数据就可以了
    @staticmethod
    def csv_reader(file):
        if os.path.exists(file):
            with open(file, 'r') as f:
                lines = csv.reader(f)
                contents = []
                for line in lines:
                    content = []
                    for el in line:
                        content.append(Calculator.str_to_num(el))
                    contents.append(content)
                return contents
        return None