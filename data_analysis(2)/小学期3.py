import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 载入训练集和测试集
path = 'C:/Users/王斯哲/PycharmProjects/pythonProject/'
Train_data = pd.read_csv(path + 'data_1.csv')
Test_data = pd.read_csv(path + 'used_car_testB_20200421.csv', sep=' ')

print('Train data shape:', Train_data.shape)
print('TestA data shape:', Test_data.shape)

print(Train_data.head())

# 选择所需列
selected_columns = ['SaleID', 'regDate', 'creatDate', 'brand','bodyType','fuelType','gearbox']
new_Train_data = Train_data[selected_columns]

# 计算使用时间
new_Train_data.loc[:, 'useDate'] = pd.to_datetime(new_Train_data['creatDate'], format='%Y%m%d', errors='coerce') - pd.to_datetime(new_Train_data['regDate'], format='%Y%m%d', errors='coerce')
new_Train_data['distance']= new_Train_data['creatDate']- new_Train_data['regDate']
new_Train_data['price'] = Train_data['price']
new_Train_data['kilometer'] = 33-Train_data['kilometer']/15*33
new_Train_data['D_score'] = pd.qcut(new_Train_data['distance'],33,labels=[33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1])
new_Train_data[['D_score']] = new_Train_data[['D_score']].fillna(1)
new_Train_data['notRepairedDamage'] = Train_data['notRepairedDamage']
new_Train_data['notRepairedDamage'] = np.where(new_Train_data['notRepairedDamage'] == '0.0', 33.0,
                                               np.where(new_Train_data['notRepairedDamage'] == '1.0', 15.0, 0.0))
new_Train_data['sum']= new_Train_data['kilometer'] + new_Train_data['notRepairedDamage']+new_Train_data.D_score.astype('int')
#new_Train_data['K_score'] = pd.qcut(new_Train_data['kilometer'],4,labels=[4,3,2,1])

# 筛选品牌为1的数据
new_Train_data = new_Train_data[new_Train_data['brand'] == 1]
new_Train_data = new_Train_data[new_Train_data['bodyType'] == 0]
new_Train_data = new_Train_data[new_Train_data['fuelType'] == 0]
new_Train_data = new_Train_data[new_Train_data['gearbox'] == 0]
'''
plt.figure(figsize=(10, 6))
plt.hist(new_Train_data['sum'], bins=20, edgecolor='black')
plt.title('Histogram of sum')
plt.xlabel('sum')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

'''
plt.figure(figsize=(10, 6))
plt.scatter(new_Train_data['sum'], new_Train_data['price'], alpha=0.5)
plt.title('Scatter Plot of sum vs. price')
plt.xlabel('sum')
plt.ylabel('Price')
plt.grid(True)
plt.show()

# 打印新数据集的形状和前几行数据
print('New Train data shape:', new_Train_data.shape)
print(new_Train_data.head())
'''
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
'''