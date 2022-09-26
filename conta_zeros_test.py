#!/usr/bin/env python3

from conta_zeros import conta_zeros

import unittest

class Testconta(unittest.TestCase):
    def testform(self):
     
        self.assertEqual(conta_zeros("000056007974501515"), ("0000"))
        self.assertEqual(conta_zeros("65065000664894980"), ("000"))
        self.assertEqual(conta_zeros("498405484005498498400000"), ("00000"))





unittest.main()