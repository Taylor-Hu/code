#!/usr/bin/env python
#-*- coding:utf-8 -*-

from interface.ddt_test_data.common.function import Fun

# from lxml import etree

# 遍历第二个节点下每个节点的数据
# xml = etree.parse("D:/Other/class.xml")
# root = xml.getroot()
# list=xml.xpath("//student[@sequence='2']")
# for item in list:
#     for node in item.getchildren():
#         print('节点名为：%s, 内容为：%s' % (node.tag, node.text))
#
# # 读取某个特定节点的数据
# list = xml.xpath("/class/student[2]")
# print(list[0].get('sequence'))  # 获取某个节点的属性值
# print(list[0].getchildren()[0].tag)
# print(list[0].getchildren()[0].text)


# tree = etree.parse("D:/Other/window_dump.xml")
# # 根据单个属性获取节点，并读取该节点的其他数据
# node_list = tree.xpath("//node[@resource-id='com.miui.calculator:id/btn_7']")
# print(node_list[0].get('text'))
# print(node_list[0].get('class'))
# print(node_list[0].get('bounds'))
#
# # 根据多个属性获取节点数据
# node_list = tree.xpath("//node[@index='0' and @text='7']")
# print(node_list[0].get('resource-id'))
# print(node_list[0].get('class'))
# print(node_list[0].get('bounds'))
#
# # 对bounds属性的数据进行运算，获取中心点的位置坐标
# bounds = node_list[0].get('bounds')
# bounds = bounds.replace('[', '', 1)
# bounds = bounds.replace('][', ',', 1)
# bounds = bounds.replace(']', '')
# left_top_x = int(bounds.split(",")[0])
# left_top_y = int(bounds.split(",")[1])
# bottom_right_x = int(bounds.split(",")[2])
# bottom_right_y = int(bounds.split(",")[3])
# print(left_top_x, left_top_y, bottom_right_x, bottom_right_y)
# position_x = int((bottom_right_x - left_top_x) / 2) + left_top_x
# position_y = int((bottom_right_y - left_top_y) / 2) + left_top_y
# print(position_x, position_y)



