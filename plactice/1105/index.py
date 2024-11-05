# 標準入力から距離を受け取る
dist = int(input())

# 初乗り料金
base_fare = 650

# 加算運賃
distance_fare = dist * 300

# 長距離割引の適用
if dist >= 100:
    discount = 5000
else:
    discount = 0

# 運賃の計算
total_fare = base_fare + distance_fare - discount

# 結果を出力
print(total_fare)