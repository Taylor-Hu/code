#!/usr/bin/env python
#-*- coding:utf-8 -*-

def get_sum(num):
    sum = 0;
    for i in range(num+1):
        sum += i

    return sum

print(get_sum(10))