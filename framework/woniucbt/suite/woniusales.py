from framework.woniucbt.case.login import LoginTest
from framework.woniucbt.case.sell import SellTest
from framework.woniucbt.case.customer import CustomerTest
from framework.woniucbt.common.reporter import Reporter
from framework.woniucbt.common.utility import UtilityTest

import time

class WoniuSalesSuite:
    def start_test(self):
        # 与高内聚，低耦合原则违背
        # 展示自定义的HTML测试报告，禁止使用unittest，必须使用POM和ATM及单例模式
        # 测试WoniuSales销售出库，客户管理和商品入库模块，基于UI和接口两个部分。
        # 在不同的模块的case里面实现高内聚，在suite层调用模块级用例实例低耦合
        UtilityTest.version = UtilityTest.get_config_value('ci', 'version')
        LoginTest().main_test()
        SellTest().main_test()
        CustomerTest().main_test()
        time.sleep(5)
        Reporter().generate_report(UtilityTest.version)

if __name__ == '__main__':
    WoniuSalesSuite().start_test()


