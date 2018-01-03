# coding:utf-8

import unittest
from HTMLTestRunner import HTMLTestRunner

discover=unittest.defaultTestLoader.discover("./case",pattern="*_test.py")

if __name__ == "__main__":
    filename="./report/report.html"
    f=open(filename,"wb")
    runner=HTMLTestRunner(stream=f,title="count",description=u"测试运算方法")
    runner.run(discover)
    f.close()






