# -*- coding: utf-8 -*-

S = "aabbcaabcccabbbbb"
na = S.count("a")
nb = S.count("b")
nc = S.count("c")
max = max(na, nb, nc)
if na == max:
  print("a", na)
elif nb == max:
  print("b", nb)
elif nc == max:
  print("c", nc)