from framework.woniucbt.common.utility import UtilityTest
import random

class CustomerTest:
    def __init__(self):
        pass

    def main_test(self):
        # 会员管理模块：新增、编辑、查询
        self.test_add_customer()
        self.test_edit_customer()
        self.test_query_customer()

    def test_add_customer(self):
        list = self.read_customer_data()
        for item in list:
            data = {'customername': item['customername'], 'customerphone': item['customerphone'],
                    'childsex': item['childsex'],
                    'childdate': item['childdate'], 'creditkids': item['creditkids'],
                    'creditcloth': item['creditcloth']}
            resp = UtilityTest.session.post('http://192.168.80.128:8080/woniusales/customer/add', data=data)
            self.write_result('新增会员', item['expectresult'], resp.text)
            print(resp.text)

    def test_edit_customer(self):
        rand_phone = random.randrange(10000000, 99999999)
        data = UtilityTest.build_dict('customerid=8&customerphone=182%d&customername=已修改&childsex=男&'
                                    'childdate=2017-10-28&creditkids=0&creditcloth=784' % rand_phone)
        resp = UtilityTest.session.post('http://192.168.80.128:8080/woniusales/customer/edit', data=data)
        self.write_result('修改会员', 'edit-successful', resp.text)

    def test_query_customer(self):
        pass

    def write_result(self, case, expect, actual):
        UtilityTest.assert_result('会员管理', '接口测试', case, expect, actual)

    def read_customer_data(self):
        path = '../data/customer.csv'
        with open(path, encoding='utf-8') as f:
            temp_list = f.readlines()

        column = temp_list[0].strip().split(',')

        list = []
        for i in range(1, len(temp_list)):
            dict = {}
            temp = temp_list[i].strip().split(',')
            for j in range(len(column)):
                dict[column[j]] = temp[j]
            list.append(dict)

        return list