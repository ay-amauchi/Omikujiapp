import random

omikuji = ["大吉", "吉", "凶"]  # 結果リストをまとめて定義する

idx = random.randint(0, 2)

result = omikuji[idx]

print(f"今日の運勢は... {result}です。")
