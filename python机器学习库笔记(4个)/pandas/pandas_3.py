#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pandas as pd
import numpy as np

titanic_survival = pd.read_csv("C:\\Users\\TNanko\\PycharmProjects\\MachineLearning\\venv\\Data\\pandas\\titanic_train.csv")
print(titanic_survival.head())
age = titanic_survival["Age"]
print("type:", type(age)) # pandas_4
print(age.loc[0:10])
age_is_null = pd.isnull(age) # 用于判断是否是缺失值
print(age_is_null)
age_null_true = age[age_is_null]
print(age_null_true)
age_null_count = len(age_null_true)
print(age_null_count)
mean_age = sum(titanic_survival["Age"])/len(titanic_survival["Age"]) # 计算平均年龄
print(mean_age) # 因为在数据“年龄”中有缺失值，所以无法计算，输出为 NaN

good_ages = titanic_survival["Age"][age_is_null == False] # 取出无缺失值（年龄）的数据
print(good_ages)
correct_mean_age = sum(good_ages) / len(good_ages) # 计算非缺失值的平均年龄
print(correct_mean_age)
correct_mean_age = titanic_survival["Age"].mean() # 不建议
print(correct_mean_age)

# 查看每个船舱的舱位等级船票的平均价格
passenger_classes = [1, 2, 3]
fares_by_class = {}
for this_class in passenger_classes:
    pclass_rows = titanic_survival[titanic_survival["Pclass"] == this_class]
    pclass_fares = pclass_rows["Fare"]
    fare_for_class = pclass_fares.mean()
    fares_by_class[this_class] = fare_for_class
print(fares_by_class)

# 住各个等级的船舱平均获救多少人
passenger_survival = titanic_survival.pivot_table(index="Pclass", values="Survived", aggfunc=np.mean) # index（以哪个列为基准） values(处理的数据) aggfunc（计算的函数）
print(passenger_survival)

passenger_age = titanic_survival.pivot_table(index="Pclass", values="Age", aggfunc=np.mean)
print(passenger_age)
# 这边产生一个疑惑，当参数 aggfunc 不写的时候，输出的结果不变，即下一行代码与第41行代码输出的结果一致
# passenger_age = titanic_survival.pivot_table(index="Pclass", values="Age")
# 解释：当 aggfunc 指定函数后，下一次调用 pivot_table() 的 aggfunc 默认使用的参数是上一次使用的参数，直到传入新的参数位置

# 各个码头登船的总得船票的价格，获救人数
port_stats = titanic_survival.pivot_table(index="Embarked", values=["Fare", "Survived"], aggfunc=np.sum)
print(port_stats)

# dropna()如果有缺失值，则将数据样本去掉
drop_na_columns = titanic_survival.dropna(axis=1)
new_titanic_survival = titanic_survival.dropna(axis=0, subset=["Age", "Sex"]) # 在 "Age","Sex" 两列中检查缺失值
print(new_titanic_survival)

row_index_83_age = titanic_survival.loc[83, "Age"] # 查看样本 83 的年龄
row_index_766_pclass = titanic_survival.loc[766, "Pclass"]
print(row_index_83_age)
print(row_index_766_pclass)

# 排序
new_titanic_survival = titanic_survival.sort_values("Age", ascending=False)
print(new_titanic_survival[0:10])
titanic_reindexed = new_titanic_survival.reset_index(drop=True) # 形成新的 index 值
print("-------------------------------------")
print(titanic_reindexed.loc[0:10])

# apply() 自定义函数
# 返回第100行数据
def hunderdth_row(column):
    hunderdth_item = column.loc[99]
    return hunderdth_item

hunderdth_row = titanic_survival.apply(hunderdth_row)
print(hunderdth_row)

# 计算每一列的缺失值的个数
def not_null_count(column):
    column_null = pd.isnull(column)
    null = column[column_null]
    return len(null)

column_null_count = titanic_survival.apply(not_null_count)
print(column_null_count)

# 对数据进行转换
def which_class(row):
    pclass = row["Pclass"]
    if pd.isnull(pclass):
        return "Unknown"
    elif pclass == 1:
        return "First Class"
    elif pclass == 2:
        return "Second Class"
    elif pclass == 3:
        return "Third Class"

classes = titanic_survival.apply(which_class, axis=1)
print(classes)

def is_minor(row):
    if row["Age"] < 18:
        return True
    else:
        return False

minors = titanic_survival.apply(is_minor, axis=1)
print(minors)

def generate_age_label(row):
    age = row["Age"]
    if pd.isnull(age):
        return "unknown"
    elif age < 18:
        return "minor"
    else:
        return "adult"

age_labels = titanic_survival.apply(generate_age_label, axis=1)
print(age_labels)

titanic_survival["age_labels"] = age_labels
age_group_survival = titanic_survival.pivot_table(index="age_labels", values="Survived")
print(age_group_survival)
