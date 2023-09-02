import csv
import random
from datetime import datetime, timedelta

# ユーザーIDのリスト
user_ids = [1, 2, 3, 4, 5]

# 日付の範囲
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)

# データを生成する回数
num_rows = 1000

# データを格納するリスト
data = []

# データを生成
for i in range(num_rows):
    id = i
    user_id = random.choice(user_ids)
    date = start_date + timedelta(days=random.randint(0, 364))
    amount = random.randint(100, 10000)
    store = f"store_{random.randint(1, 10)}"
    data.append((id, user_id, date, amount, store))

# データをCSVファイルに書き込む
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "user_id", "date", "amount", "store"])
    writer.writerows(data)
