#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random
import time
# 卡号 密码 余额 账户 性别
account_info = [[1001, "123456", 1000, "root", "女"],
                [1002, "123456", 1500, "admin", "女"]] # 全局变量，用于存储所有的账户信息

def show_start_menu():
    print("*" * 30)
    print("1.登录 2.注册 3.退出".center(24, "*"))
    print("*" * 30)


def get_birthday(pid):
    birthday = pid[6:14]
    year = birthday[:4]
    month = birthday[4:6]
    day = birthday[6:8]
    birthday = year + "年" + month + "月" + day + "日"
    return birthday

def check_cardno(cardno):
    for i in account_info:
        if i[0] == cardno:
            accindex = account_info.index(i)
            return accindex
    else:
        return "False"

def get_cardno():
    while 1:
        cardno = random.randint(1000, 9999)  # 生成一个随机卡号
        if check_cardno(cardno)!="False":
            continue
        else:
            return cardno

# 检查密码是否是六位数字并且两次输入是否一致
def check_pwd():
    while 1:
        pwd = input("请输入你的密码：")
        conpwd = input("请在输入一次：")
        if (len(pwd) == 6) and (pwd.isdigit()) and (pwd == conpwd):
            return pwd
        else:
            print("输入不合理，请重新输入")


def regedit():
    rname = input("请输入你的姓名:")
    rsex = input("请输入你的性别:")
    rpid = input("请输入你的身份证号:")
    birthday = get_birthday(rpid)
    phone = input("请输入你的手机号:")
    cardno = get_cardno()
    password = check_pwd()
    balance = int(input("请输入存取金额："))
    acc_info = [cardno,password,balance,rname,rsex]
    account_info.append(acc_info)
    print("姓名：%s 性别：%s 生日：%s 手机号：%s 账号：%d 密码：%s 余额：%s"
          %(rname,rsex,birthday,phone,cardno,password,balance))

def check_login_cardno():
    err_count = 0
    while 1:
        cardno = int(input("请输入卡号："))            # 重要，字符串和数字比较会出现错误的
        if err_count < 3:
            if check_cardno(cardno) != "False":
                login_index = check_cardno(cardno)
                return login_index
            else:
                err_count += 1
                print("卡号输入错误，请重新输入：%d"%err_count)
        else:
            print("卡号错误超过三次，请退出：")
            break


def check_login_accpass(login_index):
    err_pwd = 0
    while 1:
        if err_pwd < 3:
            password = input("请输入登录密码：")
            if account_info[login_index][1] == password:
                print("登录成功")
                return
            else:
                err_pwd += 1
                print("密码输入不正确，请重新输入：")
        else:
            print("错误次数超过三次，已锁定该账户")
            exit("lock")

def login():
    login_index = check_login_cardno()

    check_login_accpass(login_index)
    return login_index


def get_balance(login_index):
    return account_info[login_index][2]

def query_balance(login_index):
    print("当前余额是：%d" %(get_balance(login_index)))

def save_money(login_index):
    smoney = int(input("请输入存款金额："))
    account_info[login_index][2] += smoney
    query_balance(login_index)

def make_draw_money(login_index, dmoney):
    if account_info[login_index][2] > dmoney:
        return True
    else:
        return False


def draw_money(login_index):
    while 1:
        dmoney = int(input("请输入取款金额："))
        if make_draw_money(login_index, dmoney):
            print("开始取款操作。。。")
            time.sleep(3)
            account_info[login_index][2] -= dmoney;
            query_balance(login_index)
            return
        else:
            print("余额不足，请重新输入：")


def make_tran_money(login_index, other_index):
    while 1:
        tmoney = int(input("请输入转账金额："))
        if make_draw_money(login_index, tmoney):
            print("开始转账。。。")
            time.sleep(3)
            account_info[login_index][2] -= tmoney
            account_info[other_index][2] += tmoney
            query_balance(login_index)
            query_balance(other_index)
            break
        else:
            print("余额不足，请重新输入：")


def tran_money(login_index):
    while 1:
        other_cardno = int(input("请输入转账的账户卡号："))
        if check_cardno(other_cardno) != "False":
            other_index = check_cardno(other_cardno)
            break
        else:
            print("账户不存在，请重新输入：")

    make_tran_money(login_index, other_index)


def check_login_accpass(login_index):
    err_pwd = 0
    while 1:
        if err_pwd < 3:
            password = input("请输入登录密码：")
            if account_info[login_index][1] == password:
                print("登录成功")
                return
            else:
                err_pwd += 1
                print("密码输入不正确，请重新输入：")
        else:
            print("错误次数超过三次，已锁定该账户")
            exit("lock")


def modify_pwd(login_index):
    err_pwd = 0
    while 1:
        if err_pwd < 3:
            password = input("请输入登录密码：")
            if account_info[login_index][1] == password:
                conpass = input("请输入需要修改的密码：")
                account_info[login_index][1] = conpass
                print("密码修改正确！")
                return
            else:
                err_pwd += 1
                print("密码输入不正确，请重新输入：")
        else:
            print("错误次数超过三次，已锁定该账户")
            exit("lock")






