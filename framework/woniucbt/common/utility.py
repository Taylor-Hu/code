from selenium import webdriver
import time, requests, os
from framework.woniucbt.common.reporter import Reporter

class UtilityTest:

    driver = None       # 将driver定义为类级变量，不随实例化而被重新赋值为None
    session = None
    version = ''

    def __init__(self):
        pass

    @classmethod
    def get_webdriver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.get('http://192.168.80.128:8080/woniusales/')
            try:
                cls.driver.maximize_window()
            except:
                pass
            cls.driver.implicitly_wait(10)
            time.sleep(5)

        return cls.driver

    @classmethod
    def get_session(cls):
        if cls.session is None:
            cls.session = requests.session()
        return cls.session

    @classmethod
    def write_result_file(self, case, result):
        path = '../result/mytest.txt'
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        line = now + "," + case + ',' + result + '\n'
        with open(path, 'a+', encoding='utf-8') as f:
            f.write(line)

    @classmethod
    def write_result(cls, module, testtype, casetitle, result):
        reporter = Reporter()
        if result == '失败':
            screenshot = reporter.capture_screen()
        else:
            screenshot = '无'
        reporter.write_report(version=cls.version, module=module, testtype=testtype,
                            casetitle=casetitle, result=result, screenshot=screenshot)

    @classmethod
    def assert_result(cls, module, testtype, case, expect, actual):
        if expect == actual:
            cls.write_result(module, testtype, case, '成功')
        else:
            cls.write_result(module, testtype, case, '失败')

    @classmethod
    def assert_result_2(cls, module, testtype, case, result):
        cls.write_result(module, testtype, case, result)


    # 把一个POST请求上下文的key=value&key=value&key=value的普通字符串转换为一个字典对象，供request发请求用
    @classmethod
    def build_dict(self, string):
        dict = {}
        list = string.split('&')
        for item in list:
            key = item.split('=')[0]
            value = item.split('=')[1]
            dict[key] = value

        return dict

    @classmethod
    def get_config_value(cls, section, key):
        from configparser import ConfigParser
        config = ConfigParser()
        config.read('../data/woniusales.conf')  # 读取当前目录下的配置文件
        return config.get(section, key)


# if __name__ == '__main__':
#     Utility.version = '1.2.3'
#     Utility.assert_result('登录','GUI','成功登录','1', '2')