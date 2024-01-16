from cleaned import ratings_df
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


#? Quick test of basic set up!
X = ratings_df[['IMDb Rating', 'Runtime (mins)', 'Year', 'Num Votes',
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

# Evaluation..
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')