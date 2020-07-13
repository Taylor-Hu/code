# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         demo01
# Description:  
# Author:       Administrator
# Date:         2018/12/14
#-------------------------------------------------------------------------------

import socket
s = socket.socket()
s.bind(('127.0.0.1',8888))
s.listen(5)
c,address = s.accept()
c.send('链接成功！'.encode('utf8'))
while 1:
	content = c.recv(1024).decode('utf8')
	if content == 'quit':
		break
	print('['+address[0]+' '+str(address[1])+']'+content)
	c.send(content.encode('utf8'))