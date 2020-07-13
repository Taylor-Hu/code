#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/6 10:28
# software: PyCharm
#使用文件对ATM进行重构

#1.显示开始菜单；
def show_start_menu():
    choice = input('1.登录；2.注册；')
    if choice == '1' :
        acc_name = login()
        return acc_name
    elif choice == '2':
        regedit_acc()
        return show_start_menu()
    else:
        return show_start_menu()

#2.1账号检查
def check_acc(acc):
    file = open('../data/atm_data.txt')
    atm_info = file.readlines()
    if len(atm_info) != 0:
        for i in atm_info:
            if i[:i.find(',')] == acc :
                file.close()
                return True
        else:
            file.close()
            return False
    else :
        file.close()
        return False

#2.注册；
def regedit_acc():
    while True:
        acc_name = input('请输入账号名称')
        if check_acc(acc_name):
            print('账号已存在，请重新输入')
        else:
            print('账号输入正确')
            break

    #输入注册密码
    acc_pass = input('请输入密码')
    acc_balance = input('请输入初始金额')

    file = open('../data/atm_data.txt','a+')
    new_acc = '\n'+acc_name + ',' + acc_pass + ',' + acc_balance
    file.writelines(new_acc)
    file.close()
    print('您的账号是%s;密码是%s；余额是%s' % (acc_name, acc_pass, acc_balance))

#3.1密码验证
def confirm_pass(acc_name):
    while True:
        acc_pass = input('请输入密码')
        file = open('../data/atm_data.txt')
        atm_info = file.readlines()
        for i in atm_info:
            acc_info = i.split(',')
            if acc_info[0] == acc_name:
                if acc_info[1] == acc_pass:
                    print('输入正确，欢迎使用本机')
                    file.close()
                    return acc_name
        else:
            print('密码输入错误，请重新输入密码')
            file.close()

def login():
    while True:
        acc_name = input('请输入您的账号')
        if check_acc(acc_name):
            acc_name = confirm_pass(acc_name)
            return acc_name
        else:
            print('没有这个账号，请重新输入')



#4.显示主菜单
def show_main_menu(acc_name):
    while True:
        choice = input('1.查询余额；2.存款；3.取款；4.转账')
        if choice == '1':
            balance = get_balance(acc_name)
            print('您的账户余额是%s'%(balance))
        elif choice == '2':
            save_money(acc_name)
        elif choice == '3':
            draw_money(acc_name)
        elif choice == '4':
            tran_money(acc_name)
        else:
            pass

#5.查询余额；
def get_balance(acc_name):
    file = open('../data/atm_data.txt')
    atm_info = file.readlines()
    for i in atm_info:
        acc_info = i.split(',')
        if acc_info[0] == acc_name:
            file.close()
            return acc_info[2]

#从文件中读取所有的内容，改变其中选定的余额，返回该条记录
def read_info(acc_name,balance):
    file = open('../data/atm_data.txt', 'r')
    atm_info = file.readlines()
    for i in atm_info:
        acc_info = i.split(',')
        if acc_info[0] == acc_name:
            new_acc_info = acc_info[0] + ',' + acc_info[1] + ',' + balance + '\n'
    file.close()
    return new_acc_info

#将被修改的内容重新写入到文件中
def write_info(acc_name,new_acc_info):
    f = open('../data/atm_data.txt', 'r')
    atm_info = f.readlines()
    f.close()
    file = open('../data/atm_data.txt', 'w')
    for i in atm_info:
        acc_info = i.split(',')
        if acc_info[0] == acc_name:
            file.writelines(new_acc_info)
        else:
            file.writelines(i)
    file.close()

#更新文件中的余额
def update_balance(acc_name,balance):
    new_acc_info = read_info(acc_name, balance)
    write_info(acc_name, new_acc_info)

#增加账户余额
def add_balance(acc_name,balance,add_money):
    balance += add_money
    balance = str(balance)
    update_balance(acc_name, balance)
#6.存款；
def save_money(acc_name):
    smoney = int(input('请输入你要存款的金额'))
    balance = int(get_balance(acc_name))
    add_balance(acc_name, balance, smoney)
    return
# 减少账户余额
def sub_balance(acc_name,balance,sub_money):
    balance -= sub_money
    balance = str(balance)
    update_balance(acc_name, balance)

#7.取款
def draw_money(acc_name):
    while True:
        dmoney = int(input('请输入要取款的金额'))
        balance = int(get_balance(acc_name))
        if balance >= dmoney:
            sub_balance(acc_name, balance, dmoney)
            return
        else:
            print('余额不足，请重新输入')

#8.转账
def tran_money(acc_name):
    while True:
        other_acc = input('请输入对方账号')
        if check_acc(other_acc):
            tran_money = int(input('请输入转账金额：'))
            balance = int(get_balance(acc_name))
            if balance >= tran_money:
                sub_balance(acc_name, balance, tran_money)
                other_balance = int(get_balance(other_acc))
                add_balance(other_acc, other_balance, tran_money)
                break
            else:
                print('您的余额不足，不能转账')
        else:
            print('没有这个账号，请重新输入')

acc_name = show_start_menu()
show_main_menu(acc_name)
