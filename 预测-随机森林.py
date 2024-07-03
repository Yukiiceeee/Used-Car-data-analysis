
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from sklearn.model_selection import GridSearchCV,cross_val_score,StratifiedKFold,train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from math import sqrt
from sklearn.metrics import mean_squared_error, mean_absolute_error
from matplotlib import pyplot as plt
from sklearn.model_selection import GridSearchCV
plt.rcParams['font.family'] = 'SimHei'

# 载入训练集和测试集；
path = './data/'
Train_data = pd.read_csv(path+'模型构建所用数据-train.csv')
Test_data = pd.read_csv(path+'模型构建所用数据-test.csv', )

# Train_data = Train_data.fillna(-1)

# 使用时间空缺填充成平均值
Train_data['used_time']=Train_data['used_time'].fillna(Train_data['used_time'].mean())

# X_data=Train_data.drop(['SaleID','regDate','creatDate','regionCode'],axis=1)
# X_data=Train_data[['kilometer','v_0','v_1','v_2','v_3','v_4','v_5','v_6','v_7','used_time']]

X_data=Train_data.drop(['price','v_0','v_1','v_2','v_3','v_4','v_5','v_6','v_7','v_8','v_9','v_10','v_11','v_12','v_13','v_14'],axis=1)

Y_data=Train_data['price']

x_train,x_val,y_train,y_val = train_test_split(X_data,Y_data,test_size=0.3,random_state=33)

print(len(x_train),len(x_val),len(y_train))



# 随机森林分类器
model2 = RandomForestRegressor()
# n_estimators=100, random_state=0






# 设置需要调试的参数
tuned_parameters = {'n_estimators': [100,190],'max_depth': [5,10]}

# 调用网格搜索函数
rf_clf = GridSearchCV(model2, tuned_parameters, cv=5, n_jobs=-1, scoring='r2')

rf_clf.fit(x_train, y_train)
print(rf_clf.best_params_)
print(rf_clf.best_score_)

# y_predict = model2.predict(x_val)
#
# score_train = model2.score(x_train,y_train)
# score_test = model2.score(x_val,y_val)
# print(score_train,score_test)
#
# # MSE
# mse_sklearn = mean_squared_error(y_val, y_predict)
#
# # RMSE
# rmse_sklearn = np.sqrt(mse_sklearn)
#
# # MAE
# mae_sklearn = mean_absolute_error(y_val, y_predict)
#
# print("MSE (scikit-learn):", mse_sklearn)
# print("RMSE (scikit-learn):", rmse_sklearn)
# print("MAE (scikit-learn):", mae_sklearn)


# # 定义存储分数的数组
# scores_train=[]
# scores_test=[]
# # 定义存储n_estimators取值的数组
# estimators=[]
#
# # 设置n_estimators在100-210中每隔20取一个数值
# for i in range(100,210,20):
#         estimators.append(i)
#         rf = RandomForestRegressor(n_estimators=i, random_state=12)
#         rf.fit(x_train,y_train)
#         y_predict =  rf.predict(x_val)
#         scores_test.append(rf.score(x_val,y_val))
#
# # 查看我们使用的n_estimators取值
# print("estimators =", estimators)
#
# # 查看以上模型中在测试集最好的评分
# print("best_scores_test =",max(scores_test))
#
# # 画出n_estimators与scores的图形
# fig,ax = plt.subplots()
#
# # 设置x y坐标名称
# ax.set_xlabel('estimators')
# ax.set_ylabel('决定系数分数')
# plt.plot(estimators,scores_test, label='测试集')
#
# #显示汉语标注
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['font.family']=['sans-serif']
#
# # 设置图例
# plt.legend(loc="lower right")
# plt.show()






model2.fit(x_train,y_train)


y_predict2 = model2.predict(x_val)

print('预测数据长度',len(y_predict2))

# 决定系数
score_train = model2.score(x_train,y_train)
score_test = model2.score(x_val,y_val)
print("训练集score:"+str(score_train))
print("测试集score:"+str(score_test))

# MSE
mse_sklearn = mean_squared_error(y_val, y_predict2)

# RMSE
rmse_sklearn = np.sqrt(mse_sklearn)

# MAE
mae_sklearn = mean_absolute_error(y_val, y_predict2)

print("MSE (scikit-learn):", mse_sklearn)
print("RMSE (scikit-learn):", rmse_sklearn)
print("MAE (scikit-learn):", mae_sklearn)



# # 查看随机森林各项指标系数
# importance =model2.feature_importances_
#
#
# # 将特征重要性转换为DataFrame
# feature_importance = pd.DataFrame(importance, index=X_data.columns, columns=['Importance'])
# feature_importance = feature_importance.sort_values(by='Importance', ascending=False)
#
# # 打印特征重要性
# print("Feature Importances:")
# print(feature_importance)
#
#
# merged_importance = {}
# prefixes = ['brand_', 'bodyType_', 'gearbox_', 'power_bin_','fuelType','notRepairedDamage','Unnamed:0']
#
# for col in X_data.columns:
#     added_to_merged = False
#     for prefix in prefixes:
#         if col.startswith(prefix):
#             category_name = col.split('_')[0]  # 获取分类变量名称
#             merged_importance[category_name] = merged_importance.get(category_name, 0) + feature_importance.loc[col]
#             added_to_merged = True
#             break
#     if not added_to_merged:
#         merged_importance[col] = feature_importance.loc[col]
#
# # 将合并后的重要性转换为DataFrame并排序
# merged_importance_df = pd.DataFrame.from_dict(merged_importance, orient='index', columns=['Importance'])
# merged_importance_df = merged_importance_df.sort_values(by='Importance',ascending=True)
#
# # 使用条形图展示合并后的特征重要性
# plt.figure(figsize=(12, 6))
# # plt.barh(merged_importance_df.index, merged_importance_df['Importance'])
# merged_importance_df.plot(kind='barh', title='Feature Importances', figsize=(10, 6), legend=False)
# plt.title('随机森林模型指标重要性')
# plt.xlabel('Importance')
# plt.show()

