import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

plt.rcParams['font.family'] = 'SimHei'

# 读取数据
path = 'C:/Users/王斯哲/PycharmProjects/pythonProject/'
Train_data = pd.read_csv(path + 'data_1.csv')

# 转换日期格式
Train_data['creatDate'] = pd.to_datetime(Train_data['creatDate'], format='%Y%m%d', errors='coerce')

# 按车型和日期分组，计算平均价格
average_prices = Train_data.groupby(['bodyType', 'creatDate'])['price'].mean().reset_index()


# 定义一个更复杂的拟合函数，例如四次多项式
def complex_poly_fit(x, a, b, c, d, e):
    return a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e


# 车型映射
body_type_mapping = {
    0: '豪华轿车', 1: '微型车', 2: '厢型车', 3: '大巴车', 4: '敞篷车',
    5: '双门汽车', 6: '商务车', 7: '搅拌车'
}

# 获取所有车型的唯一值
body_types = average_prices['bodyType'].unique()

# 遍历每个车型，生成独立的图表
for body_type in body_types:
    body_type_data = average_prices[average_prices['bodyType'] == body_type]
    body_type_data.sort_values('creatDate', inplace=True)

    # 将日期转换为数字格式，便于拟合
    xdata = (body_type_data['creatDate'] - body_type_data['creatDate'].min()).dt.days
    ydata = body_type_data['price']

    # 拟合曲线
    popt, _ = curve_fit(complex_poly_fit, xdata, ydata)

    # 生成拟合曲线的y值
    x_fit = np.linspace(xdata.min(), xdata.max(), 100)
    y_fit = complex_poly_fit(x_fit, *popt)

    # 创建独立的图表
    plt.figure(figsize=(14, 8))

    # 绘制面积图
    plt.fill_between(body_type_data['creatDate'].min() + pd.to_timedelta(x_fit, unit='D'), y_fit, alpha=0.5,
                     label=f'{body_type_mapping[body_type]} Fitted Curve')

    # 绘制原始数据点和拟合曲线的折线图
    plt.plot(body_type_data['creatDate'], ydata, 'o', linestyle='-',
             label=f'{body_type_mapping[body_type]} Original Data')
    plt.plot(body_type_data['creatDate'].min() + pd.to_timedelta(x_fit, unit='D'), y_fit, '-',
             label=f'{body_type_mapping[body_type]} Fitted Curve')

    plt.title(f'平均价格 vs. 出售时间 for 车身类型 {body_type_mapping[body_type]}')
    plt.xlabel('出售时间')
    plt.ylabel('平均价格')
    plt.legend(title='Body Type')
    plt.grid(True)

    # 保存图表到本地
    plt.savefig(path + f'price_trend_{body_type_mapping[body_type]}.png')
    plt.close()