import math

N = int(input())

x = math.ceil(N / 9)
y = N % 9

if y == 0:
  y = 9

ans = ""

for _ in range(0, x):
  ans += str(y)

print(ans)


# 全探索による解放
z = 0 # 今までに出てきたゾロ目の数
for i in range(1, 555555 + 1):
  si = str(i)
  ok = True
  for s in si:
    if s != si[0]:
      ok = False
  if ok:
    z += 1
  if ok and z == N:
    ans = i
print(ans)