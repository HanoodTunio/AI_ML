import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_csv('data.csv')

# Extract the features (independent variable) and target variable (dependent variable)
X = data[['Size (sq.ft.)']].values
y = data['price($)'].values

# Create and fit linear regression model
model = LinearRegression()
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Predict price for a new area value
new_area = np.array([[100]])  # Example new area value
predicted_price = model.predict(new_area)
print("Predicted Price for New Area:", predicted_price)

# Visualize the data and the linear regression line
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X, y_pred, color='red', linewidth=2, label='Linear Regression')
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Linear Regression')
plt.legend()
plt.show()

