# Dataset Creation 

print("Student Result Dataset")
import pandas as pd
data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
print(df)


print("Disease Dataset")
import pandas as pd
data = {
    "Temperature": [98, 99, 100, 101, 102],
    "Disease": [0, 0, 0, 1, 1]
}
df = pd.DataFrame(data)
print(df)


print("Loan Approval Dataset")
import pandas as pd
data = {
    "Income": [20000, 30000, 40000, 50000, 60000],
    "Approved": [0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
print(df)

# Model Building 

print("Create Random Forest Model 2. Train the Model 3. Make Predictions")
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Result"]
model = RandomForestClassifier()
model.fit(X, y)
prediction = model.predict([[4]])
print("Prediction:", prediction)

# Prediction Practice

print("Predict Student Result")
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Result"]
model = RandomForestClassifier()
model.fit(X, y)
prediction = model.predict([[6]])
print("Student Result:", prediction)


print("Predict Disease Status")
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
data = {
    "Temperature": [98, 99, 100, 101, 102],
    "Disease": [0, 0, 0, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Temperature"]]
y = df["Disease"]
model = RandomForestClassifier()
model.fit(X, y)
prediction = model.predict([[101]])
print("Disease Status:", prediction)


print("Predict Loan Approval")
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
data = {
    "Income": [20000, 30000, 40000, 50000, 60000],
    "Approved": [0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Income"]]
y = df["Approved"]
model = RandomForestClassifier()
model.fit(X, y)
prediction = model.predict([[55000]])
print("Loan Approval:", prediction)