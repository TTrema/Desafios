#!/usr/bin/env python3

from validacpf import retira_formatacao
from validacpf import valida_cpf
import unittest

class Testformatacao(unittest.TestCase):
    def testform(self):
        testcase = "123.456.789-01"
        expected = "12345678901"
        self.assertEqual(retira_formatacao(testcase), (expected))

class Testvalida(unittest.TestCase):
    def testform(self):
        testcase = "11111111111"
        expected = "todos os digitos repetidos não devem ser aceitos"
        self.assertEqual(valida_cpf(testcase), (expected))


unittest.main()