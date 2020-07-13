#!/usr/bin/env python
# -*- coding:utf-8 -*-
from atmV6_obj.manger.account_manager import AccountManager
from atmV6_obj.manger.admin_manager import AdminManager
from atmV6_obj.util.utility import ConnUtil
from atmV6_obj.view.admin_menu import AdminView
from atmV6_obj.view.comm_menu import comm_regedit

class menu_view:

    def start_menu(self):
        while 1:
            choice = int(input("***1.注册 2.登录 3.管理员入口***"))
            if choice == 1:
                self.__regedit()
            elif choice == 2:
                self.__login()
            elif choice == 3:
                self.__show_admin()
            else:
                break

    def __regedit(self):
        comm_regedit()

    def __login(self):
        while 1:
            accno = input("请输入登录账号：")
            if AccountManager().check_accno(accno):
                if AdminManager().admin_lock_status(accno):
                    print("该账户已被锁定，请联系管理员")
                else:
                    break
            else:
                print("账户不存在，请重新输入")

        err_count = 0
        while 1:
            if err_count < 3:
                password = input("请输入密码：")
                sql = "select password from account where number='%s'"%(accno)
                result = ConnUtil().db_dql(sql)
                if result[0][0] == password:
                    print("密码输入正确，登录成功")
                    break
                else:
                    print("密码输入错误，请重新输入")
                    err_count += 1
            else:
                print("密码错误次数太多，该账户已被锁定")
                AdminManager().admin_lock_account(accno)
                exit("Lock, exit")


    def __show_admin(self):
        admin_no = input("请输入管理员账号：")
        admin_pass = input("输入管理员密码：")

        if admin_no == "1001" and admin_pass == "123456":
            print("欢迎您管理员！")
            self.__show_manager_menu()
        else:
            exit("bye")

    def __show_manager_menu(self):

        while 1:
            choice = int(input("1.add 2.modify 3.delete 4.query 5.account list 6.lock&unlock"))
            if choice == 1:
                AdminView().add_account()
            elif choice == 2:
                AdminView().modify_account()
            elif choice == 3:
                AdminView().delete_account()
            elif choice == 4:
                AdminView().query_account()
            elif choice == 5:
                AdminView().list_account()
            elif choice == 6:
                AdminView().lock_unlock_account()
            else:
                pass




