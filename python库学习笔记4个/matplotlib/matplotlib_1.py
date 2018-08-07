#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 折线图绘制

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv("C:\\Users\\TNanko\\PycharmProjects\\MachineLearning\\venv\\Data\\matplotlib\\UNRATE.csv")
unrate["DATE"] = pd.to_datetime(unrate["DATE"])
print(unrate.head(12))
# plt.plot()
# plt.show()
first_twelve = unrate[0:12]
plt.plot(first_twelve["DATE"], first_twelve["VALUE"])
# plt.xticks(rotation=45) 横坐标倾斜角度
# print(help(plt.xticks))
plt.xlabel("Month") # 标注横坐标
plt.ylabel("Unemployment Rate") # 标注纵坐标
plt.title("Monthly Unemployment Trends, 1948") # 标注折线图标题
plt.show()

# 子图操作
fig = plt.figure()
ax1 = fig.add_subplot(4, 3, 1)
ax2 = fig.add_subplot(4, 3, 2)
ax3 = fig.add_subplot(4, 3, 6)
plt.show()

fig = plt.figure(figsize=(3, 3)) # 指定画图区域的位置
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.plot(np.random.randint(1, 5, 5), np.arange(5))
ax2.plot(np.arange(10) * 3, np.arange(10))
plt.show()

unrate["MONTH"] = unrate["DATE"].dt.month
unrate["MONTH"] = unrate["DATE"].dt.month
fig = plt.figure(figsize=(6, 3))

plt.plot(unrate[0:12]["MONTH"], unrate[0:12]["VALUE"], c="red")
plt.plot(unrate[12:24]["MONTH"], unrate[12:24]["VALUE"], c="blue")
plt.show()

fig = plt.figure(figsize=(10, 6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i * 12
    end_index = (i + 1) * 12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset["MONTH"], subset["VALUE"], c=colors[i], label=label)
plt.legend(loc="best")
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")
plt.title("Monthly Unemployment Trends, 1948-1952")
# print(help(plt.legend))
plt.show()


