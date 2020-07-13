#!/usr/bin/env python
#-*- coding:utf-8 -*-
# 使用二维列表和函数完成ATM功能

from atmV3.manger_atmV3_List_2 import *

show_start_menu()
while 1:
    choice = int(input("请输入您的选择："))
    # while 1:
    if choice==1:
        login_index = login()
        break     #没有break跳出循环执行不到后面的语句就会报错
    elif choice==2:
        regedit()
    else:
        exit(0)


while 1:
    sel = int(input("***请选择：1.查询余额 2.存款 3.取款 4.转账 5.修改密码 6.返回上一级 7.退出***"))
    if sel == 1:
        query_balance(login_index)
    elif sel == 2:
        save_money(login_index)
    elif sel == 3:
        draw_money(login_index)
    elif sel == 4:
        tran_money(login_index)
    elif sel == 5:
        modify_pwd(login_index)
    elif sel == 6:
        exit(0)
    else:
        exit(0)







