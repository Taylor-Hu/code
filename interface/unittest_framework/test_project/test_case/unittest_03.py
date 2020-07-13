import unittest
from parameterized import parameterized

from interface.unittest_framework.test_project.common.function import Function


class UnitTest03(unittest.TestCase):
    # cls.func = Function()和self.func = Function()初始化都可以，但是类初始化只会有一次，
    # self.func = Function()在每个测试用例运行前都会执行
    @classmethod
    # 重写父类的方法setUpClass，每次执行一个测试类时，会调用一次;
    def setUpClass(cls):
        cls.func = Function()
        print("每次执行一个测试类时，会调用一次")

    @classmethod
    def tearDownClass(cls):
        cls.func = None
        print("每次执行一个测试类后，会调用一次")

    # setUp()方法用于测试用例执行前的初始化工作。如测试用例中需要访问数据库，可以在setUp中建立数据库连接并进行初始化。
    # 如测试用例需要登录web，可以先实例化浏览器。
    # def setUp(self):
    #     self.func = Function()
    #     # print(id(self.func))
    #     print("每一个测试用例执行前，均会调用该方法")
    #
    # def tearDown(self):
    #     self.func = None
    #     # print(id(self.func))
    #     print("每一个测试用例执行后，均会调用该方法")

    @parameterized.expand([('12345', True),('123T5', False),('-123.45', True), ('123-5', False), ('-.', False)])
    # @performance(thread=100, iteration=20)
    def test_01(self, number, expect):
        actual = self.func.check_number(number)
        self.assertEqual(actual, expect)

    @parameterized.expand([(5,3,125),(5,-3,0.008),(-5,3,-125)])
    def test_02(self, x, y, expect):
        actual = self.func.power(x, y)
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()
