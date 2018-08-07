#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import numpy

world_alcohol = numpy.genfromtxt("C:\\Users\\TNanko\\Desktop\\numpy\\world_alcohol.txt",delimiter=",",dtype=str)
print(type(world_alcohol))
print(world_alcohol)
#print(help(numpy.genfromtxt))
print(world_alcohol.shape)

print("==================================")

vector = numpy.array([5, 10, 15, 20])
matrix = numpy.array([[5, 10,15],[20,25,30],[35,40,45]])
print(vector)
print(matrix)

print("==================================")

vector = numpy.array([1,2,3,4])
print(vector.shape)
matrix = numpy.array([[5, 10, 15], [20, 25, 30]])
print(matrix.shape)

print("==================================")

# 当构造numpy.ndarray时，里面所有的元素必须是相同的结构，测试如下：
numbers = numpy.array([1, 2, 3, 4])
print(numbers)
print(numbers.dtype)
# 改变其中一个元素，int型全部转换为float类型
numbers = numpy.array([1, 2, 3, 4.0])
print(numbers)
print(numbers.dtype)
numbers = numpy.array([1, 2, 3, '4'])
print(numbers)
print(numbers.dtype)

print("==================================")

# numpy数据的选取
world_alcohol = numpy.genfromtxt("C:\\Users\\TNanko\\Desktop\\numpy\\world_alcohol.txt",delimiter=",",dtype=str,skip_header=1)
print(world_alcohol)
# 取第二个数据的第五个元素
uruguay_other_1986 = world_alcohol[1, 4]
third_country = world_alcohol[2, 2]
print(uruguay_other_1986)
print(third_country)

print("==================================")

# 在numpy中使用切片
vector = numpy.array([5, 10, 15, 20])
print(vector[0:3])

print("==================================")

# 取某一个样本的一列
matrix = numpy.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])
# 冒号表示现在去样本的所有行
print(matrix[:, 1], end='\n'+'\n')
# 取两列数据
print(matrix[:, 0:2], end='\n'+'\n')
# 取两行数据其中的两列数据
print(matrix[1:3, 0:2])

