import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

#todo: Other ideas
"""
Clustering? ..
Linear Regression
Decision Trees
Random Forest
Support Vector Machines (SVM)
Gradient Boosting
"""

#! Created a template for how I can carry out K-Nearest neighbours analysis
# Load your IMDb ratings dataset
df = pd.read_csv('your_ratings_dataset.csv')

# Assume 'Your Rating' is your target variable and other relevant columns are features
X = df[['Feature1', 'Feature2', ...]]  # Replace with your features
y = df['Your Rating']

# Data preprocessing
# For example, handle missing values and one-hot encode categorical features

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling (important for KNN)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# K-Nearest Neighbors
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

# Predictions
y_pred = knn.predict(X_test_scaled)

# Model evaluation
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
