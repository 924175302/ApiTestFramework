# unitest测试框架

import unittest
import config
import time
from script.test_login import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))

report = config.BASE_DIR + "/report/report_{}.html".format(time.strftime("%Y%m%d-%H%M"))

with open(report, "wb") as f:
    # 创建HTMLTestRunner
    runner = HTMLTestRunner(f, title="接口测试报告")
    # 执行测试套件
    runner.run(suite)

