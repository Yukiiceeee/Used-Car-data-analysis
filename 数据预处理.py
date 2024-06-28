import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 载入训练集和测试集；
path = './data/'
Train_data = pd.read_csv(path+'used_car_train_20200313.csv', sep=' ')
Test_data = pd.read_csv(path+'used_car_testB_20200421.csv', sep=' ')

# 输出数据的大小信息
print('Train data shape:',Train_data.shape)
print('TestA data shape:',Test_data.shape)
# 获取数据前5行
print(Train_data.head())

print(Train_data.info())
# 通过describe()来熟悉数据的相关统计量
print(Train_data.describe(include='all'))
Train_data.describe(include='all').to_csv(path+"描述性统计.csv")

# 分离label即预测值
Y_train = Train_data['price']
# 数字特征
numeric_features = ['power', 'kilometer', 'v_0', 'v_1', 'v_2', 'v_3', 'v_4', 'v_5', 'v_6', 'v_7', 'v_8', 'v_9', 'v_10', 'v_11', 'v_12', 'v_13','v_14' ]

# # 类型特征
categorical_features = ['name', 'model', 'brand', 'bodyType', 'fuelType', 'gearbox', 'notRepairedDamage', 'regionCode',]

# 特征nunique分布
for cat_fea in categorical_features:
    # print(cat_fea + "的特征分布如下：")
    print("{}特征有个{}不同的值".format(cat_fea, Train_data[cat_fea].nunique()))
    print(Train_data[cat_fea].value_counts())


# 这里我包装了一个异常值处理的代码，可以随便调用。
def outliers_proc(data, col_name, scale=3):
    """
    用于清洗异常值，默认用 box_plot（scale=3）进行清洗
    :param data: 接收 pandas 数据格式
    :param col_name: pandas 列名
    :param scale: 尺度
    :return:
    """

    def box_plot_outliers(data_ser, box_scale):
        """
        利用箱线图去除异常值
        :param data_ser: 接收 pandas.Series 数据格式
        :param box_scale: 箱线图尺度，
        :return:
        """
        iqr = box_scale * (data_ser.quantile(0.75) - data_ser.quantile(0.25))
        val_low = data_ser.quantile(0.25) - iqr
        val_up = data_ser.quantile(0.75) + iqr
        rule_low = (data_ser < val_low)
        rule_up = (data_ser > val_up)
        return (rule_low, rule_up), (val_low, val_up)

    data_n = data.copy()
    data_series = data_n[col_name]
    rule, value = box_plot_outliers(data_series, box_scale=scale)
    index = np.arange(data_series.shape[0])[rule[0] | rule[1]]
    print("Delete number is: {}".format(len(index)))
    data_n = data_n.drop(index)
    data_n.reset_index(drop=True, inplace=True)
    print("Now column number is: {}".format(data_n.shape[0]))
    index_low = np.arange(data_series.shape[0])[rule[0]]
    outliers = data_series.iloc[index_low]
    print("Description of data less than the lower bound is:")
    print(pd.Series(outliers).describe())
    index_up = np.arange(data_series.shape[0])[rule[1]]
    outliers = data_series.iloc[index_up]
    print("Description of data larger than the upper bound is:")
    print(pd.Series(outliers).describe())

    fig, ax = plt.subplots(1, 2, figsize=(10, 7))
    sns.boxplot(y=data[col_name], data=data, palette="Set1", ax=ax[0])
    sns.boxplot(y=data_n[col_name], data=data_n, palette="Set1", ax=ax[1])
    plt.show()
    return data_n

# 我们可以删掉一些异常数据，以 power 为例。
Train_data = outliers_proc(Train_data, 'power', scale=3)
Train_data = outliers_proc(Train_data, 'kilometer', scale=3)

Train_data = outliers_proc(Train_data, 'price', scale=3)

'''---------------------'''
# 离散型特征的异常值处理，需要分别将每个特征取值分布查看
# print(Train_data['notRepairedDamage'].value_counts())
# print(Train_data['brand'].value_counts())
# print(Train_data['bodyType'].value_counts())
# print(Train_data['fuelType'].value_counts())
# print(Train_data['gearbox'].value_counts())
# print(Train_data['model'].value_counts())

Train_data['notRepairedDamage'].replace('-', np.nan, inplace=True)
''''-------'''
# # 计算特征缺失值个数
nan_count=Train_data.isnull().sum()
# 查看存在缺失值的特征
print(nan_count[nan_count > 0].sort_values(ascending=False))

filling_columns = nan_count[nan_count > 0].index
for column in filling_columns:
    Train_data[column].fillna('未知', inplace=True)
Train_data.dropna(subset=['model'], inplace=True)
# print(Train_data.head())
# Train_data.dropna(subset=nan_count[nan_count > 0].index, inplace=True)


'''
Train_data['train']=1
Test_data['train']=0
data = pd.concat([Train_data, Test_data], ignore_index=True)
'''

data=Train_data
# 使用时间：data['creatDate'] - data['regDate']，反应汽车使用时间，一般来说价格与使用时间成反比
# 不过要注意，数据里有时间出错的格式，所以我们需要 errors='coerce'

data['used_time'] = (pd.to_datetime(data['creatDate'], format='%Y%m%d', errors='coerce') -
                            pd.to_datetime(data['regDate'], format='%Y%m%d', errors='coerce')).dt.days
# 看一下空数据，有 15k 个样本的时间是有问题的，我们可以选择删除，也可以选择放着。
# 但是这里不建议删除，因为删除缺失数据占总样本量过大，7.5%
# 我们可以先放着，因为如果我们 XGBoost 之类的决策树，其本身就能处理缺失值，所以可以不用管；
data['used_time'].isnull().sum()

# 从邮编中提取城市信息，相当于加入了先验知识
data['city'] = data['regionCode'].apply(lambda x : str(x)[:-2])
data = data

# 计算某品牌的销售统计量，同学们还可以计算其他特征的统计量
# 这里要以 train 的数据计算统计量
Train_gb = Train_data.groupby("brand")

all_info = {}
for kind, kind_data in Train_gb:
    info = {}
    kind_data = kind_data[kind_data['price'] > 0]
    info['brand_amount'] = len(kind_data)
    info['brand_price_max'] = kind_data.price.max()
    info['brand_price_median'] = kind_data.price.median()
    info['brand_price_min'] = kind_data.price.min()
    info['brand_price_sum'] = kind_data.price.sum()
    info['brand_price_std'] = kind_data.price.std()
    info['brand_price_average'] = round(kind_data.price.sum() / (len(kind_data) + 1), 2)
    all_info[kind] = info
brand_fe = pd.DataFrame(all_info).T.reset_index().rename(columns={"index": "brand"})
data = data.merge(brand_fe, how='left', on='brand')
brand_fe.to_excel(path+'品牌价格信息.xlsx')
# 数据分桶 以 power 为例
# 这时候我们的缺失值也进桶了，
# 为什么要做数据分桶呢，原因有很多，= =
# 1. 离散后稀疏向量内积乘法运算速度更快，计算结果也方便存储，容易扩展；
# 2. 离散后的特征对异常值更具鲁棒性，如 age>30 为 1 否则为 0，对于年龄为 200 的也不会对模型造成很大的干扰；
# 3. LR 属于广义线性模型，表达能力有限，经过离散化后，每个变量有单独的权重，这相当于引入了非线性，能够提升模型的表达能力，加大拟合；
# 4. 离散后特征可以进行特征交叉，提升表达能力，由 M+N 个变量编程 M*N 个变量，进一步引入非线形，提升了表达能力；
# 5. 特征离散后模型更稳定，如用户年龄区间，不会因为用户年龄长了一岁就变化

# 当然还有很多原因，LightGBM 在改进 XGBoost 时就增加了数据分桶，增强了模型的泛化性

bin = [i*10 for i in range(31)]
data['power_bin'] = pd.cut(data['power'], bin, labels=False)
print(data[['power_bin', 'power']].head())

# bin1 = [i*4 for i in range(5)]
# data['kilometer_bin'] = pd.cut(data['kilometer'], bin1, labels=False)
data['price_bin'] = pd.qcut(data['price'], q=3, labels=False)
print(data[['price_bin', 'price']].head())
# data.dropna(subset=['price_bin'], inplace=True)
print(data.shape)
print(data.columns)


data.to_csv(path+'data_数据清洗.csv', index=0)



mappingBrand = {
    0: '揽胜极光',
    1: 'Panamera',
    2: '奔驰B级',
    3: '宝马3系',
    4: '奥迪A6L',
    5: '凯迪拉克XTS',
    6: '别克GL8',
    7: '探界者',
    8: '蒙迪欧',
    9: '奔驰GLC',
    10: '凯迪拉克XT5',
    11: '别克GL8',
    12: '奔驰M级',
    13: '宝马M4',
    14: '雷克萨斯IS',
    15: '捷豹XEL',
    16: '奥迪A4L',
    17: '凯迪拉克XT5',
    18: 'MINI',
    19: '本田CR-V',
    20: '凯迪拉克XTS',
    21: '奔驰R级',
    22: 'Cayman',
    23: '奔驰C级(进口)',
    24: '奔驰GL级',
    25: '宝马5系',
    26: '朗逸',
    27: '捷达',
    28: '宝马3系',
    29: '奔驰V级',
    30: '奔驰C级',
    31: 'MINI',
    32: '天籁',
    33: '奔驰GLB',
    34: '揽胜',
    35: '奔驰GLC',
    36: '奥迪A6L',
    37: '奔驰GLC',
    38: '揽胜运动版',
    39: '沃尔沃XC90'
}

mapping_city = {
    0: '成都',
    1: '杭州',
    2: '重庆',
    3: '北京',
    4: '临沂',
    5: '贵州',
    6: '广西',
    7: '长春',
    8: '大连',
    9: '湖南',
    10: '武汉',
    11: '枣庄',
    12: '上海',
    13: '石家庄',
    14: '温州',
    15: '浙江',
    16: '太原',
    17: '四川',
    18: '廊坊',
    19: '天津',
    20: '安徽',
    21: '厦门',
    22: '山东',
    23: '南京',
    24: '广州',
    25: '南通',
    26: '锦州',
    27: '哈尔滨',
    28: '宁波',
    29: '苏州',
    30: '新疆',
    31: '扬州',
    32: '保定',
    33: '海口',
    34: '昆明',
    35: '衢州',
    36: '吉林',
    37: '黔西南州',
    38: '东莞',
    39: '南昌',
    40: '福州',
    41: '郑州',
    42: '沈阳',
    43: '西安',
    44: '常州',
    45: '大庆',
    46: '宜昌',
    47: '佛山',
    48: '深圳',
    49: '南宁',
    50: '无锡',
    51: '绵阳',
    52: '潍坊',
    53: '南阳',
    54: '银川',
    55: '西宁',
    56: '桂林',
    57: '三亚',
    58: '长沙',
    59: '洛阳',
    60: '徐州',
    61: '唐山',
    62: '韶关',
    63: '郴州',
    64: '漳州',
    65: '绍兴',
    66: '滁州',
    67: '湖州',
    68: '宁德',
    69: '钦州',
    70: '柳州',
    71: '乌鲁木齐',
    72: '晋城',
    73: '莆田',
    74: '南阳',
    75: '潍坊',
    76: '绵阳',
    77: '无锡',
    78: '佛山',
    79: '深圳',
    80: '滁州',
    81: '湖州',
    82: '宁德',

}

# 使用 replace 方法替换 brand 列中的数字
data['brand'] = data['brand'].replace(mappingBrand)
regionCode_index=data['city'].unique()
code_mapping = {code: idx for idx, code in enumerate(regionCode_index)}
# print(data['regionCode'].unique().size())
data['city'] = data['city'].replace(code_mapping)
data['city'] = data['city'].replace(mapping_city)

data.to_csv(path+'数据分析所用数据.csv', index=0)
# 打印替换后的结果
print(data)