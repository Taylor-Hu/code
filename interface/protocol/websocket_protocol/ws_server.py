#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import time


# 创建一个处理类，用于处理连接，接收和发送消息以及关闭服务器
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("服务器成功...")
        self.write_message("你已经与服务器建立连接.")
        # for i in range(10):
        #     now = time.strftime("%Y-%m-%d %H:%M:%S")
        #     self.write_message(now)
        #     time.sleep(1)


    def on_message(self, message):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        self.write_message(u"在" + now + " 你说: " + message)
        # 把消息给保存到数据库。。。。。。
        print("客户端说：" + message)


    def on_close(self):
        print("服务器关闭...")


class Test:
    pass


# 定义处理路径，当用户访问ws://localhost:8888/根目录时，交由WebSocketHandler处理
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r'/', WebSocketHandler)]
        tornado.web.Application.__init__(self, handlers)


# 实例化Application对象并启动WebSocket服务器，绑定端口号8888
if __name__ == '__main__':
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


















