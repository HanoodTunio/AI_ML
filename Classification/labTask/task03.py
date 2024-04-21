"""Logistic Regression is a statistical method used for binary classification tasks, where the outcome
variable is categorical and has only two possible outcomes. Despite its name containing "regression,"
logistic regression is primarily used for classification, not regression. It models the probability
that a given input belongs to a particular category.

Logistic regression can be extended to handle multi-class classification problems through techniques 
like one-vs-rest (OvR) or multinomial logistic regression. However, it's originally designed for binary
classification."""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# For binary classification, let's consider only two classes: 0 and 1
X_binary = X[y != 2]
y_binary = y[y != 2]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_binary, y_binary, test_size=0.2, random_state=42)

# Initialize the logistic regression model
log_reg = LogisticRegression()

# Train the model
log_reg.fit(X_train, y_train)

# Make predictions on the test set
y_pred = log_reg.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Parameters of the logistic regression model
print("Intercept:", log_reg.intercept_)
print("Coefficients:", log_reg.coef_)
print("Classes:", log_reg.classes_)
print("Number of iterations:", log_reg.n_iter_)
