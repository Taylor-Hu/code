#!/usr/bin/env python
#-*- coding:utf-8 -*-

#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 事件驱动，多线程
import threading
import websocket, time

def when_open(ws):
    print("建立连接")

    def run():
        while True:
            msg = input("请输入内容:")
            ws.send(msg)
            # if msg == 'quit':
            #     ws.close()
            time.sleep(1)   # 延时一下，让主线程可以when_message收到消息可以打印出来，要不然input一直阻塞在那里
            if msg == 'quit':
                ws.close()

    threading.Thread(target=run).start()    # close的时候，连接关闭了，但是线程还在运行，然后又向服务器发消息的时候就会报错

# on_message has 2 arguments.
def when_message(ws, message):
    print("收到消息" + message)

def when_close(ws):
    print("连接关闭")

def when_error(ws, exception):
    print("通信出错" + exception)


# 这里的地址和端口号要一一对应 ws://echo.websocket.org是网上websocket服务器的网址
# ws = websocket.WebSocketApp(url='ws://echo.websocket.org',
ws = websocket.WebSocketApp(url='ws://192.168.80.128:8888',
                            on_open=when_open,
                            on_message=when_message,
                            on_close=when_close,
                            on_error=when_error)

# ws.close()   代码不会被运行
ws.run_forever()
# ws.close()   代码不会被运行
















