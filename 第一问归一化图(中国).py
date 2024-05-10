import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import PchipInterpolator

size = 32

# 数据初始化
years = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
gdp_growth_rate_normalized = np.array([0.392594454, 0.384010953, 0.34651601, 0.499495598, 0.738723883, 0.639144629, 0.70815953, 1, 0.759844207, 0.295975906, 0.762342538, 0.769650936, 0.375400787, 0.361599132, 0.284704076, 0.211197621, 0.275810957, 0.429264842, 0.380684251, 0.224745832, 0, 0.523234663, 0.102550507, 0.093132557])
inflation_rate_normalized = np.array([0, 0.161242604, 0.014792899, 0.289940828, 0.687869822, 0.386094675, 0.366863905, 0.835798817, 1, 0.314792899, 0.591715976, 0.940828402, 0.50887574, 0.50295858, 0.427514793, 0.350591716, 0.436390533, 0.347633136, 0.408284024, 0.551775148, 0.49112426, 0.24852071, 0.400887574, 0.171597633])

# 使用 PchipInterpolator 创建平滑曲线
pchip_gdp = PchipInterpolator(years, gdp_growth_rate_normalized)
years_smooth = np.linspace(years.min(), years.max(), 200)
gdp_growth_rate_smooth = pchip_gdp(years_smooth)

pchip_inflation = PchipInterpolator(years, inflation_rate_normalized)
inflation_rate_smooth = pchip_inflation(years_smooth)

# 绘图
plt.figure(figsize=(25, 8))
plt.plot(years_smooth, gdp_growth_rate_smooth, label='经济指标', color='blue')
plt.plot(years_smooth, inflation_rate_smooth, label='通胀数据', color='green')
plt.xlabel('年份', fontsize=size, fontproperties='SimHei')
plt.ylabel('归一化指标', fontsize=size, fontproperties='SimHei')
plt.xticks(years, fontsize=size, fontproperties='SimHei')
plt.yticks([0, 0.5, 1], fontsize=size)
plt.axhline(y=0.5, linestyle='--', color='red')
plt.legend(prop={'family': 'SimHei', 'size': size})
plt.grid(True)
plt.tight_layout(pad=2.0)
plt.xticks(years, fontsize=size)

# 设置横轴显示范围
plt.xlim(2000, 2023)
# 添加每两个月一条浅灰色的细实线
months = np.arange(2000, 2023, 2/12)
for month in months:
    plt.axvline(x=month, linestyle='-', color='gray', alpha=0.1)

# 调整边距以防止标签被截断
plt.tight_layout(pad=1.0)

plt.show()
