#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/16 12:04
# software: PyCharm

import socket,threading

class ClientSocket:

    def __init__(self):
        self.client = socket.socket()

    def conn_server(self):
        self.client.connect(('127.0.0.1',8001))
        warn_msg = self.client.recv(1024).decode()
        print(warn_msg)
        username = input()
        self.client.send(username.encode())


        # 将收、发消息分开成两个线程，可以在收的同时发

        threading.Thread(target=self.send).start()
        threading.Thread(target=self.receive).start()

    # 线程方法，专用于接收消息
    def receive(self):
        while 1:
            server_msg = self.client.recv(1024).decode()
            if server_msg != 'quit':
                print(server_msg)
            else:
                print(server_msg)
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
