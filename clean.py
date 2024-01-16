import pandas as pd

df = pd.read_csv("imdb_ratings.csv")

#? Removing columns
ratings_df = df.drop(["Const", "URL", "Release Date", "Directors", "Title"], axis = 1)
"""print(ratings_df.head())
print()
print(ratings_df.columns)"""


#? Convert object columns to categorical/ datetime!
ratings_df[["Genres", "Title Type"]] = ratings_df[["Genres", "Title Type"]].astype("category")
ratings_df["Date Rated"] = pd.to_datetime(ratings_df["Date Rated"], format="%d/%m/%Y", errors="coerce")
print(ratings_df.info()) #! woooh!
print(ratings_df.head())

#? Fixing Genres
# print(ratings_df["Title Type"].value_counts(), '\n')

print(ratings_df.Genres[1070])
print(ratings_df.Genres.value_counts())





#* Basic stats
"""
#? Avg Rating
avg_rating = ratings_df["Your Rating"].mean()
print(f"Your average movie rating on imdb is {round(avg_rating, 2)} / 10", '\n')

#? Num movies for each rating
num_list = list(range(1,11))
num_list.reverse()
for num in num_list:
    rating  = ratings_df[ratings_df["Your Rating"] == num]["Your Rating"].count()
    print(f"You have rated {rating} movies with a rating of {num} / 10")
"""



