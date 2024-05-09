import random

# 生成二维数组
data = [[year, random.choice(['A', 'B', 'C', 'D'])] for year in range(1990, 2025)]

# 输出结果
for item in data:
    print(item)
