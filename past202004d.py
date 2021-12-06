# 入力
S = input()

# TがSにマッチするかどうかを調べる関数
def is_match(T, S):
  # Sのi文字目から始まる部分がTとマッチするか調べる
  for i in range(0, len(S) - len(T) + 1):
    ok = True
    # Tのj文字目とSのi+j文字目を見比べる
    for j in range(0, len(T)):
      if S[i+j] != T[j] and T[j] != ".":
        ok = False
    if ok:
      return True
  return False

# 使える文字の一覧
C = "abcdefghijklmnopqrstuvwxyz."
M = []

# 長さ1の文字列を全て調べてSとマッチしたらMに入れる
for T in C:
  if is_match(T, S):
    M.append(T)

# 長さ2の文字列を全て調べてSとマッチしたらMに入れる
for c1 in C:
  for c2 in C:
    T = c1 + c2
    if is_match(T, S):
      M.append(T)

# 長さ3の文字列を全て調べてSとマッチしたらMに入れる
for c1 in C:
  for c2 in C:
    for c3 in C:
      T = c1 + c2 + c3
      if is_match(T, S):
        M.append(T)

# 出力
print(len(M))