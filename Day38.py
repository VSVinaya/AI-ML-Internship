# Dataset Creation

print("Create Pass/Fail Dataset")
import pandas as pd
data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Result": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
print(df)


print("Create Disease Dataset")
import pandas as pd
data = {
    "Temperature": [98, 99, 100, 101, 102],
    "Disease": [0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
print(df)


print("Create Spam Dataset")
import pandas as pd
data = {
    "Message_Length": [10, 20, 30, 40, 50],
    "Spam": [0, 0, 0, 1, 1]
}
df = pd.DataFrame(data)
print(df)

# Model Training

print("Train and predict Logistic Regression Model")
import pandas as pd
from sklearn.linear_model import LogisticRegression
data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Result": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Result"]
model = LogisticRegression()
model.fit(X, y)
prediction = model.predict([[5]])
print("Prediction:", prediction)

# Prediction Practice

print("Predict Student Result")
import pandas as pd
from sklearn.linear_model import LogisticRegression
data = {
    "Hours": [1, 3, 4, 5, 6],
    "Result": [0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Result"]
model = LogisticRegression()
model.fit(X, y)
prediction = model.predict([[2]])
print(prediction)


print("Predict Disease Status")
import pandas as pd
from sklearn.linear_model import LogisticRegression
data = {
    "Temperature": [98, 99, 100, 101, 102],
    "Disease": [0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Temperature"]]
y = df["Disease"]
model = LogisticRegression()
model.fit(X, y)
prediction = model.predict([[101]])
print("Disease Prediction:", prediction)


print("Predict Spam Message Status")
import pandas as pd
from sklearn.linear_model import LogisticRegression
data = {
    "Message_Length": [10, 20, 30, 40, 50],
    "Spam": [0, 0, 0, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Message_Length"]]
y = df["Spam"]
model = LogisticRegression()
model.fit(X, y)
prediction = model.predict([[45]])
print("Spam Prediction:", prediction)

# Probability Analysis

print("Use predict_proba()")
import pandas as pd
from sklearn.linear_model import LogisticRegression
data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Result": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Result"]
model = LogisticRegression()
model.fit(X, y)
probability = model.predict_proba([[5]])
print(probability)
