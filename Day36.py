# Dataset Practice

print("Create Student Dataset")
import pandas as pd
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [20, 35, 50, 65, 80, 85, 90, 95]
}
df = pd.DataFrame(data)
print(df)

print("Create Salary Dataset")
import pandas as pd
data = {
    "Experience": [1, 2, 3, 4, 5, 6],
    "Salary": [25000, 32000, 40000, 50000, 62000, 70000]
}
df = pd.DataFrame(data)
print(df)

print("Create Sales Dataset")
import pandas as pd
data = {
    "Advertising": [10, 20, 30, 40, 50, 60],
    "Sales": [100, 180, 260, 340, 420, 500]
}
df = pd.DataFrame(data)
print(df)

# Train-Test Split Practice

print("Split Dataset")
import pandas as pd
from sklearn.model_selection import train_test_split
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [20, 35, 50, 65, 80, 85, 90, 95]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Marks"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Training Data:")
print(X_train)
print("\nTesting Data:")
print(X_test)

# test_size=0.2
# This means 20% of the dataset is used for testing, while 80% is used for training.
# random_state=42
# This keeps the data split the same every time the program runs, making the results reproducible.

# Model Training

print("Train Linear Regression Model")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [20, 35, 50, 65, 80, 85, 90, 95]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Marks"]
X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.2,  random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
print("Model Trained Successfully")

# 2. Use fit()
# model.fit(X_train, y_train)
# The fit() function trains the model using the training data.
# 3. Train with Training Data Only
# model.fit(X_train, y_train)
# The model learns only from the training dataset. The testing dataset is used later to evaluate the model.

# Prediction Practice

print("Predict Test Data")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [20, 35, 50, 65, 80, 85, 90, 95]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Marks"]
X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.2,  random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(predictions)

print("Compare Actual vs Predicted")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [20, 35, 50, 65, 80, 85, 90, 95]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Marks"]
X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.2,  random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
result = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions
})
print(result)

print("Print Accuracy Score")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [20, 35, 50, 65, 80, 85, 90, 95]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Marks"]
X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.2,  random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
print("Accuracy:", score)
