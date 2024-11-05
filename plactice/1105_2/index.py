# 標準入力から値を受け取る
# age: int 型
age = int(input())

# age の値に応じて場合分け

if age < 15: # age が 15 未満なら
    print("child") 
elif age < 65: # そうではなく、age が 65 未満なら
    print("working-age")
else: # それ以外なら
    print("senior")