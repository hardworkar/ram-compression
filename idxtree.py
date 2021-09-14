import math

def bin_fixed(x, l):
  return ('{0:0' + str(l) + 'b}').format(x)

class IdxTree():
  def __init__(self, y):
    self.N = len(y)
    self.v = int(math.log2(self.N))
    assert self.N & (self.N-1) == 0

    self.Q = []
    nsum = 1
    for i in range(0, self.v + 1):
      self.Q.append([])
      for j in range(0, self.N, nsum):
        k = j // nsum
        print("Q[%d][%d]: %s" % (i + 1, j + 1, y[j:j + nsum]))
        self.Q[i].append(sum(y[j:j + nsum]))
      nsum *= 2
  def sumj(self, j):
    a = bin_fixed(j, self.v + 1)
    S = 0
    T = 0
    for i in range(0, self.v + 1):
      T = 2 * T + int(a[i])
      S = S + int(a[i]) * self.Q[self.v - i][T - 1]
    return S
