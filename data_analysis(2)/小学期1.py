import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
## 1) 载入训练集和测试集；
path = 'C:/Users/王斯哲/PycharmProjects/pythonProject/'
Train_data = pd.read_csv(path+'used_car_train_20200313.csv', sep=' ')
Test_data = pd.read_csv(path+'used_car_testB_20200421.csv', sep=' ')

print('Train data shape:',Train_data.shape)
print('TestA data shape:',Test_data.shape)

print(Train_data.head())
user_num =  len(Train_data['brand'].unique())
print("品牌总数为:",user_num)

# 计算客户交易次数
user_counts =  Train_data['brand'].value_counts()
print("每个品牌的二手车数量为:\n",user_counts)