#!/usr/bin/env python3

from classificador_senha import classifica_senha
import unittest

class Testclassifica(unittest.TestCase):
    def testform(self):
        testcase = "!An3g4s"
        expected = 0
        self.assertEqual(classifica_senha(testcase), (expected))

class Testclassifica2(unittest.TestCase):
    def testform(self):
        testcase = "Password"
        expected = 1
        self.assertEqual(classifica_senha(testcase), (expected))

class Testclassifica3(unittest.TestCase):
    def testform(self):
        testcase = "P4ssw0rd"
        expected = 2
        self.assertEqual(classifica_senha(testcase), (expected))

class Testclassifica4(unittest.TestCase):
    def testform(self):
        testcase = "Password!"
        expected = 2
        self.assertEqual(classifica_senha(testcase), (expected))

unittest.main()