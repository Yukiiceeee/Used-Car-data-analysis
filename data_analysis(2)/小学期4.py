import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

plt.rcParams['font.family'] = 'SimHei'

# Load datasets
path = 'C:/Users/王斯哲/PycharmProjects/pythonProject/'
Train_data = pd.read_csv(path + 'data.csv')

# Select relevant columns
selected_columns = ['SaleID', 'regDate', 'creatDate', 'brand', 'notRepairedDamage', 'kilometer', 'bodyType', 'fuelType',
                    'gearbox']
new_Train_data = Train_data[selected_columns].copy()

# Calculate useDate and price
new_Train_data.loc[:, 'useDate'] = pd.to_datetime(new_Train_data['creatDate'], format='%Y%m%d',
                                                  errors='coerce') - pd.to_datetime(new_Train_data['regDate'],
                                                                                    format='%Y%m%d', errors='coerce')
new_Train_data.loc[:, 'price'] = Train_data['price']

# Handle missing values in useDate and price
new_Train_data.dropna(subset=['useDate', 'price'], inplace=True)

# Set polynomial degree
degree = 2

brands = set(new_Train_data['brand'].unique())


# Function to create and save polynomial regression plot
def create_and_save_plot(brand, bodyType, fuelType, gearbox):
    filtered_data = new_Train_data[(new_Train_data['brand'] == brand)
                                   & (new_Train_data['bodyType'] == bodyType)
                                   & (new_Train_data['fuelType'] == fuelType)
                                   & (new_Train_data['gearbox'] == gearbox)]

    if filtered_data.empty:
        print(f'No data for brand: {brand}, bodyType: {bodyType}, fuelType: {fuelType}, gearbox: {gearbox}')
        return  # Skip if no data available

    # Split data based on notRepairedDamage
    data_damage_0 = filtered_data[filtered_data['notRepairedDamage'] == 0]
    data_damage_1 = filtered_data[filtered_data['notRepairedDamage'] == 1]

    if data_damage_0.empty or data_damage_1.empty:
        print(f'Insufficient data for brand: {brand}, bodyType: {bodyType}, fuelType: {fuelType}, gearbox: {gearbox}')
        return  # Skip if no data available

    # Extract X and y for regression for both categories
    X_damage_0 = data_damage_0['useDate'].dt.days.values.reshape(-1, 1)
    y_damage_0 = data_damage_0['price'].values

    X_damage_1 = data_damage_1['useDate'].dt.days.values.reshape(-1, 1)
    y_damage_1 = data_damage_1['price'].values

    # Polynomial regression
    model_damage_0 = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model_damage_1 = make_pipeline(PolynomialFeatures(degree), LinearRegression())

    # Fit the models
    model_damage_0.fit(X_damage_0, y_damage_0)
    model_damage_1.fit(X_damage_1, y_damage_1)

    # Predict based on the models
    X_range_damage_0 = np.linspace(X_damage_0.min(), X_damage_0.max(), 100).reshape(-1, 1)
    y_pred_damage_0 = model_damage_0.predict(X_range_damage_0)

    X_range_damage_1 = np.linspace(X_damage_1.min(), X_damage_1.max(), 100).reshape(-1, 1)
    y_pred_damage_1 = model_damage_1.predict(X_range_damage_1)

    # Plotting the data and the fitted curves
    plt.figure(figsize=(10, 6))

    # Scatter plot of actual data points for notRepairedDamage=0
    plt.scatter(X_damage_0, y_damage_0, color='blue', alpha=0.5, label='汽车没有尚未修复的损坏')

    # Scatter plot of actual data points for notRepairedDamage=1
    plt.scatter(X_damage_1, y_damage_1, color='green', alpha=0.5, label='汽车有尚未修复的损坏')

    # Plot the fitted curves
    plt.plot(X_range_damage_0, y_pred_damage_0, color='red', linewidth=2,
             label=f'汽车没有尚未修复的损坏(拟合曲线) (degree={degree})')
    plt.plot(X_range_damage_1, y_pred_damage_1, color='orange', linewidth=2,
             label=f'汽车有尚未修复的损坏(拟合曲线)(degree={degree})')

    plt.title(
        f'品牌 {brand}, 车型 {bodyType}, 燃料类型 {fuelType}, 变速箱 {gearbox} 的价格 vs. 使用时间 (Polynomial Regression)')
    plt.xlabel('使用时间（天）')
    plt.ylabel('价格（元）')
    plt.legend()
    plt.grid(True)

    # Save the plot to a file
    filename = f'price_vs_use_date_brand_{brand}_bodyType_{bodyType}_fuelType_{fuelType}_gearbox_{gearbox}.png'
    plt.savefig(filename)
    plt.close()


# Iterate over all combinations
for brand in brands:
    for bodyType in range(8):
        for fuelType in range(7):
            for gearbox in range(2):
                create_and_save_plot(brand, bodyType, fuelType, gearbox)