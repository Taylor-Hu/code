#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/16 9:33
# software: PyCharm

import socket

class ClientSocket:

    def __init__(self):
        self.client = socket.socket()

    def conn_server(self):
        # self.client.connect(('192.168.2.125',8888))
        self.client.connect(('127.0.0.1', 8888))
        # 接收从服务端来的欢迎消息
        welcome_info = self.client.recv(1024).decode()
        print(welcome_info)
        self.send_receive()

    def send_receive(self):
        while 1:
            msg = input('请输入您要说的话：')
            #如果没有输入quit，就进行消息发送
            if msg != 'quit':
                # 发送消息至服务器
                self.client.send(msg.encode())
                # 接收从服务器的反馈
                confirm_msg = self.client.recv(1024).decode()
                print(confirm_msg)
            else:
                choice = input('您真的要退出吗？（y/n）')
                if choice.lower() == 'y':
                    self.client.send('y'.encode())
                    print('您退出了蜗牛聊天室')
                    break


    def __del__(self):
        self.client.close()

if __name__ == '__main__':
    ClientSocket().conn_server()

