#!/usr/bin/env python
#-*- coding:utf-8 -*-
from atmV6_obj.util.utility import ConnUtil

class AdminManager:

    def admin_add_account(self):
        pass

    def admin_modify_account(self):
        pass

    def admin_delete_account(self):
        pass

    def admin_query_account(self):
        pass

    def admin_list_account(self):
        pass

    def admin_lock_account(self, accno):
        sql = "update account set flag=%d where number='%s'" % (1, accno)
        ConnUtil().db_dml(sql)

    def admin_unlock_account(self, accno):
        sql = "update account set flag=%d where number='%s'" % (0, accno)
        ConnUtil().db_dml(sql)

    def admin_lock_status(self, accno):
        sql = "select flag from account where number='%s'" % (accno)
        result = ConnUtil().db_dql(sql)
        # print(result)   # ((0,),)
        if result[0][0] == 1:
            return True
        else:
            return False


