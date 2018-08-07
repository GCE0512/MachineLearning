#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import numpy

# 在numpy中的计算

# 判断
vector = numpy.array([5, 10, 15, 20])
print(vector == 10)

matrix = numpy.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45],
])
print(matrix == 25)

# 将布尔值当成索引，输出结果
vector = numpy.array([5, 10, 15, 20])
equal_to_ten = (vector == 10)
print(equal_to_ten)
print(vector[equal_to_ten])

matrix = numpy.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45],
])
second_column_25 = (matrix[:, 1] == 25)
print(second_column_25)
# 首先先定位到 25 所在的那一行
print(matrix[second_column_25, :])

# 与或判断
vector = numpy.array([5, 10, 15, 20])
# 与&
equal_to_ten_and_five = (vector == 10) & (vector == 5)
print(equal_to_ten_and_five)

# 或|
equal_to_ten_or_five = (vector == 10) | (vector == 5)
print(equal_to_ten_or_five)

print(vector[equal_to_ten_or_five])
print(vector)

vector[equal_to_ten_or_five] = 50
print(vector)

# 对 numpy array 值的类型的改变
vector = numpy.array(["1", "2", "3"])
print(vector.dtype)
print(vector)
vector = vector.astype(float)# astype,值类型的转换
print(vector.dtype)
print(vector)

# 求极值
vector = numpy.array([5, 10, 15, 20])
print("最小值：", vector.min())
print("最大值：", vector.max())
#print(help(numpy.array))# 输出帮助文档

# 求和（按行求和、按列求和）
matrix = numpy.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])
print(matrix.sum(axis=1))# axis=1，对每行求和
print(matrix.sum(axis=0))# axis=0，对每列求和


