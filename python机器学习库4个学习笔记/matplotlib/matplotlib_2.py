#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 柱形图
import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange

reviews = pd.read_csv("C:\\Users\\TNanko\\PycharmProjects\\MachineLearning\\venv\\Data\\pandas\\fandango_score_comparison.csv")
cols = ["FILM", "RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue", "Fandango_Stars"]
norm_reviews = reviews[cols]
print(norm_reviews[:1])

num_cols = ["RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue", "Fandango_Stars"]
bar_heights = norm_reviews.ix[0, num_cols].values
print(bar_heights)
bar_positions = arange(5) + 0.75
print(bar_positions)
fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, 0.3)
plt.show()



num_cols = ["RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue", "Fandango_Stars"]
bar_heights = norm_reviews.ix[0, num_cols].values # 高度
bar_positions = arange(5) + 0.75 # 位置
tick_positions = range(1, 6)
fig, ax = plt.subplots()

ax.bar(bar_positions, bar_heights, 0.5) # 竖着放置
ax.set_xticks(tick_positions)
ax.set_xticklabels(num_cols, rotation=45)

ax.set_xlabel("Rating Sourse")
ax.set_ylabel("Average Rating")
ax.set_title("Average User Rating For Avengers: Age of Ultron (2015)")
plt.show()



num_cols = ["RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue", "Fandango_Stars"]
bar_widths = norm_reviews.ix[0, num_cols].values
bar_positions = arange(5) + 0.75
tick_positions = range(1, 6)
fig, ax = plt.subplots()
ax.barh(bar_positions, bar_widths, 0.5) # 横着放置

ax.set_yticks(tick_positions)
ax.set_yticklabels(num_cols)
ax.set_ylabel("Rating Source")
ax.set_xlabel("Average Rating")
ax.set_title("Average User Rating For Avengers: Age of Ultron (2015)")
plt.show()

# 散点图
fig, ax = plt.subplots()
ax.scatter(norm_reviews["Fandango_Ratingvalue"], norm_reviews["RT_user_norm"])
ax.set_xlabel("Fandango")
ax.set_ylabel("Rotten Tomatoes")
plt.show()



fig = plt.figure(figsize=(5, 10))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
ax1.scatter(norm_reviews["Fandango_Ratingvalue"], norm_reviews["RT_user_norm"])
ax1.set_xlabel("Fandango")
ax1.set_ylabel("Rotten Tomatoes")
ax2.scatter(norm_reviews["RT_user_norm"], norm_reviews["Fandango_Ratingvalue"])
ax2.set_xlabel("Rotten Tomatoes")
ax2.set_ylabel("Fandango")
plt.show()
