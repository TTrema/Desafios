#!/usr/bin/env python3

from converte_romano import valida_numero
from converte_romano import numero_para_romano
import unittest

class Testvalida2(unittest.TestCase):
    def testform(self):

        self.assertEqual(valida_numero(3998), ("MMMCMXCVIII"))
        self.assertEqual(valida_numero(3999), ("invalido"))
        self.assertEqual(numero_para_romano(3998), ("MMMCMXCVIII"))


unittest.main()