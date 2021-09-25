# Fast direct access to compressed memory

## Comparison

### "Fast direct access to variable length codes"

L = alphabet size \
N = length of seq

- Theorem 1. \
T = log(N) * (log(N) + log(log(L))) \
S = N(h(p) + log(log(L+2)) + 4)

- Theorem 2. \
T = logM * (logM + log(logL)) + logN \
S = N(h(p) + log(log(L+2)) + 4) + m * log(N(logL + 1)), \
where M = N / m

- Theorem 3. \
T = log(m) * (log(N) + log(log(L))) \
S = N * (hm(p) + (1/M) * (log(M) + log(log(L)) + O(1))) \
where M = N / m, hm = ...

##### Source:
https://arxiv.org/abs/2107.14577
##### Year: 2021

---

###  "Space Efficient Direct Access Data Structure"

...

##### Source:
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7786150
##### Year: 2016

---

### "Enhanced Variable-Length Codes: Improved Compression with Efficient Random Access"

##### Source:
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6824444
##### Year: 2014

---

### "DACs: Bringing Direct Access to Variable-Length Codes"

...

##### Source:
https://users.dcc.uchile.cl/~gnavarro/ps/ipm12.pdf 
##### Year: 2012
