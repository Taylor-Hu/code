#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 实现将字符串转化成数字
# 完善代码，使用异常处理的方式

class Fun:

    def str_2_num(self, str):
        is_point = 0
        is_separator = 0
        is_digital = 0
        is_correct = False

        for i in str:
            num = ord(i)
            if num == 47 or num < 45 or num > 57:
                # raise Exception("ERROR-NUMBER")
                return is_correct
            elif num == 45:
                is_separator += 1
            elif num == 46:
                is_point += 1
            else:
                is_digital += 1

        if is_separator <= 1 and is_point <= 1 and is_digital > 0:
            if is_separator == 1 and ord(str[0]) != 45:
                is_correct = False
            else:
                is_correct = True
        else:
            is_correct = False

        return is_correct
