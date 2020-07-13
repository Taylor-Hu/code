
import unittest

from interface.unittest_framework.test_project.common.function import Function

class UnitTest02(unittest.TestCase):
    @classmethod
    def setUpClass(cls): # 重写父类的方法setUpClass，每次执行一个测试类时，会调用一次
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

    def test_21(self):
        result = self.func.check_number('12345')
        print("test_21 is tested")
        self.assertTrue(result)

    def test_22(self):
        result = self.func.check_number('124T5')
        self.assertFalse(result)

    def test_23(self):
        result = self.func.check_number('123.')
        self.assertTrue(result)

    def test_24(self):
        result = self.func.check_number('-123.45')
        self.assertTrue(result)

    def test_25(self):
        result = self.func.power(5, 3)
        self.assertEqual(result, 125)

if __name__ == '__main__':
    unittest.main()
