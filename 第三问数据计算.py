import pandas as pd
import numpy as np
import glob
import os
import xlsxwriter

# 定义无风险利率和基准年化回报率
risk_free_rate = 0.017
benchmark_return = 0.0917

# 设置文件目录路径
folder_path = '分段表格'

# 获取该目录下所有的Excel文件
excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

# 初始化一个空的DataFrame来收集结果
all_data = pd.DataFrame()

# 确保读取了所有文件
if not excel_files:
    print("没有找到Excel文件，请检查路径。")
else:
    # 逐个读取文件
    for file in excel_files:
        # 读取数据
        df = pd.read_excel(file, parse_dates=['日期'])

        # 计算各资产类别的日收益率
        returns = df.iloc[:, 1:].pct_change().dropna()

        # 计算日望收益率和日方差
        expected_daily_returns = returns.mean()
        variance_daily_returns = returns.var()

        # 计算年期望收益率和年方差
        annual_returns = (1 + expected_daily_returns) ** 365 - 1
        annual_variance_returns = variance_daily_returns * 365
        std_dev_annual_returns = np.sqrt(annual_variance_returns)

        # 计算夏普比率
        sharpe_ratio = (annual_returns - risk_free_rate) / std_dev_annual_returns

        # 计算索提诺比率
        negative_returns = returns[returns < 0]
        semi_deviation = np.sqrt(negative_returns.var() * 365)
        sortino_ratio = (annual_returns - risk_free_rate) / semi_deviation

        # 计算信息比率
        tracking_error = np.sqrt((returns - benchmark_return) ** 2).mean() * np.sqrt(365)
        information_ratio = (annual_returns - benchmark_return) / tracking_error

        # 文件名作为DataFrame的标签
        file_name = os.path.basename(file).split('.')[0]  # 去除路径和文件扩展名

        # 为每个资产类别生成一行数据
        for asset in df.columns[1:]:
            result_df = pd.DataFrame({
                '文件标签': f"{file_name}_{asset}",
                '日望收益率': [expected_daily_returns[asset]],
                '年期望收益率': [annual_returns[asset]],
                '日方差': [variance_daily_returns[asset]],
                '年方差': [annual_variance_returns[asset]],
                '日标准差': [std_dev_annual_returns[asset]],
                '年标准差': [std_dev_annual_returns[asset]],
                '夏普比率': [sharpe_ratio[asset]],
                '索提诺比率': [sortino_ratio[asset]],
                '信息比率': [information_ratio[asset]]
            })

            # 将结果添加到总DataFrame中
            all_data = pd.concat([all_data, result_df], axis=0)

    # 将所有结果保存到一个Excel文件中
    output_path = '汇总分析结果.xlsx'
    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        all_data.to_excel(writer, index=False, sheet_name='Analysis Results')

        # 获取工作表和工作簿对象
        workbook = writer.book
        worksheet = writer.sheets['Analysis Results']

        # 设置列的格式
        format = workbook.add_format({'num_format': '0.###############'})
        worksheet.set_column('B:K', None, format)

    print("所有文件已分析完毕并汇总到一个Excel文件。")
