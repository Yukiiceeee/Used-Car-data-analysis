import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
plt.rcParams['font.family'] = 'SimHei'

# 载入训练集和测试集
path = './data/'
Train_data = pd.read_csv(path + '模型构建所用数据-train.csv')
Test_data = pd.read_csv(path + '模型构建所用数据-test.csv')

# 使用时间空缺填充成平均值
Train_data['used_time'] = Train_data['used_time'].fillna(Train_data['used_time'].mean())

# 选择特征和目标变量
X_data = Train_data.drop(['price', 'v_0', 'v_1', 'v_2', 'v_3', 'v_4', 'v_5', 'v_6', 'v_7', 'v_8', 'v_9', 'v_10', 'v_11', 'v_12', 'v_13', 'v_14'], axis=1)
Y_data = Train_data['price']

# 划分数据集
x_train, x_val, y_train, y_val = train_test_split(X_data, Y_data, test_size=0.3, random_state=33)

# 创建XGBoost模型
model = XGBRegressor(n_estimators=190,max_depth=5)
# 设置需要调试的参数
tuned_parameters = {'n_estimators': [100,190],'max_depth': [5,10]}

# 调用网格搜索函数
rf_clf = GridSearchCV(model, tuned_parameters, cv=5, n_jobs=-1, scoring='neg_mean_squared_error')
rf_clf.fit(x_train, y_train)
print(rf_clf.best_params_)
print(rf_clf.best_score_)



# 训练模型
model.fit(x_train, y_train)

# 预测
y_predict = model.predict(x_val)

# 模型评估
mse = mean_squared_error(y_val, y_predict)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_val, y_predict)
print("MSE (XGBoost):", mse)
print("RMSE (XGBoost):", rmse)
print("MAE (XGBoost):", mae)
print("训练集score:")
print(model.score(x_train, y_train))
print("测试集score:")
print( model.score(x_val, y_val))

# 特征重要性

# 查看各项指标系数
importance =model.feature_importances_
# 将特征重要性转换为DataFrame
feature_importance = pd.DataFrame(importance, index=X_data.columns, columns=['Importance'])
feature_importance = feature_importance.sort_values(by='Importance', ascending=False)

# 打印特征重要性
print("Feature Importances:")
print(feature_importance)

# # 通过图形的方式直观展现前八名的重要指标
# index=X_data.columns
# feature_importance = pd.DataFrame(importance.T, index=index).sort_values(by=0, ascending=True)
# importance_dict = feature_importance[0].to_dict()
#
# # # 查看指标重要度
# print(feature_importance)
# print(importance_dict)
#
# # 水平条形图绘制
# feature_importance.tail(9).plot(kind='barh', title='Feature Importances', figsize=(10, 6), legend=False)
# plt.show()

# 如果有哑变量，合并分类变量的重要性

merged_importance = {}
prefixes = ['brand_', 'bodyType_', 'gearbox_', 'power_bin_','fuelType','notRepairedDamage','Unnamed:0']

for col in X_data.columns:
    added_to_merged = False
    for prefix in prefixes:
        if col.startswith(prefix):
            category_name = col.split('_')[0]  # 获取分类变量名称
            merged_importance[category_name] = merged_importance.get(category_name, 0) + feature_importance.loc[col]
            added_to_merged = True
            break
    if not added_to_merged:
        merged_importance[col] = feature_importance.loc[col]

# 将合并后的重要性转换为DataFrame并排序
merged_importance_df = pd.DataFrame.from_dict(merged_importance, orient='index', columns=['Importance'])
merged_importance_df = merged_importance_df.sort_values(by='Importance',ascending=True)

# 重新展示特征重要性
# merged_importance_df = pd.DataFrame.from_dict(merged_importance, orient='index')
# , orient='index', columns=['Importance']
# print(merged_importance_df.columns)
# print(merged_importance)

# merged_importance_df = merged_importance_df.sort_values(by='0',ascending=False)

# 使用条形图展示合并后的特征重要性
plt.figure(figsize=(12, 6))
# plt.barh(merged_importance_df.index, merged_importance_df['Importance'])
merged_importance_df.plot(kind='barh', title='Feature Importances', figsize=(10, 6), legend=False)
plt.title('xgboost 指标重要性')
plt.xlabel('Importance')
plt.savefig('./figures/xgboost_importance.png')
plt.show()