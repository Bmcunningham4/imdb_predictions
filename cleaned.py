
import pandas as pd

# from clean import ratings_df, genres_df ------ This was printing all the garbage on that file..

#! Simplified shit (With clean data) import wasn't clean
df = pd.read_csv("imdb_ratings.csv")
ratings_df = df.drop(["Const", "URL", "Release Date", "Directors", "Title"], axis = 1)

#? converting out of objec type!
ratings_df[["Genres", "Title Type"]] = ratings_df[["Genres", "Title Type"]].astype("category")
ratings_df["Date Rated"] = pd.to_datetime(ratings_df["Date Rated"], format="%d/%m/%Y", errors="coerce")
min_date = ratings_df["Date Rated"].min()
ratings_df["Day_Rated"] = (ratings_df["Date Rated"] - min_date).dt.days # Adding column so regression can be performed with numeric vals

#? One hot encoding
genres_df = ratings_df['Genres'].str.get_dummies(sep=', ')
title_type_df = pd.get_dummies(ratings_df["Title Type"], dtype=int)

#? Finalising new_df
ratings_df = pd.concat([ratings_df, genres_df, title_type_df], axis=1)
ratings_df = ratings_df.drop(['Genres', 'Title Type'], axis=1)
# print(ratings_df.head())










