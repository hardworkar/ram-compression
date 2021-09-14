#!/usr/bin/env python3
from huffman import Huffman
import math
import random

L = 15
uL = math.ceil(math.log2(L))
h = Huffman(L)

trim_hcode = dict()

from idxtree import IdxTree, bin_fixed

for a, c in h.code.items():
  if len(c) <= uL:
    trim_hcode[a] = "0" + c
  else:
    trim_hcode[a] = "1" + bin_fixed(h.c_idx[a], uL)

x = [chr(i + ord('a')) for i in [5, 0, 0, 10, 1, 2, 3, 4]]
print("message: %s" % " ".join(x))
z = [trim_hcode[i] for i in x]
print("z_coded: %s" % " ".join(z))
y = list(map(len, z))
print("y_coded: %s" % y)


N = 1024 
y = [random.randint(1, 100) for _ in range(N)]
it = IdxTree(y)
for i in range(1, N + 1):
  print("till %d: %d" % (i, it.sumj(i)))
  assert it.sumj(i) == sum(y[:i])
