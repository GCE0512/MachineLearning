#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import numpy as np
# np是numpy的别名

print(np.arange(15))
a = np.arange(15).reshape(3, 5)
print(a)
# 打印矩阵的行列情况
print(a.shape)
# 维度
print(a.ndim)
# 值得类型
print(a.dtype.name)
# 元素的个数
print(a.size)
# 初始化矩阵
print(np.zeros((3, 4)))
# 初始化矩阵，并且指定dtype
print(np.ones((2, 3, 4), dtype=np.int32))
# 指定输出一串序列，步长
print(np.arange(10, 30, 5))#起点10，终点30，步长5
print(np.arange(0, 2, 0.3))
# 随机模块
print(np.random.rand(2, 3))
# 输出在区间[0,2pi]的100个数字，数字之间间隔相等
from numpy import pi
print(np.linspace(0, 2*pi, 100))
print(np.sin(np.linspace(0, 2*pi, 100)))

a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(a)
print(b)
# 矩阵之间的相减
c = a-b
print(c)
# 矩阵的每个元素减1
c = c-1
print(c)
# 矩阵的每个元素平方
print(b**2)
# 判断矩阵的元素小于25 真True 假False
print(a<25)

A = np.array([
    [1, 1],
    [0, 1]
])
B = np.array([
    [2, 0],
    [3, 4]
])
print(A)# print1
print("==========")
print(B)# print2
print("==========")
print(A*B)# print3
print("==========")
print(A.dot(B))# print4 与print5意义一样
print("==========")
print(np.dot(A, B))# print5