#!/usr/bin/env python3

from converte_romano import valida_numero
from converte_romano import numero_para_romano
import unittest

class Testvalida2(unittest.TestCase):
    def testform(self):
        testcase = 3998
        expected = "MMMCMXCVIII"
        self.assertEqual(valida_numero(testcase), (expected))

class Testvalida(unittest.TestCase):
    def testform(self):
        testcase = 3999
        expected = "invalido"
        self.assertEqual(valida_numero(testcase), (expected))

class Testnumero(unittest.TestCase):
    def testform(self):
        testcase = 3998
        expected = "MMMCMXCVIII"
        self.assertEqual(numero_para_romano(testcase), (expected))


unittest.main()