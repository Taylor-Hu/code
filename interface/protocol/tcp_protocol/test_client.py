#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket

client = socket.socket()  # 实例化socket对象，默认不带构造参数，则使用的是TCP连接
client = socket.socket(type=socket.SOCK_STREAM)
# client = socket.socket(type=socket.SOCK_DGRAM)  # 使用UDP协议
client.connect(('127.0.0.1', 6000))
while True:
    msg_send = input("请输入你的消息：")
    client.send(msg_send.encode())
    msg_recv = client.recv(1024).decode()
    print(msg_recv)

client.close()
