#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/7 10:39
# software: PyCharm

# 实现业务处理与UI分离
#一个模块有两种名称：1.模块名：2.模块全名:p1.p2.mname

from project.ATM.atmV3.db_manager import *

#添加数据
def add_info():
    acc_name = input('请输入账户名称')
    acc_pass = input('请输入账户密码')
    balance = int(input('请输入账户余额'))
    sql = 'insert into acc_info values("%s","%s",%d)'%(acc_name,acc_pass,balance)
    flag = update_info(sql)
    if flag:
        print('添加数据成功')
    else:
        print('添加数据失败')
#修改余额
def update_balance():
    acc_name = input('请输入您要修改的账户的名称')
    balance = int(input('请输入修改后的余额'))
    sql = 'update acc_info set balance=%d where acc_name="%s"'%(balance,acc_name)
    flag = update_info(sql)
    if flag:
        print('修改数据成功')
    else:
        print('修改数据失败')


def query_balance():
    acc_name = input('请输入您要查询的账户的名称')
    sql = 'select balance from acc_info where acc_name="%s"'%(acc_name)
    result = find_balance(sql)
    print("查询到的余额是%d"%result)


def delete_acc():
    acc_name = input('请输入您要删除的账户的名称')
    sql = 'delete from acc_info where acc_name="%s"'%acc_name
    flag = update_info(sql)
    if flag:
        print('删除数据成功')
    else:
        print('删除数据失败')



#列表显示所有信息
def list_acc():
    sql = 'select * from acc_info'
    result = find_all(sql)
    for i in result:
        print(i)


def show_main_menu():
    while 1:
        choice = input('1.添加；2.修改；3.删除；4.查询；5.列表显示')
        if choice == '1':
            add_info()
        elif choice == '2':
            update_balance()
        elif choice == '3':
            delete_acc()
        elif choice == '4':
            query_balance()
        elif choice == '5':
            list_acc()

show_main_menu()




