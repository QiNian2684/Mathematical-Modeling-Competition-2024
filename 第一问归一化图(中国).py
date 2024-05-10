import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# 数据
years = np.array([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
gdp_growth_rate = np.array([0.457186637, 0.424145737, 0.558952279, 0.769761668, 0.682011988, 0.742828341, 1, 0.788373164, 0.397233552, 0.790574628, 0.797015001, 0.449599162, 0.437436993, 0.369676639, 0.304902187, 0.361839937, 0.497064488, 0.454254963, 0.31684102, 0.118793509, 0.579871296])

# 通胀率数据
inflation_years = np.array([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
inflation_rate = np.array([0.161899604, 0.01493688, 0.29009699, 0.689174267, 0.386100619, 0.367311296, 0.835978387, 1, 0.015386049, 0.593022554, 0.940999076, 0.509932672, 0.503457534, 0.427490327, 0.351478551, 0.436990316, 0.347799195, 0.40835677, 0.552160049, 0.491748237, 0.248856866])

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
