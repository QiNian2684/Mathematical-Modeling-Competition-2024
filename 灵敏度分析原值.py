import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd

size = 38

# 数据：时间范围和对应的状态
data = [
    {"start": "2019-01", "end": "2020-08", "status": "衰退"},
    {"start": "2020-08", "end": "2020-12", "status": "复苏"},
    {"start": "2020-12", "end": "2021-04", "status": "过热"},
    {"start": "2021-04", "end": "2022-10", "status": "滞胀"},
    {"start": "2022-10", "end": "2023-01", "status": "衰退"}
    # {"start": "2019-01", "end": "2020-06", "status": "衰退"},
    # {"start": "2020-06", "end": "2020-10", "status": "复苏"},
    # {"start": "2020-10", "end": "2020-11", "status": "过热"},
    # {"start": "2020-11", "end": "2023-01", "status": "滞胀"}
]

# 转换日期格式
for entry in data:
    entry["start"] = datetime.strptime(entry["start"], "%Y-%m")
    entry["end"] = datetime.strptime(entry["end"], "%Y-%m")

# 设置时间范围
start_date = datetime.strptime("2019-01", "%Y-%m")
end_date = datetime.strptime("2023-01", "%Y-%m")

# 创建状态列表并调整顺序
statuses = ["复苏", "过热", "滞胀", "衰退"]

# 创建状态字典
status_colors = {
    "衰退": "#E74C3C",  # 亮红色
    "复苏": "#2ECC71",  # 亮绿色
    "过热": "#F39C12",  # 亮橙色
    "滞胀": "#3498DB"   # 亮蓝色
}

# 创建绘图
fig, ax = plt.subplots(figsize=(27, 5))

# 绘制状态甬道
for status in statuses:
    intervals = [(entry["start"], entry["end"]) for entry in data if entry["status"] == status]
    for start, end in intervals:
        ax.fill_betweenx([statuses.index(status) + 0.5, statuses.index(status) + 1.5], start, end, color=status_colors[status])

# 设置标题和标签，并调整字体大小和字体
ax.set_xlabel("时间", fontsize=size, fontproperties='SimHei')
ax.set_ylabel("状态", fontsize=size, fontproperties='SimHei')
ax.set_yticks([i + 1 for i in range(len(statuses))])
ax.set_yticklabels(statuses, fontsize=size, fontproperties='SimHei')

# 设置横轴刻度为每2个月一次，并调整范围
ax.set_xlim(start_date, end_date)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.xticks(rotation=45, fontsize=size)
plt.yticks(fontsize=size)

# 图例放在图外
ax.legend(loc='upper left', bbox_to_anchor=(1,1), prop={'size': size, 'family': 'SimHei'})

# 自动调整日期标签
plt.tight_layout()

# 显示图形
plt.show()
