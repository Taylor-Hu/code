#!/usr/bin/env python
#-*- coding:utf-8 -*-
from atmV6_obj.manger.account_manager import AccountManager
from atmV6_obj.manger.admin_manager import AdminManager
from atmV6_obj.util.utility import ConnUtil
from atmV6_obj.view.comm_menu import comm_regedit


class AdminView:

    def add_account(self):
        comm_regedit()

    def modify_account(self):
        pass

    def delete_account(self):
        accno = input("请输入你要删除的账号名：")
        sql = "delete from account where number='%s'"%(accno)
        result = ConnUtil().db_dml(sql)
        if result > 0:
            print("成功删除账号")
        else:
            print("该账号信息不存在")

    def query_account(self):
        accno = input("请输入你要查询的账号：")
        sql = "select * from account where number='%s'"%(accno)
        result = ConnUtil().db_dql(sql)
        if len(result)>0:
            for info in result:
                for i in info:
                    print("%s"%i, end='\t')
        else:
            print("该账号信息不存在")

    def list_account(self):
        sql = "select * from account"
        result = ConnUtil().db_dql(sql)
        if len(result) > 0:
            for info in result:
                for i in info:
                    print("%s" % i, end='\t')
                print("")
        else:
            print("数据库为空")

    def lock_unlock_account(self):
        accno = input("请输入你要操作的账户：")
        if AccountManager().check_accno(accno):
            if AdminManager().admin_lock_status(accno):
                choice = input("当前状态已锁定，需要执行解锁操作吗？（y/n）")
                if choice == 'y':
                    AdminManager().admin_unlock_account(accno)
                    print("解锁成功")
                else:
                    print("退出操作")
            else:
                choice = input("当前状态未锁定，需要执行加锁操作吗？（y/n）")
                if choice == 'y':
                    AdminManager().admin_lock_account(accno)
                    print("加锁成功")
                else:
                    print("退出操作")
        else:
            print("该账户不存在")

