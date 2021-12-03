# -*- coding: utf-8 -*-

s = list(map(int, input().split())) # 配列として受け取る
s.sort(reverse=True) # 降順に並べる
print(s[2])

