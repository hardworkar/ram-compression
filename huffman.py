#!/usr/bin/env python3
# https://en.wikipedia.org/wiki/Huffman_coding

from queue import PriorityQueue

class Node():
  def __init__(self, prob, c = None, child = [None, None]):
    self.child = child[:]
    self.prob = prob
    self.c = c
  def __lt__(self, other):
    return self.prob < other.prob

class Huffman():
    def __init__(self, L):
      self.A = list(map(chr, range(ord('a'), ord('a') + L)))
      self.c_idx = dict()
      for i in range(L):
        self.c_idx[self.A[i]] = i
      self.p = [pow(2.0, -i) for i in range(1, L)]
      self.p.append(self.p[-1])

      Q = PriorityQueue()

      for i in range(L):
        Q.put(Node(self.p[i], self.A[i]))

      e = None
      while True:
        n1 = e = Q.get()
        if Q.empty():
          break
        n2 = Q.get() 
        Q.put(Node(n1.prob + n2.prob, None, [n1, n2]))

      self.code = dict()

      def trTree(node, seq = ""):
        if node.child[0] == node.child[1] == None:
          self.code[node.c] = seq
        else:
          trTree(node.child[0], seq + "0")
          trTree(node.child[1], seq + "1")
      trTree(e)
