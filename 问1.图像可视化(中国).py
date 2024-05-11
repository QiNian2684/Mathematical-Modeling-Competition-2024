import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd

size = 32

# 数据：时间范围和对应的状态
data = [
    {"start": "2000-01", "end": "2003-01", "status": "衰退"},
    {"start": "2003-01", "end": "2003-05", "status": "复苏"},
    {"start": "2003-05", "end": "2004-07", "status": "过热"},
    {"start": "2004-07", "end": "2006-04", "status": "复苏"},
    {"start": "2006-04", "end": "2008-06", "status": "过热"},
    {"start": "2008-06", "end": "2008-08", "status": "滞胀"},
    {"start": "2008-08", "end": "2009-06", "status": "衰退"},
    {"start": "2009-06", "end": "2009-09", "status": "复苏"},
    {"start": "2009-09", "end": "2011-08", "status": "过热"},
    {"start": "2011-08", "end": "2013-01", "status": "滞胀"},
    {"start": "2013-01", "end": "2018-07", "status": "衰退"},
    {"start": "2018-07", "end": "2019-11", "status": "滞胀"},
    {"start": "2019-11", "end": "2020-11", "status": "衰退"},
    {"start": "2020-11", "end": "2021-02", "status": "复苏"},
    {"start": "2021-02", "end": "2023-01", "status": "衰退"}
]


# 转换日期格式
for entry in data:
    entry["start"] = datetime.strptime(entry["start"], "%Y-%m")
    entry["end"] = datetime.strptime(entry["end"], "%Y-%m")

# 设置时间范围
start_date = datetime.strptime("2001-01", "%Y-%m")
end_date = datetime.strptime("2023-1", "%Y-%m")

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
fig, ax = plt.subplots(figsize=(35, 5))

# 绘制状态甬道
for i, status in enumerate(statuses):
    ax.fill_between([start_date + pd.DateOffset(months=i) for i in range((end_date - start_date).days // 30)], i + 0.5, i + 1.5,
                    where=[any((entry["start"] <= start_date + pd.DateOffset(months=i) <= entry["end"]) for entry in data if entry["status"] == status) for i in range((end_date - start_date).days // 30)],
                    color=status_colors[status], label=status)

# 设置标题和标签，并调整字体大小和字体
ax.set_xlabel("时间", fontsize=size, fontproperties='SimHei')
ax.set_ylabel("状态", fontsize=size, fontproperties='SimHei')
ax.set_yticks([i + 1 for i in range(len(statuses))])
ax.set_yticklabels(statuses, fontsize=size, fontproperties='SimHei')

# 设置横轴刻度为每年，并调整范围
ax.set_xlim(start_date, end_date)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=45, fontsize=size)
plt.yticks(fontsize=size)

# 图例放在图外
ax.legend(loc='upper left', bbox_to_anchor=(1,1), prop={'size': size, 'family': 'SimHei'})

# 自动调整日期标签
plt.tight_layout()

# 显示图形
plt.show()
