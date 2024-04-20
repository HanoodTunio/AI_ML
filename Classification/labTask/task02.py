"""Binary classification involves predicting between two classes or categories. 
    For example, determining whether an email is spam or not spam.

Multi-class classification involves predicting among multiple classes or categories. 
    For instance, identifying the species of a flower as either iris-setosa, iris-versicolor, or iris-virginica.

The Naive Bayes classifier is a probabilistic machine learning model based on Bayes' theorem with an assumption 
of independence between features. It calculates the probability of each class given the input features and selects the class with the highest probability as the prediction."""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv('Iris.csv')

# Preprocessing for binary classification (setosa vs. non-setosa)
binary_data = data[data['variety'].isin(['Setosa', 'Non-Setosa'])]
X_binary = binary_data.drop(columns=['variety'])
y_binary = binary_data['variety']

# Preprocessing for multi-class classification
X_multi = data.drop(columns=['variety'])
y_multi = data['variety']

# Encode the target variable for both binary and multi-class
label_encoder = LabelEncoder()
y_binary = label_encoder.fit_transform(y_binary)
y_multi = label_encoder.fit_transform(y_multi)

# Splitting data into training and testing sets for both binary and multi-class
X_train_binary, X_test_binary, y_train_binary, y_test_binary = train_test_split(X_binary, y_binary, test_size=0.2, random_state=42)
X_train_multi, X_test_multi, y_train_multi, y_test_multi = train_test_split(X_multi, y_multi, test_size=0.2, random_state=42)

# Instantiate the Naive Bayes classifier
nb_classifier = GaussianNB()

# Fit the model for both binary and multi-class
nb_classifier.fit(X_train_binary, y_train_binary)
nb_classifier.fit(X_train_multi, y_train_multi)

# Predictions for both binary and multi-class
y_pred_binary = nb_classifier.predict(X_test_binary)
y_pred_multi = nb_classifier.predict(X_test_multi)

# Evaluation for both binary and multi-class
binary_accuracy = accuracy_score(y_test_binary, y_pred_binary)
multi_accuracy = accuracy_score(y_test_multi, y_pred_multi)

print("Binary Classification Accuracy:", binary_accuracy)
print("Multi-class Classification Accuracy:", multi_accuracy)
