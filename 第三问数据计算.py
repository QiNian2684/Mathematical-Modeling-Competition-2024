import pandas as pd
import numpy as np

# 从Excel文件中读取数据
df = pd.read_excel('D:/桌面/问题三数据/2010.10.18-2011.08 过热.xlsx', parse_dates=['日期'])

# 计算各资产类别的日收益率
returns = df.iloc[:, 1:].pct_change().dropna()

# 计算日期望收益率和日方差
expected_daily_returns = returns.mean()
variance_daily_returns = returns.var()

# 计算年期望收益率和年方差
annual_returns = (1 + expected_daily_returns) ** 252 - 1
annual_variance_returns = variance_daily_returns * 252

# 打印结果
print("日期望收益率:")
print(expected_daily_returns)
print("\n日方差:")
print(variance_daily_returns)
print("\n年期望收益率:")
print(annual_returns)
print("\n年方差:")
print(annual_variance_returns)
