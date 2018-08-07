#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# Pandas计算

import pandas

food_info = pandas.read_csv("C:\\Users\\TNanko\\PycharmProjects\\MachineLearning\\venv\\Data\\pandas\\food_info.csv")
col_names = food_info.columns.tolist()
print(col_names)
print(food_info.head(3))

print(food_info["Iron_(mg)"])
div_1000 = food_info["Iron_(mg)"] / 1000
print(div_1000)

water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
print(water_energy)
iron_grams = food_info["Iron_(mg)"] * 1000
print(food_info.shape) # 查看当前维度
food_info["Iron_(g)"] = iron_grams # 首先新建一个列 Iron_(g),其次将 iron_grams的值附在新建的列上
print(food_info.shape) # 查看当前维度，发现多了一列

weighted_protein = food_info["Protein_(g)"] * 2
weighted_fat = -0.75 * food_info["Lipid_Tot_(g)"]
initial_rating = weighted_protein + weighted_fat

# 求最大值
max_calories = food_info["Energ_Kcal"].max()
# print(max_calories)
normalized_calories = food_info["Energ_Kcal"] / max_calories
normalized_protein = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
normalized_fat = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()
food_info["Normalized_Protein"] = normalized_protein
food_info["Normalized_Fat"] = normalized_fat

# 排序
food_info.sort_values("Sodium_(mg)", inplace=True) # 对Sodium_(mg)排序;inplace=True,排序后的数据直接替换原来的数据
print(food_info["Sodium_(mg)"]) # Panndas认为NaN是个缺失值，默认从小到大排序
# sort_values()的 ascending 属性默认为 True（升序），False(降序)
food_info.sort_values("Sodium_(mg)", inplace=True, ascending=False)
print(food_info["Sodium_(mg)"])

