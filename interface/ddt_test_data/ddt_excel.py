#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/6 15:27
# software: PyCharm

# 完成对xls的读写
import xlrd,xlwt
import xlutils.copy

# 打印xls表格数据的内容
# ll = xlrd.open_workbook('./data/atm_data.xls')
# atm_info = all.sheets()[0]  #获取第一个sheet页
# rows = atm_info.nrows   #获取行数
# cols = atm_info.ncols #获取列数
# for i in range(rows):
#     print(atm_info.row_values(i))
# print(atm_info.cell_value(1, 2))



# 往特定的某行某列写入数据
# new_acc = ['zhao','333','1000']
# data = xlrd.open_workbook('./data/atm_data.xls')
# t_atm = data.sheets()[0]
# rows = t_atm.nrows   #获取行数
# cols = t_atm.ncols #获取列数
# # print('行数：%d, 列数：%d'%(rows, cols))
# ws = xlutils.copy.copy(data)
# atm_info=ws.get_sheet(0)
#
# for i in range(rows+1):
#     if i == rows:
#         for j in range(cols):
#             atm_info.write(i, j, new_acc[j])
# ws.save('./data/atm_data.xls')



