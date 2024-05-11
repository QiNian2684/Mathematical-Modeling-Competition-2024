import pandas as pd
from datetime import datetime
from sklearn.ensemble import RandomForestRegressor

# 读取数据
df = pd.read_excel('金价.xlsx', parse_dates=['日期'])

# 检查金价列的数据类型，并适当处理
if df['金价'].dtype == 'object':
    df['金价'] = df['金价'].str.replace(',', '').astype(float)
else:
    df['金价'] = pd.to_numeric(df['金价'], errors='coerce')  # 强制转换，非数字变为NaN

# 设置日期范围
start_date = datetime(2004, 1, 1)
end_date = datetime(2022, 6, 30)
all_dates = pd.date_range(start=start_date, end=end_date, freq='D')

# 将日期设置为索引
df.set_index('日期', inplace=True)

# 重新索引，填充缺失的日期
df = df.reindex(all_dates)

# 分离出有缺失值的行和无缺失值的行，并创建副本以安全地修改
df_complete = df.dropna().copy()
df_missing = df[df.isnull().any(axis=1)].copy()

# 提取日期作为特征
df_complete['Day'] = df_complete.index.day
df_complete['Month'] = df_complete.index.month
df_complete['Year'] = df_complete.index.year

df_missing['Day'] = df_missing.index.day
df_missing['Month'] = df_missing.index.month
df_missing['Year'] = df_missing.index.year

# 使用随机森林模型填补缺失值
X_train = df_complete[['Day', 'Month', 'Year']]
y_train = df_complete['金价']
X_missing = df_missing[['Day', 'Month', 'Year']]

model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(X_train, y_train)
predicted_values = model.predict(X_missing)

df.loc[df_missing.index, '金价'] = predicted_values

# 重置索引，使日期再次成为一列
df.reset_index(inplace=True)
df.rename(columns={'index': '日期'}, inplace=True)

# 确保日期格式为年-月-日（不带时间）
df['日期'] = df['日期'].dt.strftime('%Y-%m-%d')

# 输出到新的Excel文件
df.to_excel('金价(处理后).xlsx', index=False)
