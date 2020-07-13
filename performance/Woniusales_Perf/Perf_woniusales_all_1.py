import requests, re, time, threading, os, random
from performance.common.CommonUtility import monitor, rt_home_list

iteration = 15
# sleep = random.uniform(1, 3)
sleep = 0

class WoniuSalesDownload:
    def __init__(self):
        self.session = requests.session()

    @monitor('打开首页', iteration, sleep)
    def home(self):
        resp = self.session.get('http://localhost:8080/woniusales/')
        self.download(resp.text)

    @monitor('登录系统', iteration, sleep)
    def login(self):
        data = {'username': 'admin', 'password': 'admin123', 'verifycode': '0000'}
        resp = self.session.post(url='http://localhost:8080/woniusales/user/login', data=data)

    @monitor('销售出库', iteration, sleep)
    def sell(self):
        resp = self.session.get('http://localhost:8080/woniusales/sell')
        self.download(resp.text)

    @monitor('会员管理', iteration, sleep)
    def customer(self):
        resp = self.session.get('http://localhost:8080/woniusales/customer')
        self.download(resp.text)

    @monitor('新增会员', iteration, sleep)
    def add(self):
        phone = '18%s' % random.randint(100000000, 999999999)
        data = {'customername':'接口王', 'customerphone':phone, 'childsex':'男',
               'childdate':'2019-06-29', 'creditkids':'100', 'creditcloth':'200'}
        resp = self.session.post(url='http://localhost:8080/woniusales/customer/add', data=data)

    def download(self, response):
        list = []
        list += re.findall('href="(.+?)"/>', response)
        list += re.findall('src="(.+?)"', response)
        list += re.findall("url\('(.+?)'\)", response)

        # 读取download目录下的所有资源文件
        down_list = os.listdir('./download')

        for item in list:
            if not item.replace('/', '_') in down_list:
                if item.startswith('/'):
                    url = 'http://localhost:8080' + item
                elif item.startswith('http'):
                    url = item
                else:
                    url = 'http://localhost:8080/woniusales/' + item

                resp = self.session.get(url)

                # temp = item.split('/')
                # filename = temp[len(temp)-1]
                # print(filename)

                filename = item.replace('/', '_')
                with open('./download/' + filename, 'wb') as file:
                    file.write(resp.content)

    def start_run(self):
        self.home()
        self.login()
        self.sell()
        self.customer()
        self.add()

if __name__ == '__main__':
    wsd = WoniuSalesDownload()
    for i in range(200):
        wsd.start_run()

    # 让50个线程在10秒钟启动完成，每秒钟启动5个线程
    # for i in range(10):
    #     for j in range(5):
    #         threading.Thread(target=wsd.start_run).start()
    #     time.sleep(1)