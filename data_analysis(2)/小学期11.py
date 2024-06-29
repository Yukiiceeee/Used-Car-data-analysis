
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Bar3D

# Load the updated CSV file
path = 'C:/Users/王斯哲/PycharmProjects/pythonProject/'
file_path = path + 'k_values_with_scores.csv'

df = pd.read_csv(file_path)

# Aggregate scores by brand and fuelType
df_agg = df.groupby(['brand', 'fuelType']).agg({'score': 'sum'}).reset_index()

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
        xaxis3d_opts=opts.Axis3DOpts(type_="category", data=brands),
        yaxis3d_opts=opts.Axis3DOpts(type_="category", data=fuel_types),
        zaxis3d_opts=opts.Axis3DOpts(type_="value"),
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
bar3d.render("bar3d_brand_fueltype_scores.html")