import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Ensure the font is set correctly
plt.rcParams['font.family'] = 'SimHei'

# Load datasets
path = 'C:/Users/王斯哲/PycharmProjects/pythonProject/'
Train_data = pd.read_csv(path + 'data_1.csv')
Test_data = pd.read_csv(path + 'used_car_testB_20200421.csv', sep=' ')

# Select relevant columns
selected_columns = ['SaleID', 'regDate', 'creatDate', 'brand', 'bodyType', 'fuelType', 'gearbox']
new_Train_data = Train_data[selected_columns].copy()

# Calculate useDate, distance, and other derived columns
new_Train_data.loc[:, 'useDate'] = pd.to_datetime(new_Train_data['creatDate'], format='%Y%m%d', errors='coerce') - pd.to_datetime(new_Train_data['regDate'], format='%Y%m%d', errors='coerce')
new_Train_data['distance'] = new_Train_data['creatDate'] - new_Train_data['regDate']
new_Train_data['price'] = Train_data['price']
new_Train_data['kilometer'] = 50 - Train_data['kilometer'] / 15 * 50
new_Train_data['D_score'] = pd.qcut(new_Train_data['distance'], 50, labels=[i for i in range(50, 0, -1)])
new_Train_data[['D_score']] = new_Train_data[['D_score']].fillna(1)
new_Train_data['notRepairedDamage'] = Train_data['notRepairedDamage']
new_Train_data['notRepairedDamage'] = np.where(new_Train_data['notRepairedDamage'] == 0, 1.2, np.where(new_Train_data['notRepairedDamage'] == 1, 0.8, 1.0))
new_Train_data['sum'] = new_Train_data['kilometer'] * new_Train_data['notRepairedDamage'] + new_Train_data.D_score.astype('int') * new_Train_data['notRepairedDamage']

# Filter specific conditions
new_Train_data = new_Train_data[(new_Train_data['brand'] == 1) & (new_Train_data['bodyType'] == 0) & (new_Train_data['fuelType'] == 0) & (new_Train_data['gearbox'] == 0)]

# Plotting the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(new_Train_data['sum'], new_Train_data['price'], alpha=0.5)
plt.title('Scatter Plot of sum vs. price')
plt.xlabel('sum')
plt.ylabel('Price')
plt.grid(True)
plt.show()

# Fit a linear regression model
X = new_Train_data['sum'].values.reshape(-1, 1)
y = new_Train_data['price'].values
model = LinearRegression()
model.fit(X, y)

# Calculate the slope (k) and intercept (b)
k = model.coef_[0]
b = model.intercept_

# Plot the fitted line
plt.figure(figsize=(10, 6))
plt.scatter(new_Train_data['sum'], new_Train_data['price'], alpha=0.5, label='Data points')
plt.plot(new_Train_data['sum'], model.predict(X), color='red', linewidth=2, label=f'Fitted line: y = {k:.2f}x + {b:.2f}')
plt.title('Scatter Plot of sum vs. price with Fitted Line')
plt.xlabel('sum')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

# Print the slope (k) value
print(f'The slope (k) of the fitted line is: {k}')
