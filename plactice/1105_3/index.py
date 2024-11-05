# 標準入力から値を受け取る
# A, B, C: int 型
A = int(input())
B = int(input())
C = int(input())

if A <= B and B < C: # もし B が A 以上かつ C 未満なら
    print("Yes")
else: # そうでないなら
    print("No")