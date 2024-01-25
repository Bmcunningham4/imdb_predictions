
import pandas as pd

#! Cleaning, My Ratings CSV file
df = pd.read_csv("Data/imdb_ratings.csv")
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

#? Removing 3 empty rows (with no runtimes)
ratings_df.dropna(inplace=True)
# print(len(ratings_df)) 



#! Cleaning My Watchlist CSV file!
df2 = pd.read_csv("Data/watchlist.csv")
watchlist_df = df2.drop(["DateAdded", "Type"], axis=1)
movie_names = watchlist_df.Title

Runtimes = [85, 113, 85, 108, 124, 101, 148, 95, 78, 108, 151, 128, 98, 104, 106, 129, 107, 50, 112, 133, 139, 125, 123, 125, 115]
watchlist_df["Runtime (mins)"] = Runtimes

#? Creating new column Day_Rated and setting it to 3487, which would be the present day of 26/1/24 (To allow the ML model to use this feature for predictions)
watchlist_df["Day_Rated"] = 3487




#! Train-test split
#? 1) Ideally would split data like this, since some genres might help the ML models
X_1 = ratings_df[['IMDb Rating', 'Runtime (mins)', 'Year', 'Num Votes', 'Day_Rated',
                'Action', 'Adventure', 'Animation', 'Biography', 'Comedy',
                'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Game-Show',
                'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Reality-TV',
                'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western',
                'movie', 'tvMiniSeries', 'tvMovie', 'tvSeries', 'video', 'videoGame']]
y_1 = ratings_df['Your Rating']

#? 2) Will have to chose option 2 since the watchlist df that I'm going to making predictions on only includes these features!
X = ratings_df[['IMDb Rating', 'Runtime (mins)', 'Year', 'Num Votes', 'Day_Rated',]]
y = ratings_df['Your Rating']













#? Code below here is used and explained in the notebook files ----------------------------
# Changing runtimes (from exploratory_analysis.ipynb)
sample_numbers = [4, 10, 58, 247, 828, 883, 932, 980, 983, 1013, 1019, 1020, 1022, 1039, 1052]
correct_runtimes = [54, 42, 23, 49, 23, 44, 46, 42, 38, 44, 34, 28, 32, 56, 41] # Googled These 
ratings_df.loc[sample_numbers, "Runtime (mins)"] = correct_runtimes

def valid_int(prompt, min_val, max_val):
    while True:
        try:
            user_input = float(input(prompt))
            if min_val <= user_input <= max_val:
                return user_input
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
