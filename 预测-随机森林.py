from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from sklearn.model_selection import GridSearchCV,cross_val_score,StratifiedKFold,train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from math import sqrt
from sklearn.metrics import mean_squared_error, mean_absolute_error


# 载入训练集和测试集；
path = './data/'
Train_data = pd.read_csv(path+'模型构建所用数据-train.csv')
Test_data = pd.read_csv(path+'模型构建所用数据-test.csv', )

# Train_data = Train_data.fillna(-1)

# 使用时间空缺填充成平均值
Train_data['used_time']=Train_data['used_time'].fillna(Train_data['used_time'].mean())

# X_data=Train_data.drop(['SaleID','regDate','creatDate','regionCode'],axis=1)
X_data=Train_data[['kilometer','v_0','v_1','v_2','v_3','v_4','v_5','v_6','v_7','used_time']]

# X_data=Train_data.drop(['price'],axis=1)
Y_data=Train_data['price']

x_train,x_val,y_train,y_val = train_test_split(X_data,Y_data,test_size=0.3,random_state=33)

print(len(x_train),len(x_val),len(y_train))



# 随机森林分类器
model2 = RandomForestRegressor()
# n_estimators=100, random_state=0



# 均方误差
def MSE(y_true,y_predict):
    return np.sum((y_true-y_predict)**2)/len(y_true)
# 均根方误差
def RMSE(y_true,y_predict):
    return sqrt(np.sum((y_true-y_predict)**2)/len(y_true))
# 绝对平均误差
def MAE(y_true,y_predict):
    return np.sum(np.absolute(y_true-y_predict))/len(y_true)



model2.fit(x_train,y_train)

# scores = cross_val_score(model1,x_train,y_train,cv=4)

# print('各系数'+str(model2.coef_))
# print('常数项系数'+str(model2.intercept_))

y_predict2 = model2.predict(x_val)

print('预测数据长度',len(y_predict2))
print('预测数据长度',len(y_predict2))
#决定系数
score_train = model2.score(x_train,y_train)
score_test = model2.score(x_val,y_val)
print(score_train,score_test)


# MSE
mse_sklearn = mean_squared_error(y_val, y_predict2)

# RMSE
rmse_sklearn = np.sqrt(mse_sklearn)

# MAE
mae_sklearn = mean_absolute_error(y_val, y_predict2)

print("MSE (scikit-learn):", mse_sklearn)
print("RMSE (scikit-learn):", rmse_sklearn)
print("MAE (scikit-learn):", mae_sklearn)