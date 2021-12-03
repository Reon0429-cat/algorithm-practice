
# A以上B以下にKの倍数が含まれるかどうか

K = input()
A, B = map(int, input().split())

ok = False

for i in (A, B+1):
  if i % K == 0:
    ok = True

if ok:
  print("ok")
else:
  print("NG")

