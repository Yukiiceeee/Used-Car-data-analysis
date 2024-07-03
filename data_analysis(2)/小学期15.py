import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

plt.rcParams['font.family'] = 'SimHei'
# Load datasets
path = 'C:/Users/王斯哲/PycharmProjects/pythonProject/'
Train_data = pd.read_csv(path + 'used_car_train_20200313.csv', sep=' ')
Test_data = pd.read_csv(path + 'used_car_testB_20200421.csv', sep=' ')

# Select relevant columns and handle missing values for training data
selected_columns = ['regDate', 'creatDate', 'brand', 'kilometer', 'bodyType', 'fuelType', 'gearbox', 'price']
Train_data = Train_data[selected_columns + ['notRepairedDamage']].copy()
Train_data['useDate'] = pd.to_datetime(Train_data['creatDate'], format='%Y%m%d', errors='coerce') - pd.to_datetime(Train_data['regDate'], format='%Y%m%d', errors='coerce')
Train_data['useDate'] = Train_data['useDate'].dt.days
Train_data.dropna(inplace=True)

# Select relevant columns and handle missing values for test data
test_columns = ['regDate', 'creatDate', 'brand', 'kilometer', 'bodyType', 'fuelType', 'gearbox']
if 'price' in Test_data.columns:
    test_columns.append('price')
Test_data = Test_data[test_columns].copy()
Test_data['useDate'] = pd.to_datetime(Test_data['creatDate'], format='%Y%m%d', errors='coerce') - pd.to_datetime(Test_data['regDate'], format='%Y%m%d', errors='coerce')
Test_data['useDate'] = Test_data['useDate'].dt.days
Test_data.dropna(inplace=True)

# Replace categorical data with numerical data (if necessary)
brand_mapping = {'揽胜极光': 0, 'Panamera': 1, '奔驰B级': 2, '宝马3系': 3, '奥迪A6L': 4, '凯迪拉克XTS': 5, '别克GL8': 6, '探界者': 7, '蒙迪欧': 8, '奔驰GLC': 9,
                 '凯迪拉克XT5': 10, '奔驰M级': 11, '宝马M4': 12, '雷克萨斯IS': 13, '捷豹XEL': 14, '奥迪A4L': 15, 'MINI': 16, '本田CR-V': 17, '奔驰R级': 18,
                 'Cayman': 19, '奔驰C级(进口)': 20, '奔驰GL级': 21, '宝马5系': 22, '朗逸': 23, '捷达': 24, '奔驰V级': 25, '天籁': 26, '奔驰GLB': 27, '揽胜': 28,
                 '揽胜运动版': 29, '沃尔沃XC90': 30}
bodyType_mapping = {'豪华轿车': 0, '微型车': 1, '厢型车': 2, '大巴车': 3, '敞篷车': 4, '双门汽车': 5, '商务车': 6, '搅拌车': 7}
fuelType_mapping = {'汽油': 0, '柴油': 1, '液化石油气': 2, '天然气': 3, '混合动力': 4, '其他': 5, '电动': 6}
gearbox_mapping = {'手动': 0, '自动': 1}

Train_data.replace({'brand': brand_mapping, 'bodyType': bodyType_mapping, 'fuelType': fuelType_mapping, 'gearbox': gearbox_mapping}, inplace=True)
Test_data.replace({'brand': brand_mapping, 'bodyType': bodyType_mapping, 'fuelType': fuelType_mapping, 'gearbox': gearbox_mapping}, inplace=True)

# Ensure 'notRepairedDamage' is numeric and handle non-integer values
Train_data['notRepairedDamage'] = pd.to_numeric(Train_data['notRepairedDamage'], errors='coerce').fillna(0).astype(int)

# Split the training data
X = Train_data[['useDate', 'brand', 'kilometer', 'bodyType', 'fuelType', 'gearbox', 'price']]
y = Train_data['notRepairedDamage']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)

# Ensure 'price' column is in test data if it was in training data
if 'price' in Train_data.columns:
    if 'price' not in Test_data.columns:
        Test_data['price'] = 0  # Default value or imputation
X_test = scaler.transform(Test_data[['useDate', 'brand', 'kilometer', 'bodyType', 'fuelType', 'gearbox', 'price']])

# Train the model using XGBoost
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# Validate the model
y_val_pred = model.predict(X_val)
print("Validation Accuracy: ", accuracy_score(y_val, y_val_pred))
print(classification_report(y_val, y_val_pred))

# Predict on test data
Test_data['notRepairedDamage'] = model.predict(X_test)

# Save the results
Test_data['SaleID'] = Test_data.index  # Assuming SaleID should be the index or some unique identifier
Test_data[['SaleID', 'notRepairedDamage']].to_csv('used_car_testB_20200421_predictions.csv', index=False)

conf_matrix = confusion_matrix(y_val, y_val_pred)

# Plot confusion matrix
plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=np.unique(y), yticklabels=np.unique(y))
plt.xlabel('预测值')
plt.ylabel('真实值')
plt.title('混淆矩阵')
plt.show()