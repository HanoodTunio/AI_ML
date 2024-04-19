# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Data Wrangling
# Load the Iris dataset
df = pd.read_csv('Iris.csv')
df.columns = ["sepal.length", "sepal.width", "petal.length", "petal.width", "variety"]
df['variety'] = df['variety'].map({0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'})

# Drop rows with NaN values
df.dropna(inplace=True)

# Check for missing values
print(df.isnull().sum())

# Step 2: Multiple Linear Regression
X = df.drop(columns=["variety"])  # Features
y = df["variety"]  # Target

# Split the data into training and testing sets
if len(df) > 0:  # Ensure dataset is not empty
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
else:
    print("Dataset is empty after handling missing values")

# Fit the multiple linear regression model to the training data
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model on the testing data
y_pred = model.predict(X_test)

# Calculate Mean Squared Error (MSE) as a measure of model performance
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
