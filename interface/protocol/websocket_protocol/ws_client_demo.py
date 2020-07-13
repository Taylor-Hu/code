#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 连接网上websocket服务器

import websocket

ws = websocket.create_connection('ws://echo.websocket.org')    # websocket服务器网址
ws.send('你好，websocket')
# print(ws.recv())  # 如果没有收到消息会一直阻塞在这里
if ws.recv() == '你好，websocket':
    print("测试成功")
else:
    print("测试失败")
ws.close()
