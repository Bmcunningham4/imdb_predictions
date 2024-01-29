# imdb_predictions
 
# Project completed on: 26/1/24

# Project Description
For my latest data science project, I leveraged my newfound machine learning skills, incorporating both unsupervised and supervised learning techniques using the renowned scikit-learn module. Drawing on a personal dataset consisting of over 1000 IMDb movie ratings, I embarked on a comprehensive exploration of my movie preferences. Through extensive data manipulation and interactive analysis, I delved into the predictive capabilities of three distinct machine learning models: K-nearest neighbors, decision tree regressors, and multiple linear regression. Additionally, I employed k-means clustering to unveil trends and visualize clusters within the dataset, providing a holistic view of my movie preferences and paving the way for insightful discoveries in the realm of personalized recommendation systems.



# Navigation of the Repository 
Data: 
The Data folder contains 2 csv files, that I have downloaded from IMDb.com
- imdb_ratings.csv : Contains my personal movie ratings, as well as features for each movie such as genres, runtime, etc.
- watchlist.csv : Contains 25 movies that I use for predictions to assess their viewing potential.

data_cleaning.py:
- Contains the necessary dataframes cleaning for conducting exploratory analysis, including one-hot encoding genres and fixing NaN values.

exploratory_analysis.ipynb
- Contains visualizations of the distribution of my ratings and key features such as IMDb Rating, Runtime, Year, Num votes, and Day Rated.

mlr.ipynb, knn.ipynb, dtree.ipynb
Contain respective analyses for each machine learning technique (multiple linear regression, decision trees, k-nearest neighbors).  
- Each file includes feature selection, model training, model evaluations, predictions, and visualizations of various relationships.

kmc.ipynb
- Contains the Elbow method, cluster exploration, and visualizations of cluster relationships.











