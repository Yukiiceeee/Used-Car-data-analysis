
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV,cross_val_score,StratifiedKFold,train_test_split
from sklearn.linear_model import RidgeCV


from sklearn.metrics import mean_squared_error, mean_absolute_error
from matplotlib import pyplot as plt
from sklearn.linear_model import Ridge
plt.rcParams['font.family'] = 'SimHei'
# 载入训练集和测试集；
path = './data/'
Train_data = pd.read_csv(path+'模型构建所用数据-train.csv')
Test_data = pd.read_csv(path+'模型构建所用数据-test.csv', )

# Train_data = Train_data.fillna(-1)

# 使用时间空缺填充成平均值
Train_data['used_time']=Train_data['used_time'].fillna(Train_data['used_time'].mean())

X_data=Train_data.drop(['price','v_0','v_1','v_2','v_3','v_4','v_5','v_6','v_7','v_8','v_9','v_10','v_11','v_12','v_13','v_14'],axis=1)
Y_data=Train_data['price']

# 划分数据集
x_train,x_val,y_train,y_val = train_test_split(X_data,Y_data,test_size=0.3,random_state=33)

print(len(x_train),len(x_val),len(y_train))





# #构造不同的lambda值
# Lambdas=np.logspace(-5,2,200)
# #存放偏回归系数
# ridge_cofficients=[]
# for Lambda in Lambdas:
#     ridge=Ridge(alpha=Lambda)
#     ridge.fit(x_train,y_train)
#     ridge_cofficients.append(ridge.coef_)
#
# #绘制岭迹曲线
# plt.rcParams['font.sans-serif']=['Microsoft YaHei']
# plt.rcParams['axes.unicode_minus']=False
# plt.style.use('ggplot')
# plt.plot(Lambdas,ridge_cofficients)
# #x轴做对数处理
# plt.xscale('log')
# plt.xlabel('Log(Lambda)')
# plt.ylabel('Cofficients')
# plt.show()


#构造不同的lambda值
Lambdas=np.logspace(-5,2,200)
#设置交叉验证的参数，使用均方误差评估
ridge_cv=RidgeCV(alphas=Lambdas,scoring='neg_mean_squared_error',cv=5)
ridge_cv.fit(x_train,y_train)
print(ridge_cv.alpha_)

model1=Ridge(alpha=ridge_cv.alpha_,fit_intercept=True,max_iter=5)

model1.fit(x_train,y_train)


print('各系数'+str(model1.coef_))
print(X_data.columns)
print('常数项系数'+str(model1.intercept_))

y_predict1 = model1.predict(x_val)

print('预测数据长度',len(y_predict1))


# 查看各项指标系数
coefficient = model1.coef_

# 取出指标系数，并对其求绝对值
importance =abs(coefficient)

# 通过图形的方式直观展现前9名的重要指标
index=X_data.columns
feature_importance = pd.DataFrame(importance.T, index=index).sort_values(by=0, ascending=True)

# # 查看指标重要度
print(feature_importance)

# 水平条形图绘制
feature_importance.tail(9).plot(kind='barh', title='Feature Importances', figsize=(10, 6), legend=False)
plt.savefig('岭回归')
plt.show()
print(feature_importance.tail(9))
#决定系数
score_train = model1.score(x_train,y_train)
score_test = model1.score(x_val,y_val)
print(score_train,score_test)


# MSE
mse_sklearn = mean_squared_error(y_val, y_predict1)

# RMSE
rmse_sklearn = np.sqrt(mse_sklearn)

# MAE
mae_sklearn = mean_absolute_error(y_val, y_predict1)

print("MSE (scikit-learn):", mse_sklearn)
print("RMSE (scikit-learn):", rmse_sklearn)
print("MAE (scikit-learn):", mae_sklearn)

# 将特征重要性转换为DataFrame
feature_importance = pd.DataFrame(importance, index=X_data.columns, columns=['Importance'])
feature_importance = feature_importance.sort_values(by='Importance', ascending=False)

# 打印特征重要性
print("Feature Importances:")
print(feature_importance)


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

# 使用条形图展示合并后的特征重要性
plt.figure(figsize=(12, 6))
# plt.barh(merged_importance_df.index, merged_importance_df['Importance'])
merged_importance_df.plot(kind='barh', title='Feature Importances', figsize=(10, 6), legend=False)
plt.title('岭回归指标重要性')
plt.xlabel('Importance')
plt.savefig('./figures/岭回归_importance.png')
plt.show()

