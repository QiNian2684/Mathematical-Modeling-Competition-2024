import matplotlib
import matplotlib.pyplot as plt

# 配置matplotlib支持中文显示，并设置所有文本的大小
matplotlib.rcParams['font.size'] = 15  # 设置全局字体大小
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 输入数据
data = [[1990, 'A'], [1991, 'A'], [1992, 'A'], [1993, 'B'], [1994, 'B'], [1995, 'A'],
        [1996, 'C'], [1997, 'A'], [1998, 'C'], [1999, 'C'],
        [2000, 'D'], [2001, 'D'], [2002, 'D'], [2003, 'D'],
        [2004, 'A'], [2005, 'A'], [2006, 'A'],
        [2007, 'B'], [2008, 'B'], [2009, 'C'], [2010, 'B'],
        [2011, 'C'], [2012, 'C'], [2013, 'C'],
        [2014, 'D'], [2015, 'D'], [2016, 'D'], [2017, 'B'],
        [2018, 'A'], [2019, 'A'], [2020, 'A'], [2021, 'A'],
        [2022, 'B'], [2023, 'B'], [2024, 'C']
]

# 组织数据
categories = {'A': [], 'B': [], 'C': [], 'D': []}
for year, category in data:
    if categories[category] and categories[category][-1][0] + categories[category][-1][1] == year:
        categories[category][-1][1] += 1
    else:
        categories[category].append([year, 1])

# 设置颜色和行位置
color_map = {'A': '#FF6347', 'B': '#4682B4', 'C': '#3CB371', 'D': '#FFA500'}
# 设置y_positions以确保中心对齐
base_position = 1
spacing = 1
y_positions = {category: base_position + i * spacing for i, category in enumerate('ABCD')}

# 绘图
fig, ax = plt.subplots(figsize=(15, 3))
for category, ranges in categories.items():
    # 设置颜色条高度为1，并根据中心对齐调整
    ax.broken_barh(ranges, (y_positions[category] + 0.25, 1), facecolors=color_map[category], label=category)

# 设置图表
ax.set_ylim(1, 8.5)  # 调整y轴的限制以适应新的y_positions和条高度
ax.set_xlim(1990, 2025)
ax.set_yticks([y + 0.75 for y in y_positions.values()], labels=y_positions.keys())
ax.set_xlabel('年份')
ax.set_title('年份分类表示')
# 设置图例到图表外右侧
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# 更详细的年份标记，每3年显示一次
ax.set_xticks(range(1990, 2025, 3))
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

plt.show()
