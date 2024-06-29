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
new_Train_data.loc[:, 'useDate'] = pd.to_datetime(new_Train_data['creatDate'], format='%Y%m%d',
                                                  errors='coerce') - pd.to_datetime(new_Train_data['regDate'],
                                                                                    format='%Y%m%d', errors='coerce')
new_Train_data['distance'] = new_Train_data['creatDate'] - new_Train_data['regDate']
new_Train_data['price'] = Train_data['price']
new_Train_data['kilometer'] = 50 - Train_data['kilometer'] / 15 * 50
new_Train_data['D_score'] = pd.qcut(new_Train_data['distance'], 50, labels=[i for i in range(50, 0, -1)])
new_Train_data[['D_score']] = new_Train_data[['D_score']].fillna(1)
new_Train_data['notRepairedDamage'] = Train_data['notRepairedDamage']
new_Train_data['notRepairedDamage'] = np.where(new_Train_data['notRepairedDamage'] == 0, 1.2,
                                               np.where(new_Train_data['notRepairedDamage'] == 1, 0.8, 1.0))
new_Train_data['sum'] = new_Train_data['kilometer'] * new_Train_data[
    'notRepairedDamage'] + new_Train_data.D_score.astype('int') * new_Train_data['notRepairedDamage']


# Function to fit linear model and calculate k
def calculate_k(brand, bodyType, fuelType, gearbox):
    filtered_data = new_Train_data[(new_Train_data['brand'] == brand) &
                                   (new_Train_data['bodyType'] == bodyType) &
                                   (new_Train_data['fuelType'] == fuelType) &
                                   (new_Train_data['gearbox'] == gearbox)]
    if len(filtered_data) < 2:
        return None  # Not enough data to fit a model

    X = filtered_data['sum'].values.reshape(-1, 1)
    y = filtered_data['price'].values
    model = LinearRegression()
    model.fit(X, y)

    k = model.coef_[0]
    return k


# Iterate through all combinations
results = []
for brand in range(40):
    for bodyType in range(8):
        for fuelType in range(7):
            for gearbox in range(2):
                k = calculate_k(brand, bodyType, fuelType, gearbox)
                if k is not None:
                    results.append([brand, bodyType, fuelType, gearbox, k])

# Convert results to DataFrame and save
results_df = pd.DataFrame(results, columns=['brand', 'bodyType', 'fuelType', 'gearbox', 'k'])
results_df.to_csv(path + 'k_values.csv', index=False)

print("The k values have been saved to 'k_values.csv'.")