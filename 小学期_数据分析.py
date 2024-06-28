from pyecharts import options as opts
from pyecharts.charts import Map
import pandas as pd

# 读取CSV文件
df = pd.read_csv('/Users/zhouzhizhong/PycharmProjects/pythonProject/Used-Car-data-analysis/data/数据分析所用数据.csv')  # 假设CSV文件中包含城市和销量列
data = pd.DataFrame(columns=['car_counts'])
data['car_counts'] = df['city'].value_counts()
data = data.reset_index()
data['city'] = data['city'] + '市'
print(data)
# data_reset = data.reset_index(drop=False)
# print(data_reset)

# 创建地图对象，并设置城市和销量数据
m = (
    Map()
    .add(二手车数量, [list(z) for z in zip(data['city'], data['car_counts'])], china-cities, label_opts=opts.LabelOpts(is_show=False),)
    .set_global_opts(
        title_opts=opts.TitleOpts(title=各城市二手车数量地图),
        # visualmap_opts=opts.VisualMapOpts(is_piecewise=True),  # 分段颜色显示
    )
)

# 渲染地图到HTML文件
m.render(car_map.html)

