#!/usr/bin/env python
#-*- coding:utf-8 -*-

import math


class DataAnaly:
    # 平均值
    def average(self, list):
        sum = 0
        for i in list:
            sum += i
        return round(sum / len(list), 2)

    # 最小数值和最大数值
    def min_max(self, list):
        list.sort()
        min_sum = list[0]
        max_sum = list[len(list) - 1]
        return min_sum, max_sum

    # 90%的意义必须搞清楚
    def percent(self, list, ration):
        index = int(len(list) * ration / 100 - 1)
        list.sort()
        return list[index]

    # 中位数
    def median(self, list):
        length = len(list)
        list.sort()
        if length % 2 == 0:  # 偶数个
            return round((list[int(length / 2)] + list[int(length / 2) - 1]) / 2, 2)
        else:
            return round(list[int(length / 2)], 2)

    # 标准差
    def standard_deviation(self, list, average):
        sum = 0
        for i in list:
            sum += (i - average) ** 2
        return round(math.sqrt(sum / len(list)), 2)


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 7]
    da = DataAnaly()
    print(da.average(list1))
    print(da.min_max(list1))
    print(da.percent(list1, 90))
    print(da.median(list1))
    print(da.standard_deviation(list1, da.average(list1)))

