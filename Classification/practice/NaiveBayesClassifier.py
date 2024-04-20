import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv('Iris.csv')

# Renaming columns
data.columns = ["sepal.length", "sepal.width", "petal.length", "petal.width", "variety"]

# Selecting features and target
X = data.drop(columns=['variety'])

# Encoding the target variable
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data['variety'])

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instantiate the Naïve Bayes classifier
nb_classifier = GaussianNB()

# Fit the model
nb_classifier.fit(X_train, y_train)

# Predictions
y_pred_train = nb_classifier.predict(X_train)
y_pred_test = nb_classifier.predict(X_test)

# Evaluating the model
train_accuracy = accuracy_score(y_train, y_pred_train)
test_accuracy = accuracy_score(y_test, y_pred_test)
print("Train Accuracy:", train_accuracy)
print("Test Accuracy:", test_accuracy)
