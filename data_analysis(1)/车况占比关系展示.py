import pandas as pd
from collections import Counter
from pyecharts import options as opts
from pyecharts.charts import Bar

# 读取CSV文件，请替换为你的实际文件路径
df = pd.read_csv('data.csv')

# 数据预处理：筛选需要的列
data = df[['brand', 'bodyType', 'kilometer', 'price']]

# 选择分析的关键属性
categories = ['brand', 'bodyType', 'kilometer']

# 创建柱状图并保存为HTML文件
def plot_and_save_bar_chart(category):
    counter = Counter(data[category])
    top_items = counter.most_common(6)  # 取出占比最多的前6数据

    # 如果是公里数，按照数值从大到小排序
    if category == 'kilometer':
        top_items = sorted(top_items, key=lambda x: x[0], reverse=True)
    else:
        top_items = list(reversed(top_items))  # 其他类别从低到高排序

    x_data = [item[0] for item in top_items]
    y_data = [item[1] for item in top_items]

    # 替换标题中的英文部分
    if category == 'brand':
        title = "Top 6 品牌和价格之间的关系"
        xaxis_name = '品牌'
    elif category == 'bodyType':
        title = "Top 6 车型和价格之间的关系"
        xaxis_name = '车型'
        # 将5.0至0.0映射为车型名称
        x_data = ['小型车', '中型车', '中型SUV', '小型MPV', '大型MPV', '跑车']
    elif category == 'kilometer':
        title = "Top 6 公里数和价格之间的关系"
        xaxis_name = '公里数'
    else:
        title = "Top 6 数据和价格之间的关系"
        xaxis_name = '数据'

    bar = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis("数量", y_data)
        .set_global_opts(
            title_opts=opts.TitleOpts(title=title),
            xaxis_opts=opts.AxisOpts(name=xaxis_name),
            yaxis_opts=opts.AxisOpts(name='数量')
        )
    )

    # 保存为HTML文件
    bar.render(f"Top6_{category}_价格关系.html")

# 逐个生成和保存柱状图
for category in categories:
    plot_and_save_bar_chart(category)
