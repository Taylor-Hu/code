# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         demo02
# Description:  
# Author:       Administrator
# Date:         2018/12/14
#-------------------------------------------------------------------------------
import socket
s = socket.socket()
s.connect(('127.0.0.1',8888))
content = s.recv(1024).decode('utf8')
print(content)
while 1:
	str1 = input('请输入')
	s.send(str1.encode('utf8'))
	if str1 == 'quit':
		break
	str1 = s.recv(1024).decode('utf-8')
	print(str1)
s.close()