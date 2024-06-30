from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from sklearn.model_selection import GridSearchCV,cross_val_score,StratifiedKFold,train_test_split
from sklearn.ensemble import RandomForestRegressor





# 载入训练集和测试集；
path = './data/'
Train_data = pd.read_csv(path+'模型构建所用数据-train.csv')
# Train_data = pd.read_csv(path+'data_数据清洗.csv')
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


model1=LinearRegression()
# 随机森林分类器
model2 = RandomForestRegressor()
# n_estimators=100, random_state=0



# scores_train = []
# scores = []

# 5折交叉验证方式
# sk = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
# for train_ind, val_ind in sk.split(X_data, Y_data):
#     train_x = X_data.iloc[train_ind].values
#     train_y = Y_data.iloc[train_ind]
#     val_x = X_data.iloc[val_ind].values
#     val_y = Y_data.iloc[val_ind]
#
#     model1.fit(train_x, train_y)
#     pred_train_xgb = model1.predict(train_x)
#     pred_xgb = model1.predict(val_x)
#
#     score_train = mean_absolute_error(train_y, pred_train_xgb)
#     scores_train.append(score_train)
#     score = mean_absolute_error(val_y, pred_xgb)
#     scores.append(score)

model1.fit(x_train,y_train)

model2.fit(x_train,y_train)


print('各系数'+str(model1.coef_))
print('常数项系数'+str(model1.intercept_))

y_predict = model1.predict(x_val)

print('预测数据长度',len(y_predict))

score_train = model1.score(x_train,y_train)
score_test = model1.score(x_val,y_val)
print(score_train,score_test)
print(model2.score(x_train,y_train),model2.score(x_val,y_val))