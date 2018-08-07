
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("ex1data1.txt", names=['Population', 'Profit'])
print(data.head())

# 打印数据信息
print(data.info())

# 使用matplotlib绘图
fig = plt.figure()
plt.xlabel('Population')
plt.ylabel('Profit')
plt.scatter(data.Population, data.Profit)
plt.show()

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


# 计算代价函数

X = get_X(data)
y = get_y(data)

# 看一下数据的维度
print(X.shape, type(X))
print(y.shape, type(y))

# 输出数据看一下
print(X)
print("------------------------")
print(y)

# X.shape[1] = 2, 代表特征数
theta = np.zeros(X.shape[1])
print(theta.shape)

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

lr_cost(theta, X, y)


# # 批量梯度下降

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

# 迭代次数为1000
iteration = 500
final_theta, final_cost_data = batch_gradient_decent(theta, X, y, iteration)

print(final_theta)

print(final_cost_data)

# 计算最终的代价函数
lr_cost(final_theta, X, y)


# 代价函数可视化

'''
此方法官方已弃用
ax = sns.tsplot(final_cost_data, np.arange(iteration+1))
ax.set_xlabel('iteration')
ax.set_ylabel('cost')
plt.show()
'''
fig = plt.figure()
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.plot(final_cost_data, np.arange(iteration+1))
plt.show()

# 截距
b = final_theta[0]
# 斜率
k = final_theta[1]

plt.scatter(data['Population'], data['Profit'], label='Training data')
plt.plot(data.Population, k * data.Population + b, label='Prediction')
plt.legend(loc=2)
plt.show()

