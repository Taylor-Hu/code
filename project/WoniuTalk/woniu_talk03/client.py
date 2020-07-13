#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 实现群聊的功能

import socket
import threading

class ClientSocket:

    def __init__(self, ip, port):
        self.client_socket = socket.socket()
        self.client_socket.connect((ip, port))

    def start_menu(self):
        while 1:
            choice = int(input("请输入你的选择：1.登录  2.注册"))
            if choice == 1:
                self.user_login()
            elif choice == 2:
                self.user_regedit()
            else:
                return

    def user_regedit(self):
        while 1:
            uname = input("请输入注册账号：")
            self.client_socket.send(uname.encode("UTF-8"))
            msg = self.client_socket.recv(1024).decode("UTF-8")
            if msg == "该账号已被占用，请重新输入":
                print(msg)
                continue
            else:
                break

        while 1:
            upass = input("请输入注册密码：")
            self.client_socket.send(upass.encode("UTF-8"))
            msg = self.client_socket.recv(1024).decode("UTF-8")
            if msg == "密码至少输入三位":
                print(msg)
                continue
            else:
                break

        msg = self.client_socket.recv(1024).decode()
        print(msg)


    def user_login(self):
        pass

    def client_service(self):
        welcome_msg = self.client_socket.recv(1024).decode("UTF-8")
        print(welcome_msg)

        t1 = threading.Thread(target=self.__recv_thread)
        t2 = threading.Thread(target=self.__send_thread)
        t1.start()
        t2.start()

    def __send_thread(self):
        while 1:
            str = input("请输入你想说的话：")
            if str == "quit":
                tip = input("确定要退出吗？(y/n)")
                self.client_socket.send(tip.encode("UTF-8"))
                if tip == 'y':
                    break
            else:
                self.client_socket.send(str.encode("UTF-8"))

    def __recv_thread(self):
        while 1:
            msg = self.client_socket.recv(1024).decode("UTF-8")
            if msg == "LEAVE":
                break
            else:
                print(msg)


    def __delete__(self, instance):
        self.client_socket.close()

if __name__ == '__main__':

   ClientSocket("localhost", 8888).start_menu()

