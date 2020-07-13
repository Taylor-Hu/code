#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 实现群聊的功能
# 实现注册、登录的功能

# 扩展功能：实现私聊 @name msg
# 需要完善的地方：
# 1. 服务器异常挂了客户端也挂了
# 2. 私聊发送的信息@name hello world, 只能接收到hello, 空格后的内容被忽略了；
# 3. 代码有点冗余

import socket
import threading

from woniu_talk03.db_manager import DB_Manager


class ServerSocket:

    def __init__(self, ip, port):
        self.nick_name_list = []
        self.ser_socket = socket.socket()
        self.ser_socket.bind((ip, port))
        self.ser_socket.listen(5)
        print("开启监听，等待客户端连接。。。")

    def serv_server(self):
        while 1:
            channel, addr = self.ser_socket.accept()

            self.confirm_regedit(channel)

            # 要求客户端输入昵称，方便接下来的私聊
            str = "欢迎来自" + addr[0] + "的朋友进入聊天室, 请输入昵称："
            channel.send(str.encode("UTF-8"))

            # 将客户端的昵称、channel保存在列表中
            nickname = channel.recv(1024).decode("UTF-8")
            channel_info = (channel, nickname)
            self.nick_name_list.append(channel_info)

            # 群发消息，欢迎客户端进入服务器
            str = "欢迎" + nickname + "进入了聊天室"
            for info in self.nick_name_list:
                info[0].send(str.encode("UTF-8"))

            # 创建线程，接收和发送消息
            t1 = threading.Thread(target=self.__server_recv_send, args=(channel, nickname))
            t1.start()

    def check_name(self, channel):
        while 1:
            uname = channel.recv(1024).decode("UTF-8")
            print(uname)
            # 表的名字是
            sql = "select uname from user where uname='%s'"%(uname)
            result = DB_Manager().db_dql(sql)
            if result:
                channel.send("该账号已被占用，请重新输入".encode("UTF-8"))
                continue
            else:
                channel.send("该账号可以使用".encode("UTF-8"))
                return uname

    def check_pass(self, channel):
        while 1:
            upass = channel.recv(1024).decode()
            if len(upass) >= 3:
                channel.send("密码可用".encode())
                return upass
            else:
                channel.send("密码至少输入三位".encode())
                continue

    def confirm_regedit(self, channel):
        uname = self.check_name(channel)
        upass = self.check_pass(channel)

        sql = "insert into user values('%s','%s')"%(uname, upass)
        DB_Manager().db_dml(sql)
        channel.send("注册成功,请重新登录".encode())

    def __server_recv_send(self, channel, nickname):
        while 1:
            try:
                str = channel.recv(1024).decode("UTF-8")

                if str[0] == '@':   # 处理私聊信息
                    print("私聊信息：" + str)
                    self.handle_private_chat(nickname, str)
                else:
                    if str == 'y':
                        channel.send("LEAVE".encode("UTF-8"))   # 发送信息“LEAVE”，客户端接收这条信息后，可以退出，避免阻塞等待
                        quit_msg = "【" + nickname + "】说要离开聊天室"
                        print(str)
                        for info in self.nick_name_list:
                            info[0].send(quit_msg.encode("UTF-8"))
                    else:
                        str = "【" + nickname + "】说" + str   # 群发消息
                        print(str)
                        for info in self.nick_name_list:
                            info[0].send(str.encode("UTF-8"))
            except:
                break

    # 私聊：根据对方昵称获取对方的channel
    def get_channel(self, private_name):

        for info in self.nick_name_list:
            if info[1] == private_name:
                return info[0]
        else:
            return None

    # 私聊：处理私聊函数
    def handle_private_chat(self, nickname, str):
        #str.find(" ")  str.index(" ") //找到子串的下标
        msg = str.split(" ")
        private_name = msg[0][1:]   # 获取私聊的名称
        private_msg = msg[1]        # 获取私聊的信息
        # print("private_name = " + private_name + "private_msg: " + private_msg)
        private_channel = self.get_channel(private_name)
        if private_channel != None:
            private_msg = "【" + nickname + "】对你悄悄说" + private_msg
            private_channel.send(private_msg.encode("UTF-8"))
        else:
            str = "【" + nickname + "】说" + str
            print(str)
            for info in self.nick_name_list:
                info[0].send(str.encode("UTF-8"))

    def __del__(self):
        self.ser_socket.close()

if __name__ == '__main__':
    ServerSocket("localhost", 8888).serv_server()
