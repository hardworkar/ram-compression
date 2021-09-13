#!/usr/bin/env python3
from huffman import Huffman
import math

L = 15
h = Huffman(L)

trim_hcode = dict()

for a, c in h.code.items():
  if len(c) <= math.ceil(math.log2(L)):
    trim_hcode[a] = "0" + c
  else:
    trim_hcode[a] = "1" + ('{0:0' + str(math.ceil(math.log2(L))) + 'b}').format(h.c_idx[a])
for a, c in trim_hcode.items():
  print("%c : %s" % (a, c))
