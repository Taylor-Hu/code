#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time

account_info=[{"cardno":1001, "password":"123456", "balance":1500},
              {"cardno":1002, "password":"123456", "balance":1000}]

def show_start_menu():
    print("*" * 30)
    print("1.登录 2.注册 3.退出".center(24, "*"))
    print("*" * 30)

def check_cardno(cardno):
    for accinfo in account_info:
        if accinfo.get("cardno") == cardno:
            accindex = account_info.index(accinfo)
            return accindex
    else:
        return "False"

def regedit():

    while 1:
        cardno = int(input("请输入要注册的卡号："))
        if check_cardno(cardno)!="False":
            print("该卡号已被占用，请重新输入：")
        else:
            break

    pwd = input("请输入注册密码：")
    balance = int(input("请输入注册金额："))
    accinfo = {"cardno":cardno, "password":pwd, "balance":balance}
    account_info.append(accinfo)
    print("注册成功！卡号：%d 密码：%s 注册金额：%d" %(cardno, pwd, balance))


def check_login_cardno():
    err_cardno = 0
    while 1:
        if err_cardno < 3:
            cardno = int(input("请输入卡号："))
            if check_cardno(cardno)!="False":
                acc_index = check_cardno(cardno)
                return acc_index
            else:
                err_cardno += 1
                print("卡号输入错误，请重新输入：")
        else:
            print("卡号错误次数超过三次，退出登录")
            exit("bye")

def check_login_pwd(login_index):
    err_pwd = 0
    while 1:
        if err_pwd < 3:
            pwd = input("请输入密码：")
            if pwd == account_info[login_index].get("password"):
                return
            else:
                err_pwd += 1
                print("密码输入错误，请重新输入：")
        else:
            print("密码错误次数超过三次，锁定账户：")
            exit("lock")


def login():
    login_index = check_login_cardno()
    check_login_pwd(login_index)
    return login_index

def get_balance(login_index):
    return account_info[login_index].get("balance")

def query_balance(login_index):
    print("当前账户的余额：%d" %(get_balance(login_index)))

def save_money(login_index):
    smoney = int(input("请输入存款金额："))
    acc_money = get_balance(login_index)
    acc_money += smoney
    account_info[login_index]["balance"] = acc_money
    query_balance(login_index)


def make_draw_money(login_index, dmoney):
    if account_info[login_index].get("balance") > dmoney:
        return True
    else:
        return False


def draw_money(login_index):
    while 1:
        dmoney = int(input("请输入取款金额："))
        if make_draw_money(login_index, dmoney):
            print("开始取款操作。。。")
            time.sleep(3)
            acc_money = get_balance(login_index)
            acc_money -= dmoney
            account_info[login_index]["balance"] = acc_money
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
            account_info[login_index]["balance"] = account_info[login_index].get("balance") - tmoney
            account_info[other_index]["balance"] = account_info[other_index].get("balance") + tmoney
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

    # 调用执行转账的函数
    make_tran_money(login_index, other_index)


def modify_pwd(login_index):
    err_pwd = 0
    while 1:
        if err_pwd < 3:
            password = input("请输入登录密码：")
            if account_info[login_index].get("password") == password:
                conpass = input("请输入需要修改的密码：")
                account_info[login_index]["password"] = conpass
                print("密码修改正确！")
                return
            else:
                err_pwd += 1
                print("密码输入不正确，请重新输入：")
        else:
            print("错误次数超过三次，已锁定该账户")
            exit("lock")














