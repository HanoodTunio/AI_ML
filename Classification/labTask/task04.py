from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score, classification_report

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Binary classification: Consider only classes 0 and 1
X_binary = X[y != 2]
y_binary = y[y != 2]

# Multi-class classification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the LDA model for binary classification
lda_binary = LinearDiscriminantAnalysis()

# Train the binary LDA model
lda_binary.fit(X_binary, y_binary)

# Make predictions for binary classification
y_pred_binary = lda_binary.predict(X_binary)

# Calculate accuracy for binary classification
accuracy_binary = accuracy_score(y_binary, y_pred_binary)
print("Binary Classification Accuracy:", accuracy_binary)

# Classification report for binary classification
print("Binary Classification Report:")
print(classification_report(y_binary, y_pred_binary))

# Initialize the LDA model for multi-class classification
lda_multi = LinearDiscriminantAnalysis()

# Train the multi-class LDA model
lda_multi.fit(X_train, y_train)

# Make predictions for multi-class classification
y_pred_multi = lda_multi.predict(X_test)

# Calculate accuracy for multi-class classification
accuracy_multi = accuracy_score(y_test, y_pred_multi)
print("\nMulti-class Classification Accuracy:", accuracy_multi)

# Classification report for multi-class classification
print("\nMulti-class Classification Report:")
print(classification_report(y_test, y_pred_multi))
