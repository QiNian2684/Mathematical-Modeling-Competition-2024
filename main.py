import random

# 生成按照年份和月份递增的字符数组，满足大体5至10个月变一个字符的规律，允许有较多噪音
def generate_data_with_correct_cycle(start_year, end_year):
    data = []
    current_char = 'A'
    month_counter = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            # 生成日期
            date = f"{year}.{month}"
            # 添加日期和字符到数据列表中
            data.append([date, current_char])
            month_counter += 1
            # 当月数达到5至10个月时，变换字符
            if month_counter >= random.randint(8, 36):
                month_counter = 0
                current_char = chr((ord(current_char) - ord('A') + 1) % 4 + ord('A'))  # 字符在'A', 'B', 'C', 'D'之间循环
    # 在数据中引入较多噪音，但保证噪音字符在 'A', 'B', 'C', 'D' 范围内
    for i in range(len(data)):
        if random.random() < 0.3:  # 20%的概率引入噪音
            noise_char = chr((ord(data[i][1]) + random.randint(1, 3) - ord('A')) % 4 + ord('A'))
            data[i][1] = noise_char
    return data

# 生成数据
data_with_correct_cycle = generate_data_with_correct_cycle(1990, 2024)

# 格式化输出数据
formatted_data = ""
for item in data_with_correct_cycle:
    formatted_data += f"['{item[0]}', '{item[1]}'],\n"

print(formatted_data)
