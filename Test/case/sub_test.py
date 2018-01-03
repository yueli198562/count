#coding:utf-8
from Count.ceshi import *
import unittest

class Sub(unittest.TestCase):
    u'''减法'''
    def test1(self):
        u'''减法测试3-2'''
        a=sub(3,2)
        self.assertEqual(a,1)

if __name__=="__main__":
    unittest.main()