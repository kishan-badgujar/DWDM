# Naive Bayes Classification

# Step 1: Import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Step 2: Load dataset
iris = load_iris()
X = iris.data
y = iris.target

print("Dataset Loaded Successfully")
print("Total Records:", len(X))

# Step 3: Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))

# Step 4: Train the Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# Step 5: Test the model
y_pred = model.predict(X_test)

print("\nActual Values:", y_test)
print("Predicted Values:", y_pred)

# Step 6: Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy * 100, "%")

# Step 7: Display confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))