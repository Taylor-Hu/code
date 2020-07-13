#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 显示开始菜单
def StartMenu():
    print("*" * 30)
    print("1.登录 2.注册 3.退出".center(30, '*'))
    print("*" * 30)
    return

# 1.1 检测注册的卡号是否重复
def check_cardno(acc_card):
    file = open("..//data//account_data.py", "r")
    # 读取当前文件的所有内容，会返回一个列表
    acc_info = file.readlines()
    for account in acc_info:
        # 找到第一个逗号的下标
        acc_index = account.find(',')
        # print("acc_index = %d %s"%(acc_index,account))
        # 通过切片的方式获取卡号[:acc_index]，默认从0下标开始
        if acc_card == account[:acc_index]:
            file.close()
            return account  # 返回一个字符串
    else:
        file.close()
        return "False"


# 1. 注册
def regiter():
    while 1:
        cardno = input("请输入注册的卡号：")
        if check_cardno(cardno)!="False":
            input("卡号重复，请重新输入")
        else:
            break
    pwd = input("请输入密码：")
    balance = input("请输入存款金额：")
    account_info = '\n' + cardno + ',' + pwd + ',' + balance
    file = open("..//data//account_data.py", "a")
    file.writelines(account_info)
    print("注册成功")
    file.close()
    print("卡号：%s 密码：%s 存款金额：%s\n"%(cardno,pwd,balance))

# 2.1 检测登录卡号是否正确
def check_login_cno():
    cno_errcount = 0
    while 1:
        if cno_errcount<3:
            login_cno = input("请输入您登录的卡号：")
            login_info = check_cardno(login_cno)
            if login_info!='False':
                print("卡号输入正确")
                return login_info
            else:
                cno_errcount += 1
                print("卡号输入错误，请重新输入")
        else:
            print("卡号错误三次，退出")
            exit("bye")

# 2.2 检测登录密码
def check_login_pwd(login_info):
    logpwd_errcount = 0
    while 1:
        if logpwd_errcount < 3:
            login_pwd = input("请输入登录密码：")
            login_str = login_info.split(",")
            if login_str[1] == login_pwd:
                print("密码输入正确")
                break
            else:
                print("密码输入错误，请重新输入")
                logpwd_errcount += 1
        else:
            print("密码错误三次，退出")
            # acc_lock()
            exit("bye")

# 2. 登录
def login():
    while 1:
        # 验证登录名
        login_info = check_login_cno()

        # 验证密码
        check_login_pwd(login_info)
        return login_info

#######################################业务部分###########################################
# 得到余额（逻辑部分）
def get_balance(login_info):
    balance = login_info.split(",")
    balance = int(balance[2].split("\n")[0])  # 因为获取的字符串末尾有一个换行符
    return balance

# 查询余额（业务部分）
def query_balance(login_info):
    print("当前余额是%s元" %(get_balance(login_info)))

# 存款操作（逻辑部分）
def update_balance(login_info, balance):
    file = open("..//data//account_data.py", "r")
    # 获取多行内容，返回一个列表
    contents = file.readlines()
    # print("contents=%s" % (contents))

    temp_contents = []
    for content in contents:
        c = content.split(",")
        if login_info == content:
            c[2] = str(balance)
            content = c[0] + "," + c[1] + "," + c[2] + "\n"
            # print("c=%s content=%s" % (c, content))
            temp_contents.append(content)
        else:
            content = c[0] + "," + c[1] + "," + c[2] + "\n"
            temp_contents.append(content)

    temp_info = ""

    for info in temp_contents:
        temp_info += info
    file.close()
    file = open("..//data//account_data.py", "w")
    # 必须将contents转成字符串，contents是列表类型
    file.writelines(temp_info)
    file.close()

# 存款
def save_money(login_info):
    smoney = int(input("请输入存取的金额："))
    balance = get_balance(login_info)
    balance += smoney
    update_balance(login_info, balance)
    query_balance(login_info)


def draw_money(login_info):
    pass

def tran_money(login_info):
    pass

def modify_pwd(login_info):
    pass








