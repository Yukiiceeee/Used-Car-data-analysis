import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 载入训练集和测试集；
path = './data/'
Train_data = pd.read_csv(path+'data_数据清洗.csv')
Test_data = pd.read_csv(path+'used_car_testB_20200421.csv', sep=' ')


# 使用时间：data['creatDate'] - data['regDate']，反应汽车使用时间，一般来说价格与使用时间成反比


Test_data['used_time'] = (pd.to_datetime(Test_data['creatDate'], format='%Y%m%d', errors='coerce') -
                            pd.to_datetime(Test_data['regDate'], format='%Y%m%d', errors='coerce')).dt.days
# 从邮编中提取城市信息，相当于加入了先验知识
Test_data['city'] = Test_data['regionCode'].apply(lambda x : str(x)[:-2])


# 数据分桶
bin = [i*10 for i in range(31)]
Test_data['power_bin'] = pd.cut(Test_data['power'], bin, labels=False)



Train_data['train']=1
Test_data['train']=0
data = pd.concat([Train_data, Test_data], ignore_index=True)
data.to_csv(path+'模型构建所用数据.csv')

#删除无关特征

#归一化


# 特征筛选 ---相关性分析 特征提取，特征选择



