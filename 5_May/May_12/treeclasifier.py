import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Create a sample dataset
data = {
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000],
    'Education': ['Bachelor', 'Master', 'PhD', 'Bachelor', 'Master'],
    'Purchased': [0, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

# Prepare the data
X = df.drop('Purchased', axis=1)
y = df['Purchased']

# Encode categorical data
encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X[['Education']]).toarray()
X_encoded = pd.DataFrame(X_encoded, columns=encoder.get_feature_names(['Education']))
X_numerical = X.drop('Education', axis=1)
X_preprocessed = pd.concat([X_numerical, X_encoded], axis=1)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_preprocessed, y, test_size=0.2, random_state=0)

# Initialize and train the classifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

# Predict and evaluate the model
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

