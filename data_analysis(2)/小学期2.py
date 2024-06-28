import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 载入训练集和测试集
path = 'C:/Users/王斯哲/PycharmProjects/pythonProject/'
Train_data = pd.read_csv(path + 'used_car_train_20200313.csv', sep=' ')
Test_data = pd.read_csv(path + 'used_car_testB_20200421.csv', sep=' ')

print('Train data shape:', Train_data.shape)
print('TestA data shape:', Test_data.shape)

print(Train_data.head())

# 选择所需列
selected_columns = ['SaleID', 'regDate', 'creatDate', 'brand', 'notRepairedDamage','kilometer']
new_Train_data = Train_data[selected_columns]

# 计算使用时间
new_Train_data.loc[:, 'useDate'] = pd.to_datetime(new_Train_data['creatDate'], format='%Y%m%d', errors='coerce') - pd.to_datetime(new_Train_data['regDate'], format='%Y%m%d', errors='coerce')
#new_Train_data['distance']= new_Train_data['creatDate']- new_Train_data['regDate']
new_Train_data['price'] = Train_data['price']

#new_Train_data['D_score'] = pd.qcut(new_Train_data['useDate'],4,labels=[4,3,2,1])
#new_Train_data['K_score'] = pd.qcut(new_Train_data['kilometer'],4,labels=[1,2,3,4])

# 筛选品牌为1的数据
new_Train_data = new_Train_data[new_Train_data['brand'] == 1]

# 打印新数据集的形状和前几行数据
print('New Train data shape:', new_Train_data.shape)
print(new_Train_data.head())

# 绘制散点图
plt.figure(figsize=(10, 6))

# 根据notRepairedDamage的值分别绘制不同颜色的点


plt.scatter(new_Train_data.loc[new_Train_data['notRepairedDamage'] == '0.0', 'useDate'].dt.days,
            new_Train_data.loc[new_Train_data['notRepairedDamage'] == '0.0', 'price'],
            color='green', alpha=0.5, label='notRepairedDamage=1.0')
plt.scatter(new_Train_data.loc[new_Train_data['notRepairedDamage'] == '1.0', 'useDate'].dt.days,
            new_Train_data.loc[new_Train_data['notRepairedDamage'] == '1.0', 'price'],
            color='red', alpha=0.5, label='notRepairedDamage=0.0')


plt.title('Scatter Plot of price vs. useDate')
plt.xlabel('Days between regDate and creatDate')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()