#!/usr/bin/env python3

import hashlib

def hash_md5(pwd):
  hashmd5 = hashlib.md5(pwd.encode('utf8')).hexdigest()
  return hashmd5

def hash_sha256(pwd):
  hashsha256 = hashlib.sha256(pwd.encode('utf8')).hexdigest()
  return hashsha256

