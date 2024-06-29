
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

plt.rcParams['font.family'] = 'SimHei'

# Load datasets
path = 'C:/Users/王斯哲/PycharmProjects/pythonProject/'
Train_data = pd.read_csv(path + 'data_1.csv')
Test_data = pd.read_csv(path + 'used_car_testB_20200421.csv', sep=' ')

# Create directory for saving plots
output_dir = os.path.join(path, 'plots')
os.makedirs(output_dir, exist_ok=True)

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

# Function to fit model and plot results
def fit_and_plot(brand, bodyType, fuelType, gearbox):
    subset = new_Train_data[(new_Train_data['brand'] == brand) &
                            (new_Train_data['bodyType'] == bodyType) &
                            (new_Train_data['fuelType'] == fuelType) &
                            (new_Train_data['gearbox'] == gearbox)]
    if len(subset) < 10:  # Skip if there are not enough data points
        return

    X = subset['sum'].values.reshape(-1, 1)
    y = subset['price'].values
    model = LinearRegression()
    model.fit(X, y)

    k = model.coef_[0]
    b = model.intercept_

    plt.figure(figsize=(10, 6))
    plt.scatter(subset['sum'], subset['price'], alpha=0.5, label='Data points')
    plt.plot(subset['sum'], model.predict(X), color='red', linewidth=2, label=f'Fitted line: y = {k:.2f}x + {b:.2f}')
    plt.title(f'性能评分 vs. 价格 (brand={brand}, bodyType={bodyType}, fuelType={fuelType}, gearbox={gearbox})')
    plt.xlabel('性能评分')
    plt.ylabel('价格')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, f'plot_brand_{brand}_bodyType_{bodyType}_fuelType_{fuelType}_gearbox_{gearbox}.png'))
    plt.close()

# Iterate through all combinations and generate plots
for brand in range(40):
    for bodyType in range(8):
        for fuelType in range(7):
            for gearbox in range(2):
                fit_and_plot(brand, bodyType, fuelType, gearbox)

print("All plots have been generated and saved.")