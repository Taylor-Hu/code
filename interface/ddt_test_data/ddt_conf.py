#!/usr/bin/env python
#-*- coding:utf-8 -*-

from interface.ddt_test_data.common.function import Fun

import random
from configparser import ConfigParser
# 读取配置文件
def get_config_value(section, key):
    config = ConfigParser()
    config.read('./data/woniusales.conf') # 读取当前目录下的配置文件
    return config.get(section, key)

if __name__ == '__main__':
    # random可以随机生成一些数字
    print(get_config_value('ci', 'tomcat'))
    print(get_config_value('ci', 'rar'))
    print(get_config_value('ci', 'svn'))
    print(get_config_value('ci', 'svn_url'))
    print(get_config_value('ci', 'version'))
