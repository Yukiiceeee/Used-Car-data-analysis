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
selected_columns = ['SaleID', 'regDate', 'creatDate','brand','notRepairedDamage']
new_Train_data = Train_data[selected_columns]

new_Train_data.loc[:, 'useDate'] = pd.to_datetime(new_Train_data['creatDate'], format='%Y%m%d', errors='coerce') - pd.to_datetime(new_Train_data['regDate'], format='%Y%m%d', errors='coerce')
new_Train_data['price'] = Train_data['price']
# 筛选品牌
new_Train_data = new_Train_data[new_Train_data['brand'] == 1]
# 打印新数据集的形状和前几行数据
print('New Train data shape:', new_Train_data.shape)
print(new_Train_data.head())
plt.figure(figsize=(10, 6))
plt.scatter(new_Train_data['useDate'].dt.days, new_Train_data['price'], alpha=0.5)
plt.title('Scatter Plot of price vs. useDate')
plt.xlabel('Days between regDate and creatDate')
plt.ylabel('Price')
plt.grid(True)
plt.show()
