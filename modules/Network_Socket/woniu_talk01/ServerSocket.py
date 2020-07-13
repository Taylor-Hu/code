#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/16 9:32
# software: PyCharm
# socket对象是标准库的一部分
import socket

class ServerSocket:

    # 对属性进行初始化，生成socket对象
    def __init__(self):
        self.server =socket.socket()

    # 连接客户端的方法
    def connect_client(self):
        # 绑定地址
        # self.server.bind(('192.168.2.125',8888))
        self.server.bind(('127.0.0.1', 8888))
        # 开始监听
        self.server.listen()
        print('聊天室已开启。。。')
        # 准备接收消息，处于阻塞状态
        while 1:  #保证一个客户端退出后仍然处于准备接收状态
            #chanel指从客户端接收的socket对象，address指客户端的ip和端口形成的元组
            chanel,address = self.server.accept()
            print('来自'+str(address)+'的大神进入了聊天室')
            send_msg = '欢迎'+str(address)+'来到蜗牛聊天室'
            # 将欢迎消息发送回给客户端，encode()默认为utf8
            chanel.send(send_msg.encode())
            # 进行消息的收发
            self.receive_send(chanel,address)

    # 收发消息的方法
    def receive_send(self,chanel,address):
        #接收从客户端发送的消息
        while 1:
            receive_msg = chanel.recv(1024).decode()
            if receive_msg != 'y':
                temp_msg = '来自【' + str(address) + '】的大神说：' + receive_msg
                print(temp_msg)
                chanel.send(temp_msg.encode())
            else:
                temp_msg = '来自【' + str(address) + '】的大神退出了聊天室'
                print(temp_msg)

                break

    # 销毁socket对象，回收资源.当当前类对象使用完毕后会自动调用
    # 析构方法
    def __del__(self):
        self.server.close()

if __name__ == '__main__':
    ServerSocket().connect_client()