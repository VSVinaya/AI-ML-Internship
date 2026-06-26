# Dataset Practice

print("Create Student Dataset")
import pandas as pd
data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 40, 60, 80, 100]
}
df = pd.DataFrame(data)
print(df)


print("Create Salary Dataset")
import pandas as pd
data = {
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [25000, 35000, 45000, 55000, 65000]
}
df = pd.DataFrame(data)
print(df)


print("Create Sales Dataset")
import pandas as pd
data = {
    "Advertising": [10, 20, 30, 40, 50],
    "Sales": [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)
print(df)

# Model Training

print("Train Linear Regression Model")
import pandas as pd
from sklearn.linear_model import LinearRegression
data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 40, 60, 80, 100]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Marks"]
model = LinearRegression()
model.fit(X, y)
print("Model Trained Successfully")

# Prediction Practice

print("Predict Marks")
import pandas as pd
from sklearn.linear_model import LinearRegression
data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 40, 60, 80, 100]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Marks"]
model = LinearRegression()
model.fit(X, y)
prediction = model.predict([[6]])
print("Predicted Marks:", prediction)


print("Predict Salary")
import pandas as pd
from sklearn.linear_model import LinearRegression
data = {
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [25000, 35000, 45000, 55000, 65000]
}
df = pd.DataFrame(data)
X = df[["Experience"]]
y = df["Salary"]
model = LinearRegression()
model.fit(X, y)
prediction = model.predict([[6]])
print("Predicted Salary:", prediction)


print("Predict Sales Values")
import pandas as pd
from sklearn.linear_model import LinearRegression
data = {
    "Advertising": [10, 20, 30, 40, 50],
    "Sales": [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)
X = df[["Advertising"]]
y = df["Sales"]
model = LinearRegression()
model.fit(X, y)
prediction = model.predict([[60]])
print("Predicted Sales:", prediction)
