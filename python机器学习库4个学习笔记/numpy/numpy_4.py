#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import numpy as np
B = np.arange(3)
print(B)
print(np.exp(B))# e的多少次幂
print(np.sqrt(B))# 对元素开根号

a = np.floor(10*np.random.rand(3, 4))
print(a)
print('------------')
print(a.ravel())# 矩阵转换为一维向量
print('------------')
a.shape = (6, 2)
print(a)
# a.shape = (3, -1) 矩阵的维度转换时，只要确定一个方向，另一个方向也确定，输入 -1 则让程序自动计算另一维度的大小。
print('------------')
print(a.T)# 矩阵的转置

# 矩阵拼接操作
a = np.floor(10*np.random.random((2, 2)))
b = np.floor(10*np.random.rand(2, 2))
print(a)
print('------------')
print(b)
print('------------')
print(np.hstack((a, b)))# 横向拼接
print('------------')
print(np.vstack((a, b)))# 纵向拼接

# 矩阵切割操作
a = np.floor(10*np.random.rand(2, 12))
print(a)
print('------------')
print(np.hsplit(a, 3))# 按行切分
print('------------')
print(np.hsplit(a, (3, 4)))# 指定位置切割
print('------------')
b = a.T # 转置矩阵a
#b = np.floor(10*np.random.rand(12, 2))
print(np.vsplit(b, 3))# 按列切分

# numpy python 的复制
a = np.arange(12)
b = a# 完全不拷贝
# 这一块类似于Java的引用
print(b is a)# 判断变量 a 和 b 是同一个变量
b.shape = (3, 4)
print(a.shape)
# 查看两个变量的id值（个人认为类似于c/c++中的指针）
print(id(a))
print(id(b))

c = a.view()# 浅拷贝
print(c is a)
print(c)# shape前
c.shape = (2, 6)
print(c)# shape后
c[0, 4] = 1234# 共享数据
print(a)
print(id(a))
print(id(c))

d = a.copy()# 深拷贝
print(d is a)
d[0, 0] = 999
print(id(a))
print(id(d))
print(a)
print(d)

