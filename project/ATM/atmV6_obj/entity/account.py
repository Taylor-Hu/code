#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Account:

    __accno = ""
    __accpass = ""
    __accbalance = ""
    __realname = ""
    __tel = ""
    __flag = 0

    def __int__(self,accno,accpass,accbalance,realname,tel,flag):
        self.__accno = accno
        self.__accpass = accpass
        self.__accbalance = accbalance
        self.__realname = realname
        self.__tel = tel
        self.__flag = flag

    def set_accno(self,accno):
        self.__accno = accno

    def get_accno(self):
        return self.__accno

    def set_accpass(self,accpass):
        self.__accpass = accpass

    def get_accpass(self):
        return self.__accpass

    def set_accbalance(self,accbalance):
        self.__accbalance = accbalance

    def get_accbalance(self):
        return self.__accbalance

    def set_realname(self,realname):
        self.__realname = realname

    def get_realname(self):
        return self.__realname

    def set_tel(self,tel):
        self.__tel = tel

    def get_tel(self):
        return self.__tel

    def set_flag(self,flag):
        self.__flag = flag

    def get_flag(self):
        return self.__flag

    def __str__(self):
        return "%s\t%s\t%f\t%s\t%s\t%d"%(self.__accno,self.__accpass,self.__accbalance,self.__realname,self.__tel,self.__flag)




















