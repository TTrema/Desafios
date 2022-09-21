#!/usr/bin/env python3
import re

def conta_zeros(texto):
  f = max(re.findall("0+", texto), key=len)
  return f


