import pandas as pd
import matplotlib.pyplot as plt

# 1. 读取数据
df = pd.read_csv('/Used-Car-data-analysis/data/data_数据清洗.csv', parse_dates=['creatDate'], date_format=lambda x: pd.to_datetime(str(x), format='%Y%m%d'))

# 2. 确保creatDate列是日期格式
df['creatDate'] = pd.to_datetime(df['creatDate'], format='%Y%m%d')

# 3. 筛选2016年3月至2016年4月的数据
df_filtered = df[(df['creatDate'] >= '2016-03-01') & (df['creatDate'] <= '2016-04-30')]

# 4. 按日期分组并计算每个日期的交易记录数
daily_sales = df_filtered.groupby('creatDate')['creatDate'].count().reset_index(name='count')

# 5. 可视化展示
plt.figure(figsize=(12, 6))
plt.plot(daily_sales['creatDate'], daily_sales['count'], marker='o')
plt.title('Sales Trend of Used Cars from March to April 2016')
plt.xlabel('Date')
plt.ylabel('Number of Sales')
plt.xticks(rotation=45)
plt.grid(True)  # 添加网格线以便更清晰地查看趋势
plt.show()
