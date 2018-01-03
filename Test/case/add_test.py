#coding:utf-8
from Count.ceshi import *
import unittest

class Add(unittest.TestCase):
    u'''加法'''
    def test1(self):
        u'''加法测试3+2'''
        a=add(3,2)
        self.assertEqual(a,5)

    def test2(self):
        u'''加法测试3+3'''
        b = add(3, 3)
        self.assertEqual(b, 6)

    def test3(self):
        u'''加法测试3+6'''
        c = add(3, 6)
        self.assertEqual(c, 9)

    def test4(self):
        u'''加法测试20+33'''
        d = add(20, 33)
        self.assertEqual(d, 53)

if __name__=="__main__":
    unittest.main()