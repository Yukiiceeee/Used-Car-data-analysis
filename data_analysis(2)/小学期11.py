import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Bar3D

# Load the updated CSV file
path = 'C:/Users/王斯哲/PycharmProjects/pythonProject/'
file_path = path + 'k_values_with_scores.csv'

df = pd.read_csv(file_path)

# Aggregate scores by brand and fuelType
df_agg = df.groupby(['brand', 'fuelType']).agg({'score': 'sum'}).reset_index()

# Mappings
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
fuelType_mapping = {
    0: '汽油', 1: '柴油', 2: '液化石油气', 3: '天然气', 4: '混合动力', 5: '其他', 6: '电动'
}

# Replace numeric codes with descriptive names
df_agg['brand'] = df_agg['brand'].map(brand_mapping)
df_agg['fuelType'] = df_agg['fuelType'].map(fuelType_mapping)

# Prepare data for 3D Bar chart
brands = df_agg['brand'].unique().tolist()
fuel_types = df_agg['fuelType'].unique().tolist()

data = []
for _, row in df_agg.iterrows():
    brand_idx = brands.index(row['brand'])
    fuel_type_idx = fuel_types.index(row['fuelType'])
    data.append([brand_idx, fuel_type_idx, row['score']])

# Create Bar3D chart
bar3d = (
    Bar3D()
    .add(
        series_name="Scores",
        data=data,
        xaxis3d_opts=opts.Axis3DOpts(type_="category", data=brands, name="汽车品牌"),
        yaxis3d_opts=opts.Axis3DOpts(type_="category", data=fuel_types, name="燃油类型"),
        zaxis3d_opts=opts.Axis3DOpts(type_="value", name="总积分"),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            max_=df_agg['score'].max(),
            range_color=[
                "#313695", "#4575b4", "#74add1", "#abd9e9", "#e0f3f8",
                "#ffffbf", "#fee090", "#fdae61", "#f46d43", "#d73027", "#a50026"
            ],
        )
    )
)

# Render the chart to an HTML file
bar3d.render("bar3d_brand_fueltype_scores1.html")