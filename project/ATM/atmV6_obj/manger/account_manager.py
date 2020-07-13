#!/usr/bin/env python
#-*- coding:utf-8 -*-
from atmV6_obj.util.utility import ConnUtil

class AccountManager:

    def check_accno(self, accno):
        sql = "select * from account where number='%s'"%(accno)
        result = ConnUtil().db_dql(sql)
        for info in result:
            if info[0] == accno:
                return True
        else:
            return False

    def check_pass(self, pwd, con_pwd):
        if len(pwd) > 5 and pwd == con_pwd:
            return True
        else:
            return False

    def check_accbalance(self, accbalance):
        if accbalance >= 0:
            return True
        else:
            return False

    def check_realname(self, realname):
        if len(realname) > 2 and len(realname) < 20:
            return True
        else:
            return False

    def check_tel(self, tel):
        if len(tel) == 11:
            return True
        else:
            return False

