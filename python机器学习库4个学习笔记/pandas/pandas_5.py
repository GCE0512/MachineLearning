#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pandas as pd

fandango = pd.read_csv("C:\\Users\\TNanko\\PycharmProjects\\MachineLearning\\venv\\Data\\pandas\\fandango_score_comparison.csv")
print(type(fandango))
fandango_films = fandango.set_index("FILM", drop=False)
print(fandango_films.index) # DataFrame 指定索引

fandango_films["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]
fandango_films.loc["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]

# Specific movie
fandango_films.loc["Kumiko, The Treasure Hunter (2015)"]

# Selecting list of movies
movies = ["Kumiko, The Treasure Hunter (2015)", "Do You Believe? (2015)", "Ant-Man (2015)"]
print(fandango_films.loc[movies])

import numpy as np

types = fandango_films.dtypes
print(types)
float_columns = types[types.values == "float64"].index
float_df = fandango_films[float_columns]
print(float_df)
deviations = float_df.apply(lambda x: np.std(x))

# lambda 匿名函数
rt_mt_user = float_df[["RT_user_norm", "Metacritic_user_nom"]]
print(rt_mt_user.apply(lambda x: np.std(x), axis=1)) # 返回标准差

