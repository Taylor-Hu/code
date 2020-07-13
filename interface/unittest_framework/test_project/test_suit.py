import unittest, os, time
from HTMLTestRunner import HTMLTestRunner
from unittest import TestLoader

from interface.unittest_framework.test_project.test_case.unittest_01 import UnitTest01
from interface.unittest_framework.test_project.test_case.unittest_02 import UnitTest02
from interface.unittest_framework.test_project.test_case.unittest_03 import UnitTest03

# 单独添加每一个测试用例
# suite = unittest.TestSuite()
# suite.addTest(UnitTest01('test_a'))
# suite.addTest(UnitTest01('test_1'))
# suite.addTest(UnitTest02('test_22'))
# 利用addTests方法批量添加用例
# suite.addTests((UnitTest01('test_1'), UnitTest01('test_a'), UnitTest02('test_22'), UnitTest02('test_23')))

# 获取TestResult的一些属性值
# r = unittest.TestResult()
# suite.run(result=r)
# print(r.__dict__)
# print(r.testsRun)
# print(r.failures)
# print(r.__dict__['testsRun'])
# print(r.__dict__['failures'][0][0])

# 直接指定测试类这一级进行调用
# suite = unittest.TestSuite()
# suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UnitTest01))
# suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UnitTest02))
# # suite.addTest(unittest.TestLoader().loadTestsFromName('code.unittest_01.UnitTest01'))
# result = unittest.TestResult()
# suite.run(result)
# print(result.__dict__)
# print(result.failures)


# 使用HTMLTestRunner运行
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UnitTest01))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UnitTest02))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UnitTest03))

    # 很重要：拼接的时候%H:%M:%S会存在识别不到":"的问题
    # filename = time.strftime('%Y-%m-%d_%H:%M:%S.csv')
    now = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
    report = os.path.join(os.path.abspath('.'), 'test_report')
    if not os.path.exists(report):
        os.mkdir(report)

    filename = 'unittest_test_report_%s.html' % now
    HtmlFile = os.path.join(report, filename)
    runner = HTMLTestRunner(stream=open(HtmlFile, 'wb'), title='测试报告', description='这是一个牛逼的报告')
    runner.run(suite)

