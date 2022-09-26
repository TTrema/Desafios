#!/usr/bin/env python3

from validacpf import retira_formatacao
from validacpf import valida_cpf
import unittest

class Testformatacao(unittest.TestCase):
    def testform(self):

        self.assertEqual(retira_formatacao("123.456.789-01"), ("12345678901"))
        self.assertEqual(valida_cpf("11111111111"), ("todos os digitos repetidos não devem ser aceitos"))


unittest.main()