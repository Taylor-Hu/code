import unittest
from unittest import TestCase

from interface.unittest_framework.test_project.common.function import Function


class UnitTest01(unittest.TestCase):
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

    def test_1(self):
        result = self.func.check_number('12345')
        print("test_1")
        self.assertTrue(result)

    @unittest.skip('暂时不执行')      # 不执行该用例
    def test_02(self):
        result = self.func.check_number('123T45')
        # self.assertFalse(result)
        print("正在测试test_02")

    @unittest.expectedFailure       # 测试标记为失败。
    def test_11(self):
        # result = self.func.check_number('12t3.')
        # self.assertTrue(result)
        self.fail('强制当前用例失败')

    def test_a(self):
        result = self.func.check_number('-123.45')
        self.assertTrue(result)
        print("test_a")

    def test_B(self):
        result = self.func.power(5, 3)
        self.assertEqual(result, 125)

if __name__ == '__main__':
    unittest.main()
