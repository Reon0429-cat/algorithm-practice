# -*- coding: utf-8 -*-

# 変数
a_str = "10"
a_int = int(a_str)
a_int += 20
print(a_int)

print(3**2) # 3の2乗

print(len("abc"))

print("abc" * 3)

print("aacbdd".count("a"))

print("avcc".upper())

print("AA".lower())

b = "00-aaa-EEEEE"
print(b.split("-")) # ['00', 'aaa', 'EEEEE']

print("abcdefghijk"[1:4])

print([1, 2, 3] * 3)

print(list(reversed([1, 2, 3]))) # [3, 2, 1]

print(sorted([3, 1, 5, 2, 1, 4, 2, 5]))

a = [2, 3, 2, 4, 1]
a.append(100)
print(a)
a.pop()
print(a)
a[2] = 200
print(a)
a.sort()
print(a)
a.reverse()
print(a)





























