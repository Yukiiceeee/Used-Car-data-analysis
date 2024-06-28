#根据汽车开始售卖时间，统计分析某品牌汽车的平均价格变化趋势
import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件到DataFrame
file_path = "data_1.csv"  # 替换为你的CSV文件路径
df = pd.read_csv(file_path)

print('Train data shape:',df.shape)
print('TestA data shape:',df.shape)

print(df.head())
user_num =  len(df['brand'].unique())
print("品牌总数为:",user_num)

# 计算客户交易次数
user_counts =  df['brand'].value_counts()
print("每个品牌的二手车数量为:\n",user_counts)