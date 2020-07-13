#!/usr/bin/env python
#-*- coding:utf-8 -*-

from interface.ddt_test_data.common.function import Fun


# 编写基于列表的数据驱动
def test_driver(list):

    for item in list:
        number = item[0]
        expect = item[1]
        actual = Fun().str_2_num(number)
        if actual == expect:
            print("测试成功")
        else:
            print("测试失败，数字是" + number)


if __name__ == '__main__':
    list = [("123", True), (".123", True), ("1.23", True), ("-1.23", True), ("0.123", True),
            (" ", False), ("-", False), (".", False), ("1.2.3", False), ("-12-3", False), ("123@", False),
            ("12/3", False)]
    test_driver(list)
