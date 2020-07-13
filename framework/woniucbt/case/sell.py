from framework.woniucbt.object.sell import SellObject
from framework.woniucbt.common.database import Database
import random
from framework.woniucbt.common.utility import UtilityTest

class SellTest:
    def __init__(self):
        self.sell_object = SellObject()
        self.database = Database()

    def main_test(self):
        # 销售出库模块：gui+接口测试
        self.test_sell_gui()

    def test_sell_gui(self):
        # 从CSV文件中随机读取一个条码
        barcode_list = self.read_sell_barcode()
        barcode = random.choice(barcode_list)
        self.sell_object.do_buy_goods(barcode, '78')

        # 从数据库中直接读取一个电话号码
        phone = self.database.query_one('select customerphone from customer order by RAND() limit 0,1')
        self.sell_object.do_sell(phone['customerphone'], '1.8')

        # 销售完成后进行断言，直接从数据库中取值
        sql = "select barcode from sell where barcode='%s' order by sellid DESC LIMIT 0,1" % barcode
        if self.database.query_one(sql) is None:
            UtilityTest.assert_result_2('销售出库', 'GUI测试', '扫码功能测试', '失败')
        else:
            UtilityTest.assert_result_2('销售出库', 'GUI测试', '扫码功能测试', '成功')


    def read_sell_barcode(self):
        barcode_list = []
        with open('../data/barcode.csv') as file:
            line_list = file.readlines()

        for i in range(1, len(line_list)):
            barcode_list.append(line_list[i].strip())

        return barcode_list