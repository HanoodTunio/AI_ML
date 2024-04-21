from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and testing sets for binary classification
X_binary = X[y != 2]
y_binary = y[y != 2]
X_train_binary, X_test_binary, y_train_binary, y_test_binary = train_test_split(X_binary, y_binary, test_size=0.2, random_state=42)

# Split the data into training and testing sets for multi-class classification
X_train_multi, X_test_multi, y_train_multi, y_test_multi = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize classifiers
classifiers = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(),
    "SVM": SVC()
}

# Train and evaluate classifiers for binary classification
print("Binary Classification Results:")
for name, clf in classifiers.items():
    clf.fit(X_train_binary, y_train_binary)
    y_pred = clf.predict(X_test_binary)
    accuracy = accuracy_score(y_test_binary, y_pred)
    print(f"{name}: Accuracy = {accuracy:.2f}")
    print(f"Classification Report for {name}:")
    print(classification_report(y_test_binary, y_pred))
    print()

# Train and evaluate classifiers for multi-class classification
print("Multi-class Classification Results:")
for name, clf in classifiers.items():
    clf.fit(X_train_multi, y_train_multi)
    y_pred = clf.predict(X_test_multi)
    accuracy = accuracy_score(y_test_multi, y_pred)
    print(f"{name}: Accuracy = {accuracy:.2f}")
    print(f"Classification Report for {name}:")
    print(classification_report(y_test_multi, y_pred))
    print()
