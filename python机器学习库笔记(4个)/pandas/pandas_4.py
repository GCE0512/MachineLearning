#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# Series结构
# 前面记录的都是DataFrama结构
# DataFrama相当于读入的矩阵，Series相当于其中的一行或一列

# A Series object can hold many data types, including
# float - for representing float values
# int - for representing integer values
# bool - for representing Boolean values
# datetime64[ns] - for representing date & time, without time-zone
# datetime64[ns, tz] - for representing date & time, with time-zone
# timedelta[ns] - for representing differences in dates & times (seconds. minutes, etc.)
# category - for representing categorical values
# object - for representing String values

import pandas as pd
fandango = pd.read_csv("C:\\Users\\TNanko\\PycharmProjects\\MachineLearning\\venv\\Data\\pandas\\fandango_score_comparison.csv")
# print(fandango)
series_film = fandango["FILM"]
print(type(series_film)) # Series 结构
print(series_film[0:5])
series_rt = fandango["RottenTomatoes"]
print(series_rt[0:5])

# 新建一个Series结构
from pandas import Series

film_names = series_film.values
print(type(film_names)) # Series 里面的结构是一个 ndarray, pandas其实是封装在numpy基础之上的。
# print(film_names)
rt_scores = series_rt.values
print(rt_scores)
series_custom = Series(rt_scores, index=film_names)
print(series_custom[["Minions (2015)", "Leviathan (2014)"]])
five_ten = series_custom[5:10]
print(five_ten)

# 排序
original_index = series_custom.index.tolist()
print(original_index)
sorted_index = sorted(original_index)
sorted_by_index = series_custom.reindex(sorted_index)
print(sorted_by_index)

sc2 = series_custom.sort_index()
sc3 = series_custom.sort_values()
print(sc2[0:10])
print(sc3[0:10])

# 对两个series相加
import numpy as np
print(np.add(series_custom, series_custom))
np.sin(series_custom)
np.max(series_custom)

a = series_custom > 50 # 返回的是一个布尔值
print(a)
series_greater_than_50 = series_custom[series_custom > 50] # 输出大于50的值
print(series_greater_than_50)

criteria_one = series_custom > 50
criteria_two = series_custom < 75
both_criteria = series_custom[criteria_one & criteria_two]
print(both_criteria)

# data alignment same index
rt_critics = Series(fandango["RottenTomatoes"].values, index=fandango["FILM"])
rt_users = Series(fandango["RottenTomatoes_User"].values, index=fandango["FILM"])
rt_mean = (rt_critics + rt_users) / 2 # 算一下这两家媒体的平均值是多少
print(rt_mean)

