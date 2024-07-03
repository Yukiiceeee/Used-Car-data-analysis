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

# 按品牌和日期分组，计算平均价格
average_prices = Train_data.groupby(['brand', 'creatDate'])['price'].mean().reset_index()


# 定义一个更复杂的拟合函数，例如四次多项式
def complex_poly_fit(x, a, b, c, d, e):
    return a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e


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

# 获取所有品牌的唯一值
brands = average_prices['brand'].unique()

# 遍历每个品牌，生成独立的图表
for brand in brands:
    brand_data = average_prices[average_prices['brand'] == brand]
    brand_data.sort_values('creatDate', inplace=True)

    # 将日期转换为数字格式，便于拟合
    xdata = (brand_data['creatDate'] - brand_data['creatDate'].min()).dt.days
    ydata = brand_data['price']

    # 拟合曲线
    popt, _ = curve_fit(complex_poly_fit, xdata, ydata)

    # 生成拟合曲线的y值
    x_fit = np.linspace(xdata.min(), xdata.max(), 100)
    y_fit = complex_poly_fit(x_fit, *popt)

    # 创建独立的图表
    plt.figure(figsize=(14, 8))

    # 绘制面积图
    plt.fill_between(brand_data['creatDate'].min() + pd.to_timedelta(x_fit, unit='D'), y_fit, alpha=0.5,
                     label=f'{brand_mapping[brand]} Fitted Curve')

    # 绘制原始数据点和拟合曲线的折线图
    plt.plot(brand_data['creatDate'], ydata, 'o', linestyle='-', label=f'{brand_mapping[brand]} Original Data')
    plt.plot(brand_data['creatDate'].min() + pd.to_timedelta(x_fit, unit='D'), y_fit, '-',
             label=f'{brand_mapping[brand]} Fitted Curve')

    plt.title(f'平均价格 vs. 出售时间 for 汽车品牌 {brand_mapping[brand]}')
    plt.xlabel('出售时间')
    plt.ylabel('平均价格')
    plt.legend(title='Brand')
    plt.grid(True)

    # 保存图表到本地
    plt.savefig(path + f'price_trend_{brand_mapping[brand]}.png')
    plt.close()