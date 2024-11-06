# 標準入力から値を受け取る
# diff: int 型
diff = int(input())

# diff の値で場合分けして、適切な文字列を出力する

if 1 <= diff and diff <= 9: # 1 以上 9 以下なら
    print("easy")
elif 11 <= diff and diff <= 19: # そうではなく、11 以上 19 以下なら
    print("normal")
elif 21 <= diff and diff <= 29: # そうではなく、21 以上 29 以下なら
    print("hard")
else: # それ以外なら (10, 20, 30 なら)
    print("special")