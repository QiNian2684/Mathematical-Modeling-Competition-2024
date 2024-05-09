import matplotlib
import matplotlib.pyplot as plt

# 配置matplotlib支持中文显示，并设置所有文本的大小
matplotlib.rcParams['font.size'] = 15  # 设置全局字体大小
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

# 输入数据
data_month = [
    ['2019.6', 'A'], ['2019.7', 'A'], ['2019.8', 'A'], ['2019.9', 'A'], ['2019.10', 'B'], ['2019.11', 'B'], ['2019.12', 'B'],
    ['2020.1', 'B'], ['2020.2', 'A'], ['2020.3', 'D'], ['2020.4', 'B'], ['2020.5', 'C'], ['2020.6', 'A'], ['2020.7', 'C'],
    ['2020.8', 'D'], ['2020.9', 'C'], ['2020.10', 'C'], ['2020.11', 'D'], ['2020.12', 'D'], ['2021.1', 'C'], ['2021.2', 'D'],
    ['2021.3', 'D'], ['2021.4', 'D'], ['2021.5', 'B'], ['2021.6', 'A'], ['2021.7', 'A'], ['2021.8', 'A'], ['2021.9', 'A'],
    ['2021.10', 'B'], ['2021.11', 'A'], ['2021.12', 'C'], ['2022.1', 'A'], ['2022.2', 'D'], ['2022.3', 'B'], ['2022.4', 'B'],
    ['2022.5', 'B'], ['2022.6', 'B'], ['2022.7', 'C'], ['2022.8', 'C'], ['2022.9', 'C'], ['2022.10', 'C'], ['2022.11', 'D'],
    ['2022.12', 'C'], ['2023.1', 'C'], ['2023.2', 'D'], ['2023.3', 'B'], ['2023.4', 'D'], ['2023.5', 'D'], ['2023.6', 'D'],
    ['2023.7', 'B'], ['2023.8', 'A'], ['2023.9', 'D'], ['2023.10', 'A'], ['2023.11', 'A'], ['2023.12', 'B'], ['2024.1', 'A'],
    ['2024.2', 'C'], ['2024.3', 'A'], ['2024.4', 'B'], ['2024.5', 'B'], ['2024.6', 'B'], ['2024.7', 'B'], ['2024.8', 'B'],
    ['2024.9', 'B'], ['2024.10', 'D'], ['2024.11', 'C'], ['2024.12', 'C']
]

# 组织数据
categories_month = {'A': [], 'B': [], 'C': [], 'D': []}
for date, category in data_month:
    year, month = map(int, date.split('.'))
    month_decimal = year + (month - 1) / 12
    if categories_month[category] and categories_month[category][-1][0] + 1 / 12 == month_decimal:
        categories_month[category][-1][1] += 1
    else:
        categories_month[category].append([month_decimal, 1])

# 设置颜色和行位置
color_map = {'A': '#FF6347', 'B': '#4682B4', 'C': '#3CB371', 'D': '#FFA500'}
# 设置y_positions以确保中心对齐
base_position = 5
spacing = 1.5
y_positions = {category: base_position + i * spacing for i, category in enumerate('ABCD')}

# 绘图
fig, ax = plt.subplots(figsize=(15, 6))
for category, ranges in categories_month.items():
    # 设置颜色条高度为1，并根据中心对齐调整
    ax.broken_barh(ranges, (y_positions[category] + 0.25, 1), facecolors=color_map[category], label=category)

# 设置图表
ax.set_ylim(4, 12)  # 调整y轴的限制以适应新的y_positions和条高度
ax.set_xlim(2019, 2025)
ax.set_yticks([y + 0.75 for y in y_positions.values()], labels=y_positions.keys())
ax.set_xlabel('年份')
ax.set_title('年份分类表示')
# 设置图例到图表外右侧
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# 更详细的月份标记，每3个月显示一次
ax.set_xticks([2019 + i / 12 for i in range(0, 72, 3)])  # 每3个月显示一次
ax.set_xticklabels([f'{int(year)}.{int(month):02d}' for year in range(2019, 2025) for month in range(1, 13, 3)])  # 格式化标签

plt.show()
