#!/usr/bin/env python3

from criptografar_senhas import hash_md5
from criptografar_senhas import hash_sha256
import unittest

class Testhash(unittest.TestCase):
    def testform(self):

        self.assertEqual(hash_md5("!An3g4s"), ("cd1c13f98ec916e6ac22662c6c0c0fd5"))
        self.assertEqual(hash_md5("Pahrtw#ord"), ("311aacd9b1e1bb8354198a489644ccd1"))
        self.assertEqual(hash_sha256("!An3g4s"), ("6c9a8cec986dd33cc822bbcff31efb931d893a4028031801cc8ee53600be4832"))
        self.assertEqual(hash_sha256("Pahrtw#ord"), ("e6e1e80452011c59e75a8440343c88b3299ae19a3e86035beaebb376f77a2294"))

unittest.main()