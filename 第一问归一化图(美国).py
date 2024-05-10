import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# GDP增长率数据
years = np.array([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
gdp_growth_rate = np.array([0.41040559, 0.41450676, 0.53629448, 0.67942001, 0.68637555, 0.62533691, 0.53174012, 0.31683953, 0, 0.46676035, 0.44438848, 0.48650402, 0.44168689, 0.48700976, 0.45024969, 0.36762828, 0.4857518, 0.5832227, 0.48141754, 0.03758712, 1, 0.88217985, 0.61628423, 0])

# 通胀率数据
inflation_years = np.array([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
inflation_rate = np.array([0.37740235, 0.23051205, 0.31500734, 0.35946979, 0.44347526, 0.42618223, 0.3838895, 0.49750808, 0, 0.23543261, 0.41626443, 0.28796136, 0.21490843, 0.23289338, 0.05311505, 0.19101408, 0.29496974, 0.33197079, 0.2566896, 0.18882788, 0.60184285, 1, 0.53520231, 0.40313264])

# 排序数据
sorted_indices = np.argsort(years)
sorted_years = years[sorted_indices]
sorted_gdp_growth_rate = gdp_growth_rate[sorted_indices]

sorted_indices_inflation = np.argsort(inflation_years)
sorted_inflation_years = inflation_years[sorted_indices_inflation]
sorted_inflation_rate = inflation_rate[sorted_indices_inflation]

# 创建平滑曲线
spl_gdp = make_interp_spline(sorted_years, sorted_gdp_growth_rate)
years_smooth = np.linspace(sorted_years.min(), sorted_years.max(), 200)
gdp_growth_rate_smooth = spl_gdp(years_smooth)

spl_inflation = make_interp_spline(sorted_inflation_years, sorted_inflation_rate)
inflation_years_smooth = np.linspace(sorted_inflation_years.min(), sorted_inflation_years.max(), 200)
inflation_rate_smooth = spl_inflation(inflation_years_smooth)

# 限制年份到2021
years_smooth_limited = years_smooth[years_smooth <= 2021]
gdp_growth_rate_smooth_limited = gdp_growth_rate_smooth[:len(years_smooth_limited)]

inflation_years_smooth_limited = inflation_years_smooth[inflation_years_smooth <= 2021]
inflation_rate_smooth_limited = inflation_rate_smooth[:len(inflation_years_smooth_limited)]


# 绘图
plt.figure(figsize=(25, 8))
plt.plot(years_smooth_limited, gdp_growth_rate_smooth_limited, label='经济指标', color='blue')
plt.plot(inflation_years_smooth_limited, inflation_rate_smooth_limited, label='通胀数据', color='green')
plt.xlabel('年份', fontsize=25, fontproperties='SimHei')
plt.ylabel('归一化指标', fontsize=25, fontproperties='SimHei')
plt.xticks(fontsize=25)
plt.yticks([0, 0.5, 1], fontsize=25)
plt.axhline(y=0.5, linestyle='--', color='red')
plt.legend(prop={'family': 'SimHei', 'size': 25})
plt.grid(True)

# 调整布局
plt.tight_layout(pad=2.0)
plt.show()
