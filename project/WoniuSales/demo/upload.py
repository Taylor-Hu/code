import http.client

# conn = http.client.HTTPConnection(host='localhost', port=8088)
conn = http.client.HTTPConnection(host='192.168.80.128', port=8080)

boundary = '----WebKitFormBoundaryYB8ArGHkuNr10lai'
header = {'Content-Type':'multipart/form-data; boundary=%s' % boundary,
          'Cookie':'JSESSIONID=CC7A47962D7175EBEA8EA0A2427FB563'}

body = ''
body += '--%s\r\n' % boundary
body += 'Content-Disposition: form-data; name="batchname"\r\n'
body += '\r\n'
body += 'GB20190503\r\n'
body += '--%s\r\n' % boundary
body += 'Content-Disposition: form-data; name="batchfile"; filename="SaleList-20171020-Test.xls"\r\n'
body += 'Content-Type: application/vnd.ms-excel\r\n'
body += '\r\n'
body = body.encode() + open('D:/Other/SaleList-20171020-Test.xls', 'rb').read()
body += '\r\n'.encode()
body += ('--%s--' % boundary).encode()

conn.request(method='POST', url='/woniusales/goods/upload', body=body, headers=header)

resp = conn.getresponse().read().decode()
print(resp)
