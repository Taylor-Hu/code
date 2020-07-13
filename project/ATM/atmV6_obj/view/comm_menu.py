#!/usr/bin/env python
#-*- coding:utf-8 -*-
from atmV6_obj.manger.account_manager import AccountManager
from atmV6_obj.util.utility import ConnUtil


def comm_regedit():
    while 1:
        accno = input("请输入卡号：")
        if AccountManager().check_accno(accno):
            print("该卡号已存在，请重新输入")
        else:
            break

    while 1:
        accpass = input("请输入密码：")
        conpass = input("请输入确认密码：")
        if AccountManager().check_pass(accpass, conpass):
            break
        else:
            print("密码输入错误，请重新输入")

    while 1:
        accbalance = float(input("请输入余额："))
        if AccountManager().check_accbalance(accbalance):
            break
        else:
            print("输入余额有误，请重新输入")

    while 1:
        realname = input("请输入姓名：")
        if AccountManager().check_realname(realname):
            break
        else:
            print("输入姓名有误，请重新输入")

    while 1:
        tel = input("请输入电话号码：")
        if AccountManager().check_tel(tel):
            break
        else:
            print("输入电话号码有误，请重新输入")

    # 加入到数据库
    sql = "insert into account values ('%s', '%s', '%f', '%s', '%s', %d)" % (
    accno, accpass, accbalance, realname, tel, 0)
    ConnUtil().db_dml(sql)
    print("已成功添加账号")
    # print("编号：%s 密码：%s 余额：%f 姓名：%s 电话号码：%s"%(accno, accpass, accbalance, realname, tel))