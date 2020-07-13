#!/usr/bin/env python
#-*- coding:utf-8 -*-

if __name__ == '__main__':

    # dict1 = {1:2,2:3}
    # dict2 = {3:4,4:5}
    # dict1.update(dict2)
    # print(dict1)    # {1: 2, 2: 3, 3: 4, 4: 5} 没有返回值

    # dict1 = {'name':'zhangsan','age':'20'}
    # dict2 = {'name':'lisi','age':'22'}
    # dict3 = {'name':'zhouwu','age':'21'}
    # list1 = [dict1,dict2]
    # list1[1]['age'] = 23
    # print(list1[1])     #{'name': 'lisi', 'age': 23}
    #
    # #[{'name': 'zhangsan', 'age': '20'}, {'name': 'lisi', 'age': 23}, {'name': 'zhouwu', 'age': '21'}]
    # list1.append(dict3)
    # print(list1)
    # print(list1[0].keys())  #dict_keys(['name', 'age'])

    # score_table = {}
    # sno = input("请输入您的学号")
    # score_list = []
    # i = 0
    # while 1:
    #     score = int(input("请输入第%d门课的成绩"%(i+1)))
    #     score_list.append(score)
    #     sel = input("是否继续输入下一门课的成绩：（y/n）")
    #     if sel == 'y':
    #         i += 1
    #         continue
    #     else:
    #         break
    # score_table[sno] = score_list
    # print(score_table)  # {'101': [78, 87, 90]}
    # print("最高分是%d"%(max(score_list)))

    score = [45,98,65,87,43,83,68,74,20,75,85,67,79,99]
    acount = bcount = ccount = dcount = ecount = 0

    for i in score:
        if 90<=i<=100:
            acount += 1
        elif i>=80:
            bcount += 1
        elif i>=70:
            ccount += 1
        elif i>=60:
            dcount += 1
        else:
            ecount += 1

    score_dict = {'A':acount,'B':bcount,'C':ccount,'D':dcount,'E':ecount}
    # {'A': 2, 'B': 3, 'C': 3, 'D': 3, 'E': 3}
    print(score_dict)























