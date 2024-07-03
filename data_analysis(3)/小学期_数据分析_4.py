import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. 读取CSV文件并处理日期列
df = pd.read_csv('/Used-Car-data-analysis/data/data_数据清洗.csv')
df['creatDate'] = pd.to_datetime(df['creatDate'], format='%Y%m%d')
march_2016_data = df[df['creatDate'].dt.year == 2016].loc[df['creatDate'].dt.month == 3]
# 2. 数据分析
daily_avg_prices = march_2016_data.groupby(march_2016_data['creatDate'].dt.date)['price'].mean().reset_index()
print(daily_avg_prices)

X = np.array([day.day for day in daily_avg_prices['creatDate']]).reshape(-1, 1)
y = daily_avg_prices['price'].values

# 训练线性回归模型
reg = LinearRegression().fit(X, y)

# 预测未来一个月的天数（例如，假设30天）
future_days = np.arange(1, 30).reshape(-1, 1)
future_prices = reg.predict(future_days)

# 绘制实际价格
plt.figure(figsize=(12, 6))
plt.plot(daily_avg_prices['creatDate'], daily_avg_prices['price'], marker='o', label='Actual Prices')

# 绘制预测价格
predicted_dates = pd.date_range(start='2016-04-01', periods=29).date  # 根据需要调整日期范围
plt.plot(predicted_dates, future_prices, linestyle='--', label='Predicted Prices')

# 设置图表的标签和标题
plt.xlabel('Date')
plt.ylabel('Average Price')
plt.title('Average Price of Used Cars in March 2016 and Predictions')
plt.legend()
plt.show()
