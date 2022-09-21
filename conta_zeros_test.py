#!/usr/bin/env python3

from conta_zeros import conta_zeros

import unittest

class Testconta(unittest.TestCase):
    def testform(self):
        testcase = "000056007974501515"
        expected = "0000"
        self.assertEqual(conta_zeros(testcase), (expected))

class Testconta2(unittest.TestCase):
    def testform(self):
        testcase = "65065000664894980"
        expected = "000"
        self.assertEqual(conta_zeros(testcase), (expected))

class Testconta3(unittest.TestCase):
    def testform(self):
        testcase = "498405484005498498400000"
        expected = "00000"
        self.assertEqual(conta_zeros(testcase), (expected))





unittest.main()