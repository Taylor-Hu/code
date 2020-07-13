#!/usr/bin/env python
#-*- coding:utf-8 -*-

from interface.ddt_test_data.common.function import Fun

# 基于文件的数据驱动
def test_driver():
    with open('./data/test_data.csv') as file:
        list = file.readlines()

        for item in list:
            number = item.strip().split(",")[0]
            expect = item.strip().split(",")[1]     #  得到的是字符串
            result = Fun().str_2_num(number)     # 得到的是bool变量
            if str(result) == expect:
                print("测试成功")
            else:
                print("测试失败，数字是" + number)


if __name__ == '__main__':
    test_driver()






