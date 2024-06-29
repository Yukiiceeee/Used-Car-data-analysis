import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load datasets
path = 'C:/Users/王斯哲/PycharmProjects/pythonProject/'
Train_data = pd.read_csv(path + 'data_1.csv')
Test_data = pd.read_csv(path + 'used_car_testB_20200421.csv', sep=' ')

# Check for missing values
print('Train data missing values:')
print(Train_data.isnull().sum())

# Handle missing values for columns 'regDate' and 'creatDate'
Train_data['regDate'] = pd.to_datetime(Train_data['regDate'], format='%Y%m%d', errors='coerce')
Train_data['creatDate'] = pd.to_datetime(Train_data['creatDate'], format='%Y%m%d', errors='coerce')

# Drop rows with missing 'regDate' or 'creatDate'
Train_data.dropna(subset=['regDate', 'creatDate'], inplace=True)

# Continue with your original operations...

# Select required columns
selected_columns = ['SaleID', 'regDate', 'creatDate', 'brand', 'notRepairedDamage', 'kilometer', 'bodyType', 'fuelType', 'gearbox']
new_Train_data = Train_data[selected_columns]

# Calculate useDate
new_Train_data['useDate'] = new_Train_data['creatDate'] - new_Train_data['regDate']

# Filter data as per your conditions
new_Train_data = new_Train_data[(new_Train_data['brand'] == 1)
                                & (new_Train_data['bodyType'] == 0)
                                & (new_Train_data['fuelType'] == 0)
                                & (new_Train_data['gearbox'] == 0)]

# Split data based on notRepairedDamage
data_damage_0 = new_Train_data[new_Train_data['notRepairedDamage'] == 0]
data_damage_1 = new_Train_data[new_Train_data['notRepairedDamage'] == 1]

# 提取 X 和 y 数据
X_damage_0 = data_damage_0['useDate'].dt.days.values.reshape(-1, 1)
y_damage_0 = data_damage_0['price'].values.reshape(-1, 1)

X_damage_1 = data_damage_1['useDate'].dt.days.values.reshape(-1, 1)
y_damage_1 = data_damage_1['price'].values.reshape(-1, 1)

# 初始化线性回归模型
model_damage_0 = LinearRegression()
model_damage_1 = LinearRegression()

# 拟合模型
model_damage_0.fit(X_damage_0, y_damage_0)
model_damage_1.fit(X_damage_1, y_damage_1)

# 预测
X_range = np.linspace(X_damage_0.min(), X_damage_0.max(), 100).reshape(-1, 1)
y_pred_damage_0 = model_damage_0.predict(X_range)

X_range = np.linspace(X_damage_1.min(), X_damage_1.max(), 100).reshape(-1, 1)
y_pred_damage_1 = model_damage_1.predict(X_range)

# 绘图
plt.figure(figsize=(10, 6))

# 绘制散点图
plt.scatter(data_damage_0['useDate'].dt.days, data_damage_0['price'], color='green', alpha=0.5, label='notRepairedDamage=0.0')
plt.scatter(data_damage_1['useDate'].dt.days, data_damage_1['price'], color='red', alpha=0.5, label='notRepairedDamage=1.0')

# 绘制拟合曲线
plt.plot(X_range, y_pred_damage_0, color='darkgreen', linewidth=2, label='Fit notRepairedDamage=0.0')
plt.plot(X_range, y_pred_damage_1, color='darkred', linewidth=2, label='Fit notRepairedDamage=1.0')

plt.title('Scatter Plot with Fitted Curves of price vs. useDate')
plt.xlabel('Days between regDate and creatDate')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()