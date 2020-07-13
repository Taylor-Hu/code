#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/12/16 12:04
# software: PyCharm
'''
功能扩展：
1.增加用户注册和登录功能；
2.对用户信息进行持久化；
3.分组聊天；
'''
import socket, threading


class ServerSocket:

    def __init__(self):
        self.server = socket.socket()
        self.chanel_list = []  # [[name1,chanel1],[name2,chanel2],[....],] 二维列表[{name:socket},{}]

    # 在列表中遍历查找是否有重复项，如果有返回false，如果没有则返回True
    def check_username(self, username):
        # 列表不为空
        if len(self.chanel_list) != 0:
            for i in self.chanel_list:
                if i[0] == username:
                    return i[1]
            else:
                return None
        else:
            return None

    def connect_lient(self):
        self.server.bind(('127.0.0.1', 8001))
        self.server.listen()
        print('聊天服务已启动。。。')
        while 1:
            chanel, address = self.server.accept()
            warn_info = '欢迎' + str(address) + '来到蜗牛聊天室,请输入您的昵称'
            print(warn_info)
            chanel.send(warn_info.encode())
            # 从客户端获取用户的昵称
            while 1:
                username = chanel.recv(1024).decode()
                user_chanel = self.check_username(username)
                if user_chanel != None:
                    print('昵称已被占用，请重新输入')
                    chanel.send('昵称已被占用，请重新输入'.encode())
                else:
                    break
            # 将用户昵称和对象生成一个列表元素
            temp_list = [username, chanel]
            # 作为整体添加入chanel_list中
            self.chanel_list.append(temp_list)
            welcome_info = '欢迎来自' + str(address) + '的白金大神【' + username + '】来到聊天室'
            for i in self.chanel_list:
                i[1].send(welcome_info.encode())

            threading.Thread(target=self.receive_send, args=(username, chanel, address)).start()

    def receive_send(self, username, chanel, address):
        while 1:
            receive_msg = chanel.recv(1024).decode()
            if receive_msg != 'y':
                # 私聊：判断字符串是否以@符号开始,并且该字符串中间有空格 @author xxx xx xx
                if str(receive_msg).startswith('@') and str(receive_msg).find(' ') != -1:
                    private_list = str(receive_msg).split(' ')
                    # 获取要发送的对方的名字
                    other_name = private_list[0][1:]
                    # 获取要发送的信息
                    private_msg = ''
                    for i in range(1, len(private_list)):
                        private_msg += private_list[i]

                    print(private_msg)

                    other_chanel = self.check_username(other_name)
                    if other_chanel != None:
                        private_other = '【' + username + '】悄悄对你说：' + private_msg
                        private_self = '你悄悄地对【' + other_name + '】说：' + private_msg
                        print(private_other)
                        print(private_self)
                        other_chanel.send(private_other.encode())
                        chanel.send(private_self.encode())
                    else:
                        chanel.send('查无此人'.encode())
                else:
                    send_msg = '【' + username + '】说：' + receive_msg
                    print(send_msg)
                    for i in self.chanel_list:
                        i[1].send(send_msg.encode())
            else:
                temp_msg = '来自【' + str(address) + '】的大神退出了聊天室'
                print(temp_msg)
                chanel.send('quit'.encode())
                temp_list = [username, chanel]
                self.chanel_list.remove(temp_list)
                for i in self.chanel_list:
                    i[1].send(temp_msg.encode())
                break


def __del__(self):
    self.server.close()


if __name__ == '__main__':
    ServerSocket().connect_lient()
