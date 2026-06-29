# Regression Practice

print("Create Marks Prediction Dataset")
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
print(prediction)

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
    "Sales": [100, 180, 260, 340, 420]
}
df = pd.DataFrame(data)
X = df[["Advertising"]]
y = df["Sales"]
model = LinearRegression()
model.fit(X, y)
prediction = model.predict([[60]])
print("Predicted Sales:", prediction)

# Classification Practice

print("Pass/Fail Prediction")
from sklearn.linear_model import LogisticRegression 
import pandas as pd 
data = { "Hours": [1, 2, 3, 4, 5], "Result": [0, 0, 0, 1, 1] } 
df = pd.DataFrame(data) 
X = df[["Hours"]] 
y = df["Result"] 
model = LogisticRegression() 
model.fit(X, y) 
prediction = model.predict([[6]]) 
print(prediction) 

# Dataset Analysis

print("Regression Dataset")
import pandas as pd
data = {
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [25000, 35000, 45000, 55000, 65000]
}
df = pd.DataFrame(data)
print(df)

print("Classification Dataset")
import pandas as pd
data = {
    "Marks": [35, 50, 65, 80],
    "Result": ["Fail", "Pass", "Pass", "Pass"]
}
df = pd.DataFrame(data)
print(df)
