import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 载入训练集和测试集；
path = './data/'
Train_data = pd.read_csv(path+'data_数据清洗.csv')
Test_data = pd.read_csv(path+'used_car_testB_20200421.csv', sep=' ')


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

#删除无关特征seller,name
data.drop(['seller','name','offerType','city'],axis=1,inplace=True)

 #对类别特征进行 OneEncoder
data = pd.get_dummies(data, columns=['brand', 'bodyType', 'fuelType',
                                     'gearbox', 'notRepairedDamage', 'power_bin'],dtype=int)

# #归一化
# transformers = MinMaxScaler()
# data = transformers.fit_transform(data)


Train_data=data[data['train']==1]
Test_data=data[data['train']==0]





# 特征筛选 ---相关性分析 特征提取，特征选择

Train_data.to_csv(path+'模型构建所用数据-train.csv')
Test_data.to_csv(path+'模型构建所用数据-test.csv')

