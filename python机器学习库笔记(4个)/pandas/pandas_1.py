#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pandas

# 数据读取
food_info = pandas.read_csv("C:\\Users\\TNanko\\PycharmProjects\\MachineLearning\\venv\\Data\\pandas\\food_info.csv")
print(type(food_info))
print(food_info.dtypes)# 打印出数据中的数据类型（object:字符型）
# print(help(pandas.read_csv))

print(food_info.head())# 不指定参数时，只输出前5条数据
print(food_info.head(3))# 只输出前3条数据
print(food_info.tail())# 不指定参数时，只输出后5条数据
print(food_info.columns)# 输出数据的列名（每一列的第一行）
print(food_info.shape)# 输出矩阵的维度


# Pandas索引

# 按行取数据
# print(food_info[0])# 报错
# print(food_info.loc[i]) 输出第 i 条数据
print(food_info.loc[0])# 输出第0条数据，不同于numpy,不可以直接使用index索引得出结果，使用loc[]
print(food_info.loc[3:6])# 切片取数据，和python类似
two_five_ten = [2, 5, 10]
print(food_info.loc[two_five_ten])
# dtype中常见的类型
# object - For string values
# int - For integer values
# float - For float values
# datatime - For time values
# bool - For Boolean values


# 按列取数据

# 定位一列
# 法1
ndb_col = food_info["NDB_No"]# “NDB_No”其实就是索引index（请仔细观察第15行代码输出的结果 print(food_info.columns)）
print(ndb_col)
# 法2(其实两种方法本质是一样的)
col_name = "NDB_No"
ndb_col = food_info[col_name]
# 定位两列（方法类似于上面的法2）
columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[columns]
print(zinc_copper)

# 区分（查找）数据中后缀 g , mg 的列
col_names = food_info.columns.tolist()# 取出列名
print(col_names)
gram_columns = []

for c in col_names:
    if c.endswith("(g)"):
        gram_columns.append(c)
        # print("gram_columns:", gram_columns)
gram_df = food_info[gram_columns]
print(gram_df.head(3))# 输出每列的前三行数据
