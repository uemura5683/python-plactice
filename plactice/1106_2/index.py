# 標準入力から値を受け取る
# S: str 型
S = input()

# 受け取った値を利用してコードを書いてください
if(len(S) >= 5 and len(S) <= 12 and S[0].isupper()):
  print('Yes')
else:
  print('No')