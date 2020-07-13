#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/16 10:48
# software: PyCharm

import socket,threading

class ClientSocket:

    def __init__(self):
        self.client = socket.socket()

    def conn_server(self):
        # self.client.connect(('192.168.2.125',8888))
        self.client.connect(('127.0.0.1', 8888))
        welcome_info = self.client.recv(1024).decode()
        print(welcome_info)
        # 将收、发消息分开成两个线程，可以在收的同时发
        threading.Thread(target=self.receive).start()
        threading.Thread(target=self.send).start()


    # 线程方法，专用于接收消息
    def receive(self):
        while 1:
            try:
                server_msg = self.client.recv(1024).decode()
                print(server_msg)
            except:
                print('客户端结束')
                break

    # 线程方法，专用于发送消息
    def send(self):
        while 1:
            msg = input('请输入您想说的话：')
            if msg != 'quit':
                self.client.send(msg.encode())
            else:
                choice = input('您真的要退出聊天室吗？(y/n)')
                if choice == 'y':
                    self.client.send('y'.encode())
                    print('您退出了聊天室')
                    break


    def __del__(self):
        self.client.close()

if __name__ == '__main__':
    ClientSocket().conn_server()