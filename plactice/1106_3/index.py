# 標準入力から値を受け取る
# num: int 型
num = int(input())

if not(num % 2 == 0 or num % 3 == 0 or num % 5 == 0): # 条件を満たさないなら
    print("Yes")
else: # そうでないなら
    print("No")