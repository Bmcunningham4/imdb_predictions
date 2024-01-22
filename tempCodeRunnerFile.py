df2 = pd.read_csv("watchlist.csv")
watchlist_df = df.drop(["DateAdded", "Type"])
print(watchlist_df.head())