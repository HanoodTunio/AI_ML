import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Read the dataset into a DataFrame

data = pd.read_csv('Iris.csv')


# Data Wrangling/ Rename the columns for better readability
data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'variety']

# Encode the 'variety' column to numerical values
data['variety'] = data['variety'].map({'Setosa': 0, 'Versicolor': 1, 'Virginica': 2})

# Split the data into features and target
X = data.drop(columns=['variety'])  # Features
y = data['variety']  # Target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R^2 Score:", r2)

# Example input data point
example_data = [[6.5, 3, 5.2, 2]]  # Sepal Length, Sepal Width, Petal Length, Petal Width

# Predict the class using the trained model
predicted_class = model.predict(example_data)

print("Predicted Class:", predicted_class)

