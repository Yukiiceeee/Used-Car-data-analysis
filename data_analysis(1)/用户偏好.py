import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie, Bar

# 1. 读取CSV文件
df = pd.read_csv('data_1.csv')

# 2. 提取所需字段，并做统计分析
top_500_data = df.head(500)  # 假设您需要分析前500条数据

# 分析品牌
brand_counts = top_500_data['brand'].value_counts().head(10)
brands = brand_counts.index.tolist()
brand_counts = brand_counts.tolist()

# 分析车型（bodytype）
bodytype_counts = top_500_data['bodyType'].value_counts().head(10)
bodytypes = bodytype_counts.index.tolist()
bodytype_counts = bodytype_counts.tolist()

# 分析价格（price），选择特定的价格区间段
price_bins = [0, 10000, 20000, 30000, 40000, 50000, 60000]
price_labels = ['0-10000', '10001-20000', '20001-30000', '30001-40000', '40001-50000', '50001-60000']
top_500_data['price_range'] = pd.cut(top_500_data['price'], bins=price_bins, labels=price_labels)
price_counts = top_500_data['price_range'].value_counts().sort_index()

# 3. 绘制图形

# 品牌的Pie Chart
pie_brand = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(brands, brand_counts)],
        center=["25%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="用户偏好分析 - 品牌占比"),
        legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
)

# 车型的Pie Chart
pie_bodytype = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(bodytypes, bodytype_counts)],
        center=["75%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="用户偏好分析 - 车型占比"),
        legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
)

# 价格的Bar Chart
bar_price = (
    Bar()
    .add_xaxis(price_counts.index.tolist())
    .add_yaxis("价格区间", price_counts.tolist())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="用户偏好分析 - 价格分布"),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)),
    )
)

# 保存图表
pie_brand.render("品牌偏好.html")
pie_bodytype.render("车型偏好.html")
bar_price.render("价格偏好.html")


"""
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
    .render("品牌偏好.html")
)
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