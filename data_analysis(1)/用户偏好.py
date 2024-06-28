import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie

# 1. 读取CSV文件
df = pd.read_csv('data_1.csv')

# 2. 提取所需字段，并做统计分析
top_500_data = df.head(500)  # 假设您需要分析前500条数据
brand_counts = top_500_data['brand'].value_counts().head(10)  # 统计前500条数据中品牌出现次数排名前10的

# 获取要绘制的标签和值
brands = brand_counts.index.tolist()
counts = brand_counts.tolist()

# 3. 绘制Pie Chart
c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(brands, counts)],
        center=["40%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="用户偏好分析 - 品牌占比"),
        legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
    .render("user_preferences_brand_pie_chart.html")
)

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取CSV文件，假设文件名为data.csv，文件中的分隔符为制表符'\t'
df = pd.read_csv('data_1.csv', sep=',')

# 取前1000条数据作为用户的浏览记录
user_browsing_history = df.head(500)

# 分析用户偏好的车型、品牌等前十名数据
top_10_models = user_browsing_history['model'].value_counts().head(10)
top_10_brands = user_browsing_history['brand'].value_counts().head(10)

# 设置绘图风格
plt.figure(figsize=(14, 7))

# 1. 扇形图 - 车型偏好
plt.subplot(1, 2, 1)
plt.title('Top 10 Model Preferences', fontsize=16)
top_10_models.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set3', 10))
plt.axis('equal')  # 使饼图比例相等
plt.ylabel('')  # 不显示y轴标签

# 2. 扇形图 - 品牌偏好
plt.subplot(1, 2, 2)
plt.title('Top 10 Brand Preferences', fontsize=16)
top_10_brands.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set2', 10))
plt.axis('equal')  # 使饼图比例相等
plt.ylabel('')  # 不显示y轴标签

plt.tight_layout()  # 调整子图之间的间距
plt.show()

"""


"""
参数具体展示
import pandas as pd

# 读取CSV文件，假设文件名为data.csv，文件中的分隔符为制表符'\t'
# 如果分隔符是逗号或其他字符，根据实际情况调整
df = pd.read_csv('data_1.csv', sep=',')

# 取前1000条数据作为用户的浏览记录
user_browsing_history = df.head(1000)

# 分析用户偏好，例如：对价格、车型、品牌等进行统计
# 以下是一些示例分析代码，你可以根据具体需求进一步扩展和定制分析

# 1. 分析用户偏好的价格分布
price_preference = user_browsing_history['price'].describe()
print("价格偏好统计：")
print(price_preference)

# 2. 分析用户偏好的车型
model_preference = user_browsing_history['model'].value_counts()
print("\n车型偏好统计：")
print(model_preference)

# 3. 分析用户偏好的品牌
brand_preference = user_browsing_history['brand'].value_counts()
print("\n品牌偏好统计：")
print(brand_preference)

# 4. 其他可能的分析，如车龄、里程偏好等
# ...

# 可以根据具体的需求和数据特点进一步扩展分析代码
"""