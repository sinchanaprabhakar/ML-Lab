from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

# Load the Iris dataset
iris = load_iris()

# Separate features (X) and target labels (y)
X = iris.data
y = iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Gaussian Naive Bayes classifier
clf = GaussianNB()

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Evaluate the performance (accuracy)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Make a prediction for a new flower sample (replace with your sample)
new_flower = [[5.1, 3.5, 1.4, 0.2]]  # Replace with new flower features (sepal length, sepal width, petal length, petal width)
predicted_class = clf.predict(new_flower)[0]
iris_names = iris.target_names

print("\nPredicted class:", iris_names[predicted_class])
