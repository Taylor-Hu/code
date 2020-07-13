#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/16 10:48
# software: PyCharm
import socket, threading


class ServerSocket:

    def __init__(self):
        self.server = socket.socket()
        # chanel_list所有客户端对象的列表
        self.chanel_list = []

    def connect_client(self):
        # self.server.bind(('192.168.2.125', 8888))
        self.server.bind(('127.0.0.1', 8888))
        self.server.listen()
        print('聊天服务已启动。。。')
        while 1:
            chanel, address = self.server.accept()
            welcome_info = '欢迎' + str(address) + '来到蜗牛聊天室'
            self.chanel_list.append(chanel)
            print(welcome_info)
            # 将欢迎消息群发给所有用户
            for i in self.chanel_list:
                i.send(welcome_info.encode())
            # 创建线程对象，其中线程方法是收发消息，参数是chanel和address
            threading.Thread(target=self.receive_send, args=(chanel, address)).start()

    def receive_send(self, chanel, address):
        while 1:

            receive_msg = chanel.recv(1024).decode()

            if receive_msg != 'y':
                temp_msg = '来自【' + str(address) + '】的大神说：' + receive_msg
                print(temp_msg)
                # 将正常消息群发给所有的用户
                for i in self.chanel_list:
                    i.send(temp_msg.encode())
            else:
                temp_msg = '来自【' + str(address) + '】的大神退出了聊天室'
                print(temp_msg)
                # 移除当前退出的用户
                self.chanel_list.remove(chanel)
                # 将退出消息发送给剩下的用户
                for i in self.chanel_list:
                    i.send(temp_msg.encode())
                break

    def __del__(self):
        self.server.close()


if __name__ == '__main__':
    ServerSocket().connect_client()
