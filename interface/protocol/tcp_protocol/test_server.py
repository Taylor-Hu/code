#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket, subprocess, os

server = socket.socket()
server.bind(('127.0.0.1',6000))     # 绑定IP和端口
server.listen()
chanel, address = server.accept()   # 接受连接请求，返回的chanel就是与某客户端的连接通道, address是对应的客户端的地址
while True:
    msg_recv = chanel.recv(1024).decode()
    print(msg_recv)
    chanel.send(('来自服务器的回复：' + msg_recv).encode())

    if msg_recv == 'quit':
        chanel.close()
        break

    if str(msg_recv).startswith('@'):
        print("这是在私聊.")

    if str(msg_recv).startswith('MM##'):
        cmd = msg_recv.split('##')[1]
        result = os.popen(cmd).read()
        chanel.send(result.encode())
