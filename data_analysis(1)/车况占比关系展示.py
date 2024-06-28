import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'SimHei'
# 读取CSV文件
file_path = 'data_1.csv'  # 替换成你的CSV文件路径
df = pd.read_csv(file_path)


# 计算不同品牌的价格分布并选取前6
top_brands = df.groupby('brand')['price'].mean().nlargest(6)

# 计算不同型号的价格分布并选取前6
top_body_types = df.groupby('bodyType')['price'].mean().nlargest(6)

# 计算不同里程数的价格分布并选取前6
top_kilometers = df.groupby('kilometer')['price'].mean().nlargest(6)

# 绘制柱状图
plt.figure(figsize=(14, 12))

# 绘制品牌与价格关系的柱状图
plt.subplot(2, 2, 1)
top_brands.plot(kind='bar', color='skyblue')
plt.title('Top 6 品牌与价格关系')
plt.xlabel('品牌')
plt.ylabel('价格')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# 绘制型号与价格关系的柱状图
plt.subplot(2, 2, 2)
top_body_types.plot(kind='bar', color='lightgreen')
plt.title('Top 6 型号与价格关系')
plt.xlabel('型号')
plt.ylabel('价格')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()



# 绘制里程数与价格关系的柱状图
plt.subplot(2, 2, 4)
top_kilometers.plot(kind='bar', color='lightcoral')
plt.title("Top 6 '里程数与价格的关系'")
plt.xlabel('里程数')
plt.ylabel('价格')
plt.xticks(rotation=0)
plt.grid(axis='y')

plt.tight_layout()
plt.show()
