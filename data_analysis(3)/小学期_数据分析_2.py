import pandas as pd
import matplotlib.pyplot as plt

# 读取包含品牌和价格列的数据集
data = pd.read_csv("/Used-Car-data-analysis/data/数据分析所用数据.csv")

# 按照品牌对价格进行分组
grouped = data.groupby('brand')['price'].apply(list).reset_index(name='prices')
print(grouped)
# 设置中文字体
plt.rcParams['font.family'] = 'SimHei'
# 绘制箱线图
plt.figure(figsize=(12, 6))
plt.boxplot(grouped['prices'], labels=grouped['brand'])
plt.title('不同品牌二手车价格箱线图')
plt.xlabel('品牌')
plt.ylabel('价格')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
