
# coding: utf-8

'''
注意：
.py版本是由 .ipynb转化而来
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
get_ipython().run_line_magic('matplotlib', 'inline')

def get_X(df):
    # ones是m行一列的dataframe
    ones = pd.DataFrame({'ones': np.ones(len(df))})
    # 合并数据，根据列合并
    data = pd.concat([ones, df], axis=1)
    # 上面两行完成的操作，就是在原有的数据上添加一列全为0的数据
    
    # 返回ndarray,不是矩阵
    return data.iloc[:, :-1].values 

def get_y(df):
    # df.iloc[:, -1]是指df的最后一列
    return np.array(df.iloc[:, -1])

def normalize_feature(df):
    # 特征缩放
    return df.apply(lambda column: (column - column.mean()) / column.std())

def Hypothesis(X, theta):
    return X.dot(theta)

'''
X: R(m*n), m样本数, n特征数
y: R(m)
theta: R(n), 线性回归的参数,(假设函数的theta0,theta1)
'''
def lr_cost(theta, X, y):
    # m样本数
    m = X.shape[0]
    # 假设函数
    hypothesis = Hypothesis(X, theta)
    # 硬上公式
    cost = np.square(hypothesis - y).sum() / (2 * m)
    return cost

'''
批量梯度下降
'''

# 单次下降
def gradient(theta, X, y):
    m = X.shape[0]
    J = X.T.dot((Hypothesis(X, theta) - y)) / m
    #inner = X.T @ (X @ theta - y) / m
    return J

'''
批量梯度下降函数
拟合线性回归
iteration 迭代次数
'''
def batch_gradient_decent(theta, X, y, iteration, alpha = 0.01):
    cost_data = lr_cost(theta, X, y)
    # 拷贝一份theta数据，不与原来的混淆
    theta_copy = theta.copy()
    for _ in range(iteration):
        theta_copy = theta_copy - alpha * gradient(theta_copy, X, y)
        cost_data = np.append(cost_data, lr_cost(theta_copy, X, y))
    
    return theta_copy, cost_data

raw_data = pd.read_csv("ex1data2.txt", names=['Square', 'Bedrooms', 'Price'])
print(raw_data.head())


# 标准化数据(特征缩放)

def normalize_feature(df):
    # 特征缩放
    return df.apply(lambda column: (column - column.mean()) / column.std())

data = normalize_feature(raw_data)
print(data.head())


# multi-var batch gradient decent(多变量批量梯度下降)

X = get_X(data)
print(X.shape, type(X))

y = get_y(data)
print(y.shape, type(y))

# 学习率
alpha = 0.01
# theta变量 X.shape[1]: 特征数n
theta = np.zeros(X.shape[1])
# 迭代次数
iteration = 1000

final_theta, cost_data = batch_gradient_decent(theta, X, y, iteration, alpha)

sns.tsplot(cost_data, np.arange(len(cost_data)))
plt.xlabel('Iteration', fontsize=18)
plt.ylabel('Cost', fontsize=18)
plt.show()

print(final_theta)


# learning rate(学习率)

base = np.logspace(-1, -5, num=4)
new_alpha = np.sort(np.concatenate((base, base*3)))
print(new_alpha)

fig, ax = plt.subplots(figsize=(16, 9))

for alpha in new_alpha:
    lr_theta, cost_data = batch_gradient_decent(theta, X, y, iteration, alpha)
    ax.plot(np.arange(iteration+1), cost_data, label=alpha)
    
ax.set_xlabel('Iteration', fontsize=18)
ax.set_ylabel('Cost', fontsize=18)
ax.set_title('Learning rate', fontsize=20)
ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

# normal equation(正规方程)

def normalEqn(X, y):
    theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    return theta

# 和批量梯度下降的theta有点差距的
final_theta2 = normalEqn(X, y)
print(final_theta2)


