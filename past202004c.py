
#入力
N = int(input())
S = []
for i in range(0, N):
  si = list(input())
  S.append(si)

# N-2から0まで下から順番に見る
for i in range(N-2, -1, -1):
  # 1から2N-2まで左から順番に見る
  for j in range(1, 2*N-1):
    # 条件に合えば書き換える
    if S[i][j] == "#":
      if S[i+1][j-1] == "X":
        S[i][j] = "X"
      if S[i+1][j] == "X":
        S[i][j] = "X"
      if S[i+1][j+1] == "X":
        S[i][j] = "X"

# 出力
for i in range(0, N):
  S[i] = "".join(S[i]) # S[i]を結合して一つの文字列に変換する
  print(S[i])