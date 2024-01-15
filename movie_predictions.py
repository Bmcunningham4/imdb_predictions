import pandas as pd


df = pd.read_csv("imdb_ratings.csv")
print(df.head())

print(df.columns)

ratings_df = df.drop(["Const", "URL"], axis = 1)
print(ratings_df.head())
print()


#* Quick exploration
avg_rating = ratings_df["Your Rating"].mean()
print(f"Your average movie rating on imdb is {round(avg_rating, 2)} / 10", '\n')

num_list = list(range(1,11))
num_list.reverse()

for num in num_list:
    rating  = ratings_df[ratings_df["Your Rating"] == num]["Your Rating"].count()
    print(f"You have rated {rating} movies with a rating of {num} / 10")



