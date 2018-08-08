#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 排序索引问题
import numpy as np

data = np.sin(np.arange(20)).reshape(5, 4)
print(data)
ind = data.argmax(axis=0)# 每列最大值所在的索引（axis=0 即 按列进行计算）
print(ind)
data_max = data[ind, range(data.shape[1])]# 将每列最大值输出
print(data_max)

a = np.arange(0, 40, 10)
print(a)
b = np.tile(a, (3, 2))# 扩展（行变成原来的3倍，列变成原来的2倍）
print(b)

# 排序
a = np.array([[4, 3, 5], [7, 9, 3]])
print(a)
b = np.sort(a, axis=1)# 默认从小到大排序（axis=1 即 按行排序）
print(b)
a.sort(axis=1)
print(a)
print('------------')
# argsort()在 1*4 的矩阵中的使用
a = np.array([98, 97, 96, 95])
j = np.argsort(a)
print('在 1*4 的矩阵从小到大排序后的索引值：', j)
print('在 1*4 的矩阵从小到大排序后的结果：', a[j])
print('------------')
# argsort()在 2*4 的矩阵中的使用
a = np.array([[4, 3, 1, 2], [9, 5,87,56]])
j = np.argsort(a, axis=1)# 将矩阵从小到大排序 取出相应的索引
print(j)
print('------------')
print(a[1, j[1, :]])# 输出 2*4 矩阵的第二行排序后的值
