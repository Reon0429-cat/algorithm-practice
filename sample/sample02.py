# -*- coding: utf-8 -*-

a = input()
if 200 > a > 100:
  print("100より大きい200より小さい")
else:
  print("100より小さい")

if 1 < a and a < 10:
  print("OK")

print(not False)

a = [1, 2, 3, 4, 5]
sum = 0
for i in a:
  sum += i
print(sum)

for i in range(0, 100): # 0..<100
  print(i)
  sum += i
print(sum)

a = {"a": 1, "b": 2, "c": 3}

if "a" in a:
  print(a["a"])
else:
  print("not exist")

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
















