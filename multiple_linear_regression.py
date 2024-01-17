from cleaned import ratings_df
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

#* Make a note that this most likely contains overfitting since it has 34 features (training will listen to the noise too much rather than what's important!)
#todo: Can

#? Quick test of basic set up!
X = ratings_df[['IMDb Rating', 'Runtime (mins)', 'Year', 'Num Votes', 'Day_Rated',
             'Action', 'Adventure', 'Animation', 'Biography', 'Comedy',
             'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Game-Show',
             'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Reality-TV',
             'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western',
             'movie', 'tvMiniSeries', 'tvMovie', 'tvSeries', 'video', 'videoGame']]
y = ratings_df['Your Rating']


# Handle missing values if any (imputation or dropping) - #? Check if this needs to be done?
X = X.dropna()
y = y[X.index]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
# print(y_pred) -- minteresting..

# Evaluation..
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred) #* Can use either this one represents the mean diff betwen predicted an actual - makes intuitive sense!
print(f'Mean Squared Error: {mse}')
print(f'Mean Absolute Error: {mae}')


#? New stuff) Visualizing results with matplotlib
# plt.scatter(y_test, y_pred, alpha=0.4)
# plt.xlabel("Ratings: /10")
# plt.ylabel("Predicted Ratings: /10")
# plt.title("Actual Ratings vs Predicted Ratings")
# plt.show() #* My Graph looks weird because My actual ratings are all whole numbers.. :(
#! ^^ This is y Jupyter notebook files are better for as you go visualisation!


#! Extra crap: 
print(model.coef_)
print(model.intercept_)

#? Testing whether to remove points based on correlation:
# plt.scatter(ratings_df[['IMDb Rating']], ratings_df["Your Rating"], alpha = 0.4)  #* Strong correlation..
# plt.show()
# plt.close()
# plt.scatter(ratings_df[['Day_Rated']], ratings_df["Your Rating"], alpha = 0.4)  #* Nothing really
# plt.show()
# plt.scatter(ratings_df[['Runtime (mins)']], ratings_df["Your Rating"], alpha = 0.4)  #! This gives me important info that min-max normalization won't be good due to massive outliers (also weak correlation)
# plt.show()
# plt.close()