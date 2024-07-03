import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie, Bar

# 1. 读取CSV文件
df = pd.read_csv('data.csv')  # 确保路径正确

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

# 映射表
bodytype_map = {
    '0.0': '小型车',
    '1.0': '中型车',
    '2.0': '中型SUV',
    '3.0': '微型车',
    '4.0': '小型MPV',
    '5.0': '大型轿车',
    '6.0': '紧凑型',
    '7.0': '跑车',
    '未知': '跑车'  # 假设 '未知' 也映射到 '跑车'
}

# 应用映射
mapped_bodytypes = [bodytype_map.get(str(bt), bt) for bt in bodytypes]

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
        center=["50%", "50%"],
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
        [list(z) for z in zip(mapped_bodytypes, bodytype_counts)],
        center=["50%", "50%"],
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
        xaxis_opts=opts.AxisOpts(
            name="价格区间",
            axislabel_opts=opts.LabelOpts(rotate=45)
        ),
        yaxis_opts=opts.AxisOpts(
            name="数量",
        )
    )
)

# 保存图表
pie_brand.render("品牌偏好.html")
pie_bodytype.render("车型偏好.html")
bar_price.render("价格偏好.html")
