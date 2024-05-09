import matplotlib.pyplot as plt
import matplotlib
import datetime

# 配置matplotlib支持中文显示，并设置所有文本的大小
matplotlib.rcParams['font.size'] = 15  # 设置全局字体大小
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 输入数据
data = [
    ['1990.1', 'A'],
    ['1990.2', 'B'],
    ['1990.3', 'C'],
    ['1990.4', 'A'],
    ['1990.5', 'A'],
    ['1990.6', 'A'],
    ['1990.7', 'D'],
    ['1990.8', 'B'],
    ['1990.9', 'A'],
    ['1990.10', 'A'],
    ['1990.11', 'A'],
    ['1990.12', 'A'],
    ['1991.1', 'A'],
    ['1991.2', 'A'],
    ['1991.3', 'B'],
    ['1991.4', 'D'],
    ['1991.5', 'B'],
    ['1991.6', 'B'],
    ['1991.7', 'B'],
    ['1991.8', 'B'],
    ['1991.9', 'B'],
    ['1991.10', 'B'],
    ['1991.11', 'B'],
    ['1991.12', 'B'],
    ['1992.1', 'C'],
    ['1992.2', 'C'],
    ['1992.3', 'A'],
    ['1992.4', 'B'],
    ['1992.5', 'B'],
    ['1992.6', 'A'],
    ['1992.7', 'C'],
    ['1992.8', 'B'],
    ['1992.9', 'B'],
    ['1992.10', 'A'],
    ['1992.11', 'B'],
    ['1992.12', 'C'],
    ['1993.1', 'D'],
    ['1993.2', 'C'],
    ['1993.3', 'C'],
    ['1993.4', 'C'],
    ['1993.5', 'D'],
    ['1993.6', 'D'],
    ['1993.7', 'A'],
    ['1993.8', 'D'],
    ['1993.9', 'B'],
    ['1993.10', 'D'],
    ['1993.11', 'D'],
    ['1993.12', 'D'],
    ['1994.1', 'A'],
    ['1994.2', 'B'],
    ['1994.3', 'A'],
    ['1994.4', 'D'],
    ['1994.5', 'A'],
    ['1994.6', 'A'],
    ['1994.7', 'D'],
    ['1994.8', 'C'],
    ['1994.9', 'A'],
    ['1994.10', 'B'],
    ['1994.11', 'A'],
    ['1994.12', 'B'],
    ['1995.1', 'B'],
    ['1995.2', 'B'],
    ['1995.3', 'D'],
    ['1995.4', 'B'],
    ['1995.5', 'D'],
    ['1995.6', 'B'],
    ['1995.7', 'B'],
    ['1995.8', 'B'],
    ['1995.9', 'A'],
    ['1995.10', 'D'],
    ['1995.11', 'C'],
    ['1995.12', 'C'],
    ['1996.1', 'B'],
    ['1996.2', 'C'],
    ['1996.3', 'C'],
    ['1996.4', 'C'],
    ['1996.5', 'C'],
    ['1996.6', 'B'],
    ['1996.7', 'C'],
    ['1996.8', 'C'],
    ['1996.9', 'B'],
    ['1996.10', 'B'],
    ['1996.11', 'C'],
    ['1996.12', 'D'],
    ['1997.1', 'B'],
    ['1997.2', 'A'],
    ['1997.3', 'D'],
    ['1997.4', 'D'],
    ['1997.5', 'B'],
    ['1997.6', 'C'],
    ['1997.7', 'C'],
    ['1997.8', 'D'],
    ['1997.9', 'B'],
    ['1997.10', 'D'],
    ['1997.11', 'B'],
    ['1997.12', 'A'],
    ['1998.1', 'B'],
    ['1998.2', 'A'],
    ['1998.3', 'A'],
    ['1998.4', 'B'],
    ['1998.5', 'D'],
    ['1998.6', 'A'],
    ['1998.7', 'A'],
    ['1998.8', 'B'],
    ['1998.9', 'A'],
    ['1998.10', 'A'],
    ['1998.11', 'A'],
    ['1998.12', 'A'],
    ['1999.1', 'A'],
    ['1999.2', 'A'],
    ['1999.3', 'D'],
    ['1999.4', 'A'],
    ['1999.5', 'B'],
    ['1999.6', 'B'],
    ['1999.7', 'B'],
    ['1999.8', 'D'],
    ['1999.9', 'B'],
    ['1999.10', 'B'],
    ['1999.11', 'C'],
    ['1999.12', 'B'],
    ['2000.1', 'B'],
    ['2000.2', 'B'],
    ['2000.3', 'B'],
    ['2000.4', 'B'],
    ['2000.5', 'B'],
    ['2000.6', 'A'],
    ['2000.7', 'B'],
    ['2000.8', 'C'],
    ['2000.9', 'C'],
    ['2000.10', 'C'],
    ['2000.11', 'C'],
    ['2000.12', 'C'],
    ['2001.1', 'B'],
    ['2001.2', 'C'],
    ['2001.3', 'C'],
    ['2001.4', 'B'],
    ['2001.5', 'B'],
    ['2001.6', 'C'],
    ['2001.7', 'A'],
    ['2001.8', 'C'],
    ['2001.9', 'C'],
    ['2001.10', 'D'],
    ['2001.11', 'D'],
    ['2001.12', 'D'],
    ['2002.1', 'D'],
    ['2002.2', 'D'],
    ['2002.3', 'D'],
    ['2002.4', 'D'],
    ['2002.5', 'C'],
    ['2002.6', 'A'],
    ['2002.7', 'D'],
    ['2002.8', 'A'],
    ['2002.9', 'B'],
    ['2002.10', 'C'],
    ['2002.11', 'B'],
    ['2002.12', 'A'],
    ['2003.1', 'C'],
    ['2003.2', 'A'],
    ['2003.3', 'B'],
    ['2003.4', 'A'],
    ['2003.5', 'C'],
    ['2003.6', 'B'],
    ['2003.7', 'C'],
    ['2003.8', 'D'],
    ['2003.9', 'B'],
    ['2003.10', 'B'],
    ['2003.11', 'D'],
    ['2003.12', 'A'],
    ['2004.1', 'B'],
    ['2004.2', 'B'],
    ['2004.3', 'B'],
    ['2004.4', 'B'],
    ['2004.5', 'C'],
    ['2004.6', 'C'],
    ['2004.7', 'C'],
    ['2004.8', 'C'],
    ['2004.9', 'C'],
    ['2004.10', 'C'],
    ['2004.11', 'C'],
    ['2004.12', 'C'],
    ['2005.1', 'C'],
    ['2005.2', 'A'],
    ['2005.3', 'C'],
    ['2005.4', 'A'],
    ['2005.5', 'C'],
    ['2005.6', 'C'],
    ['2005.7', 'B'],
    ['2005.8', 'D'],
    ['2005.9', 'C'],
    ['2005.10', 'D'],
    ['2005.11', 'C'],
    ['2005.12', 'A'],
    ['2006.1', 'D'],
    ['2006.2', 'D'],
    ['2006.3', 'A'],
    ['2006.4', 'D'],
    ['2006.5', 'A'],
    ['2006.6', 'A'],
    ['2006.7', 'A'],
    ['2006.8', 'A'],
    ['2006.9', 'D'],
    ['2006.10', 'A'],
    ['2006.11', 'D'],
    ['2006.12', 'A'],
    ['2007.1', 'A'],
    ['2007.2', 'A'],
    ['2007.3', 'B'],
    ['2007.4', 'B'],
    ['2007.5', 'B'],
    ['2007.6', 'C'],
    ['2007.7', 'B'],
    ['2007.8', 'A'],
    ['2007.9', 'D'],
    ['2007.10', 'B'],
    ['2007.11', 'B'],
    ['2007.12', 'B'],
    ['2008.1', 'A'],
    ['2008.2', 'B'],
    ['2008.3', 'C'],
    ['2008.4', 'C'],
    ['2008.5', 'B'],
    ['2008.6', 'D'],
    ['2008.7', 'B'],
    ['2008.8', 'B'],
    ['2008.9', 'A'],
    ['2008.10', 'A'],
    ['2008.11', 'B'],
    ['2008.12', 'B'],
    ['2009.1', 'A'],
    ['2009.2', 'A'],
    ['2009.3', 'A'],
    ['2009.4', 'C'],
    ['2009.5', 'C'],
    ['2009.6', 'C'],
    ['2009.7', 'C'],
    ['2009.8', 'C'],
    ['2009.9', 'B'],
    ['2009.10', 'C'],
    ['2009.11', 'A'],
    ['2009.12', 'D'],
    ['2010.1', 'C'],
    ['2010.2', 'B'],
    ['2010.3', 'D'],
    ['2010.4', 'D'],
    ['2010.5', 'D'],
    ['2010.6', 'D'],
    ['2010.7', 'D'],
    ['2010.8', 'D'],
    ['2010.9', 'D'],
    ['2010.10', 'D'],
    ['2010.11', 'D'],
    ['2010.12', 'B'],
    ['2011.1', 'D'],
    ['2011.2', 'B'],
    ['2011.3', 'D'],
    ['2011.4', 'D'],
    ['2011.5', 'D'],
    ['2011.6', 'C'],
    ['2011.7', 'A'],
    ['2011.8', 'A'],
    ['2011.9', 'A'],
    ['2011.10', 'A'],
    ['2011.11', 'C'],
    ['2011.12', 'A'],
    ['2012.1', 'A'],
    ['2012.2', 'B'],
    ['2012.3', 'A'],
    ['2012.4', 'A'],
    ['2012.5', 'C'],
    ['2012.6', 'A'],
    ['2012.7', 'A'],
    ['2012.8', 'D'],
    ['2012.9', 'B'],
    ['2012.10', 'B'],
    ['2012.11', 'B'],
    ['2012.12', 'D'],
    ['2013.1', 'B'],
    ['2013.2', 'A'],
    ['2013.3', 'D'],
    ['2013.4', 'A'],
    ['2013.5', 'B'],
    ['2013.6', 'C'],
    ['2013.7', 'B'],
    ['2013.8', 'C'],
    ['2013.9', 'C'],
    ['2013.10', 'B'],
    ['2013.11', 'C'],
    ['2013.12', 'B'],
    ['2014.1', 'B'],
    ['2014.2', 'C'],
    ['2014.3', 'C'],
    ['2014.4', 'C'],
    ['2014.5', 'C'],
    ['2014.6', 'D'],
    ['2014.7', 'C'],
    ['2014.8', 'C'],
    ['2014.9', 'D'],
    ['2014.10', 'C'],
    ['2014.11', 'A'],
    ['2014.12', 'D'],
    ['2015.1', 'D'],
    ['2015.2', 'C'],
    ['2015.3', 'D'],
    ['2015.4', 'D'],
    ['2015.5', 'C'],
    ['2015.6', 'B'],
    ['2015.7', 'D'],
    ['2015.8', 'C'],
    ['2015.9', 'B'],
    ['2015.10', 'D'],
    ['2015.11', 'C'],
    ['2015.12', 'A'],
    ['2016.1', 'A'],
    ['2016.2', 'C'],
    ['2016.3', 'A'],
    ['2016.4', 'A'],
    ['2016.5', 'A'],
    ['2016.6', 'A'],
    ['2016.7', 'A'],
    ['2016.8', 'C'],
    ['2016.9', 'D'],
    ['2016.10', 'A'],
    ['2016.11', 'C'],
    ['2016.12', 'A'],
    ['2017.1', 'A'],
    ['2017.2', 'A'],
    ['2017.3', 'D'],
    ['2017.4', 'A'],
    ['2017.5', 'B'],
    ['2017.6', 'B'],
    ['2017.7', 'B'],
    ['2017.8', 'D'],
    ['2017.9', 'A'],
    ['2017.10', 'B'],
    ['2017.11', 'B'],
    ['2017.12', 'B'],
    ['2018.1', 'D'],
    ['2018.2', 'D'],
    ['2018.3', 'B'],
    ['2018.4', 'B'],
    ['2018.5', 'B'],
    ['2018.6', 'B'],
    ['2018.7', 'B'],
    ['2018.8', 'D'],
    ['2018.9', 'D'],
    ['2018.10', 'B'],
    ['2018.11', 'B'],
    ['2018.12', 'A'],
    ['2019.1', 'C'],
    ['2019.2', 'A'],
    ['2019.3', 'C'],
    ['2019.4', 'C'],
    ['2019.5', 'D'],
    ['2019.6', 'C'],
    ['2019.7', 'C'],
    ['2019.8', 'C'],
    ['2019.9', 'C'],
    ['2019.10', 'C'],
    ['2019.11', 'C'],
    ['2019.12', 'B'],
    ['2020.1', 'B'],
    ['2020.2', 'D'],
    ['2020.3', 'D'],
    ['2020.4', 'A'],
    ['2020.5', 'D'],
    ['2020.6', 'D'],
    ['2020.7', 'D'],
    ['2020.8', 'D'],
    ['2020.9', 'D'],
    ['2020.10', 'A'],
    ['2020.11', 'D'],
    ['2020.12', 'D'],
    ['2021.1', 'D'],
    ['2021.2', 'B'],
    ['2021.3', 'A'],
    ['2021.4', 'A'],
    ['2021.5', 'A'],
    ['2021.6', 'A'],
    ['2021.7', 'A'],
    ['2021.8', 'A'],
    ['2021.9', 'D'],
    ['2021.10', 'A'],
    ['2021.11', 'A'],
    ['2021.12', 'D'],
    ['2022.1', 'D'],
    ['2022.2', 'A'],
    ['2022.3', 'A'],
    ['2022.4', 'A'],
    ['2022.5', 'A'],
    ['2022.6', 'B'],
    ['2022.7', 'B'],
    ['2022.8', 'B'],
    ['2022.9', 'D'],
    ['2022.10', 'B'],
    ['2022.11', 'B'],
    ['2022.12', 'B'],
    ['2023.1', 'B'],
    ['2023.2', 'A'],
    ['2023.3', 'B'],
    ['2023.4', 'B'],
    ['2023.5', 'A'],
    ['2023.6', 'A'],
    ['2023.7', 'B'],
    ['2023.8', 'B'],
    ['2023.9', 'C'],
    ['2023.10', 'B'],
    ['2023.11', 'C'],
    ['2023.12', 'C'],
    ['2024.1', 'B'],
    ['2024.2', 'C'],
    ['2024.3', 'C'],
    ['2024.4', 'C'],
    ['2024.5', 'B'],
    ['2024.6', 'C'],
    ['2024.7', 'B'],
    ['2024.8', 'D'],
    ['2024.9', 'C'],
    ['2024.10', 'C'],
    ['2024.11', 'B'],
    ['2024.12', 'C']
]

# 解析日期并组织数据
categories = {'A': [], 'B': [], 'C': [], 'D': []}
for date_str, category in data:
    year, month = map(int, date_str.split('.'))
    date = datetime.date(year, month, 1)
    if categories[category] and (datetime.date.fromordinal(categories[category][-1][0]) + datetime.timedelta(days=categories[category][-1][1]*30)) == date:
        categories[category][-1][1] += 1
    else:
        categories[category].append([date.toordinal(), 1])

# 设置颜色和行位置
color_map = {'A': '#FF6347', 'B': '#4682B4', 'C': '#3CB371', 'D': '#FFA500'}
base_position = 5
spacing = 1.5
y_positions = {category: base_position + i * spacing for i, category in enumerate('ABCD')}

# 绘图
fig, ax = plt.subplots(figsize=(15, 6))
for category, ranges in categories.items():
    for start, length in ranges:
        ax.broken_barh([(start, length * 30)], (y_positions[category], 1), facecolors=color_map[category])

# 设置图表
ax.set_ylim(4, 12)
# 设置图表的x轴范围以覆盖所有数据
ax.set_xlim(datetime.date(1990, 1, 1).toordinal(), datetime.date(2024, 12, 31).toordinal())
# 由于数据跨度很大，可能需要调整x轴的刻度显示，使其更易读
ax.xaxis.set_major_locator(matplotlib.dates.YearLocator(5))  # 每5年显示一次年份
ax.xaxis.set_minor_locator(matplotlib.dates.YearLocator(1))  # 每年显示一个小刻度
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%Y'))  # 设置年份格式
ax.set_yticks([y + 0.5 for y in y_positions.values()], labels=y_positions.keys())
ax.set_xlabel('日期')
ax.set_title('按月份分类表示')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()