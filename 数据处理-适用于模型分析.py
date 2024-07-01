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

# 对测试集处理
Test_data['used_time'] = (pd.to_datetime(Test_data['creatDate'], format='%Y%m%d', errors='coerce') -
                            pd.to_datetime(Test_data['regDate'], format='%Y%m%d', errors='coerce')).dt.days

Test_data['city'] = Test_data['regionCode'].apply(lambda x : str(x)[:-2])
# 数据分桶
bin = [i*20 for i in range(15)]
Test_data['power_bin'] = pd.cut(Test_data['power'], bin, labels=False)

Train_data['train']=1
Test_data['train']=0
data = pd.concat([Train_data, Test_data], ignore_index=True)

#删除无关特征seller,name
data.drop(['seller','name','offerType','city'],axis=1,inplace=True)

#对类别特征进行 OneEncoder
data = pd.get_dummies(data, columns=['brand', 'bodyType', 'fuelType',
                                     'gearbox', 'notRepairedDamage', 'power_bin'],dtype=int)



Train_data=data[data['train']==1]
Test_data=data[data['train']==0]

# 相关特征
numeric_features = ['power', 'kilometer', 'v_0', 'v_1', 'v_2', 'v_3',
                    'v_4', 'v_5', 'v_6', 'v_7', 'v_8', 'v_9',
                    'v_10', 'v_11', 'v_12', 'v_13', 'v_14', 'price']
# 计算数值特征之间的相关系数矩阵
correlation_matrix = Train_data[numeric_features].corr()

# 绘制热力图
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()

train_columns=Train_data.columns
test_columns=Test_data.columns

# #归一化
transformers = MinMaxScaler((0,1))
Train_data = transformers.fit_transform(Train_data)
Test_data = transformers.fit_transform(Test_data)

Train_data=pd.DataFrame(Train_data,columns=train_columns)
Test_data=pd.DataFrame(Test_data,columns=test_columns)

Train_data=Train_data.drop(['SaleID','regDate','creatDate','regionCode','model','bodyType_未知','gearbox_未知','fuelType_未知',
                            'price_bin','train','notRepairedDamage_未知','power'],axis=1)
Test_data=Test_data.drop(['SaleID','regDate','creatDate','regionCode','model','bodyType_未知','gearbox_未知','fuelType_未知',
                            'price_bin','train','notRepairedDamage_未知','power'],axis=1)


# 特征筛选 ---相关性分析 特征提取，特征选择


Train_data.to_csv(path+'模型构建所用数据-train.csv')
Test_data.to_csv(path+'模型构建所用数据-test.csv')

