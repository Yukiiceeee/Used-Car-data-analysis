import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie
from pyecharts.commons.utils import JsCode

# 读取数据
path = 'C:/Users/王斯哲/PycharmProjects/pythonProject/'
data = pd.read_csv(path + 'data_1.csv')

# 品牌映射
brand_mapping = {
    0: '揽胜极光', 1: 'Panamera', 2: '奔驰B级', 3: '宝马3系', 4: '奥迪A6L',
    5: '凯迪拉克XTS', 6: '别克GL8', 7: '探界者', 8: '蒙迪欧', 9: '奔驰GLC',
    10: '凯迪拉克XT5', 11: '别克GL8', 12: '奔驰M级', 13: '宝马M4', 14: '雷克萨斯IS',
    15: '捷豹XEL', 16: '奥迪A4L', 17: '凯迪拉克XT5', 18: 'MINI', 19: '本田CR-V',
    20: '凯迪拉克XTS', 21: '奔驰R级', 22: 'Cayman', 23: '奔驰C级(进口)', 24: '奔驰GL级',
    25: '宝马5系', 26: '朗逸', 27: '捷达', 28: '宝马3系', 29: '奔驰V级',
    30: '奔驰C级', 31: 'MINI', 32: '天籁', 33: '奔驰GLB', 34: '揽胜',
    35: '奔驰GLC', 36: '奥迪A6L', 37: '奔驰GLC', 38: '揽胜运动版', 39: '沃尔沃XC90'
}

# 车型映射
body_type_mapping = {
    0: '豪华轿车', 1: '微型车', 2: '厢型车', 3: '大巴车', 4: '敞篷车',
    5: '双门汽车', 6: '商务车', 7: '搅拌车'
}

# 燃油类型映射
fuel_type_mapping = {
    0: '汽油', 1: '柴油', 2: '液化石油气', 3: '天然气', 4: '混合动力', 5: '其他', 6: '电动'
}

# 映射品牌、车型和燃油类型
data['brand'] = data['brand'].map(brand_mapping)
data['bodyType'] = data['bodyType'].map(body_type_mapping)
data['fuelType'] = data['fuelType'].map(fuel_type_mapping)

# 品牌交易记录数
brand_count = data['brand'].value_counts().reset_index()
brand_count.columns = ['brand', 'count']
top10_brands = brand_count.head(10).sort_values(by='count', ascending=True)

# 车型交易记录数
body_type_count = data['bodyType'].value_counts().reset_index()
body_type_count.columns = ['bodyType', 'count']

# 燃油类型交易记录数
fuel_type_count = data['fuelType'].value_counts().reset_index()
fuel_type_count.columns = ['fuelType', 'count']

# 品牌交易记录数图表
brand_bar = (
    Bar()
    .add_xaxis(top10_brands['brand'].tolist())
    .add_yaxis("交易记录数", top10_brands['count'].tolist(), category_gap="60%")
    .set_series_opts(
        itemstyle_opts={
            "normal": {
                "color": JsCode(
                    """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(0, 244, 255, 1)'
            }, {
                offset: 1,
                color: 'rgba(0, 77, 167, 1)'
            }], false)"""
                ),
                "barBorderRadius": [30, 30, 30, 30],
                "shadowColor": "rgb(0, 160, 221)",
            }
        }
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="前十品牌交易记录数"),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45))
    )
    .render("brand_bar.html")
)

# 车型交易记录数图表
body_type_pie = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(body_type_count['bodyType'].tolist(), body_type_count['count'].tolist())],
        radius=["40%", "75%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="车型交易记录数"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("body_type_pie.html")
)

# 燃油类型交易记录数图表
fuel_type_pie = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(fuel_type_count['fuelType'].tolist(), fuel_type_count['count'].tolist())],
        radius=["40%", "75%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="燃油类型交易记录数"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("fuel_type_pie.html")
)
