#!/usr/bin/env python
#-*- coding:utf-8 -*-

import base64

# string = b'admin'
string = 'admin'
a = base64.b64encode(string.encode())
print(a.decode())   # YWRtaW4=

bstring = 'YWRtaW4='
a = base64.b64decode(bstring.encode())
print(a.decode())   # admin


