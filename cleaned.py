
import pandas as pd

#! Cleaning, My Ratings CSV file
df = pd.read_csv("imdb_ratings.csv")
ratings_df = df.drop(["Const", "URL", "Release Date", "Directors"], axis = 1) #todo: I don't necessarily need to remove title, cause it'll make it harder knowing which movie I'm talking about!

#? converting out of object type!
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

#todo: Remvoing rows that have Nan values (just 3)
ratings_df.dropna(inplace=True)
# print(len(ratings_df)) --- Tick come and change this later !!

#! Cleaning My Watchlist CSV file!
df2 = pd.read_csv("watchlist.csv")
watchlist_df = df2.drop(["DateAdded", "Type"], axis=1)
movie_names = watchlist_df.Title

Runtimes = [85, 113, 85, 108, 124, 101, 148, 95, 78, 108, 151, 128, 98, 104, 106, 129, 107, 50, 112, 133, 139, 125, 123, 125, 115]
watchlist_df["Runtimes"] = Runtimes
# print(watchlist_df.head()) ------ All Clear...


#todo: List of things I want to explore in each df, Don't do this for too long (Just first) probs..
#* Get into a .Jupyter file and start this!!
"""
____ Var vs My Ratings:
Runtime, 
IMDb Rating, 
Year, 
Num votes, 
Day Rated, 
Genre, 
Title Type!
"""





#* This stuff is not relevant here but noting for later..
#? Feature selection methods: Filter, wrapper and embedded
"""
Filter 
- Checks correlation basically before using ...of each variable 
- Doesn't work well for multivariate relationships since it measures individually
Yes I should use!

Wrapper:
- They by using a search algorithm to find which combination of features can optimize performance of a given model..
- eg. fwd/ backward bidirectional crap and recursive ..
Yes I should try with top 5!

Embedded:
-Similar to wrapper but don't quite get If I figure out can use..




"""











