import pandas as pd

# 假设原始数据表格的路径
file_path = '问题三数据(处理后).xlsx'

# 读取数据
data = pd.read_excel(file_path, parse_dates=['日期'])

# 将日期列格式化为 YYYY-MM-DD，忽略时分秒
data['日期'] = data['日期'].dt.date

# 定义各个状态的时间段
periods = [
    {"start": "2004-01", "end": "2004-07", "status": "过热"},
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
    {"start": "2021-02", "end": "2022-06-30", "status": "衰退"}
]

# 遍历每个状态，过滤数据，并保存为新的Excel文件
for period in periods:
    # 转换起止时间为date对象
    start_date = pd.to_datetime(period['start']).date()
    end_date = pd.to_datetime(period['end']).date()

    # 过滤数据
    mask = (data['日期'] >= start_date) & (data['日期'] <= end_date)
    status_data = data.loc[mask]

    # 定义新文件的名称
    file_name = f"{period['start'].replace('-', '')}_{period['end'].replace('-', '')}_{period['status']}.xlsx"
    file_path = f"分段表格/{file_name}"

    # 将过滤后的数据保存到新的Excel文件
    status_data.to_excel(file_path, index=False)
    print(f"文件'{file_name}'已保存。")
