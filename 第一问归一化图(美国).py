import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import PchipInterpolator

size = 32


# 数据初始化
years = np.array([
    2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
    2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,
    2020, 2021, 2022, 2023
])
gdp_growth_rate_normalized = np.array([
    0.663242269, 0.410405593, 0.41450676, 0.536294483, 0.679420008,
    0.68637555, 0.625336912, 0.531740118, 0.316839532, 0,
    0.466760351, 0.444388482, 0.586504024, 0.541686894, 0.487009762,
    0.450249686, 0.367628276, 0.485751803, 0.583222704, 0.481417537,
    0.03758712, 1, 0.882179854, 0.616284232
])
inflation_rate_normalized = np.array([
    0.444043321, 0.377858002, 0.231046931, 0.315282792, 0.359807461,
    0.444043321, 0.42599278, 0.38387485, 0.596991576, 0,
    0.235860409, 0.416365824, 0.287605295, 0.215403129, 0.23345367,
    0.052948255, 0.19133574, 0.294825511, 0.332129964, 0.25631769,
    0.188929001, 0.601684717, 1, 0.535499398
])

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
