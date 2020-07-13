import requests,base64,json

# 基于kodcloud api测试
# Token的应用

class kod():
    def __init__(self):
        self.session = requests.session()

    def login(self):
        resp_login=self.session.get(url='http://192.168.80.128/kodcloud/index.php/?user/loginSubmit&isAjax=1&getToken=1&name=admin&password=123456')
        resp_login.encoding='utf-8'
        # print(resp_login.text)

    def add(self):
        data={'name':'demo1',
              'password': '123456',
              'sizeMax': '2',
              'role': '2',
              'groupInfo': '{"1": "write"}',
              'homePath':'C:/'
         }
        resp_add=self.session.post(url='http://192.168.80.128/kodcloud/index.php/?systemMember/add',data=data)
        resp_add.encoding='utf-8'
        # print(resp_add.text)

    def dele(self):
        data={'action':'del',
              'userID': '["103"]',
              }
        resp_del = self.session.post(url='http://192.168.80.128/kodcloud/index.php/?systemMember/doAction', data=data)
        resp_del.encoding = 'utf-8'
        print(resp_del.text)

    def create_file(self):
        data={'path':'C:\other/newfile.txt'}
        resp=self.session.post(url='http://192.168.80.128/kodcloud/index.php/?explorer/mkfile',data=data)
        resp.encoding = 'utf-8'
        print(resp.text)

    def modify_file(self):
        data={'path':'C:\other/newfile.txt','charset':'utf-8','filestr':'22222'}
        resp=self.session.post(url='http://192.168.80.128/kodcloud/index.php/?editor/fileSave',data=data)
        resp.encoding='utf-8'
        print(resp.text)

    def check_file(self):
        data={'filename':'C:\other/newfile.txt'}
        resp=self.session.post(url='http://192.168.80.128/kodcloud/index.php/?editor/fileGet',data=data)
        resp.encoding = 'utf-8'
        # print(resp.text)
        i=json.loads(resp.text)
        y=i['data']['content']
        x=base64.b64decode(y)
        print(i)
        print(y)
        print(x)
        print(x.decode('utf-8'))
        if '22222你真好' == x.decode('utf-8'):
            print("ok")
        else:
            print('fail')

if __name__ == '__main__':

     a=kod()
     a.login()
     # a.add()
     # a.dele()
     # a.create_file()
     # a.modify_file()
     a.check_file()

