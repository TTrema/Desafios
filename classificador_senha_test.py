#!/usr/bin/env python3

from classificador_senha import classifica_senha
import unittest

class Testclassifica(unittest.TestCase):
    def testform(self):
        self.assertEqual(classifica_senha("!An3g4s"), (0))
        self.assertEqual(classifica_senha("Password"), (1))
        self.assertEqual(classifica_senha("P4ssw0rd"), (2))
        self.assertEqual(classifica_senha("Password!"), (2))
        self.assertEqual(classifica_senha(""), ("Digite uma senha"))
        

unittest.main()