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


print("Spam Detection Dataset")
import pandas as pd
data = {
    "MessageLength": [10, 20, 30, 40, 50],
    "Spam": [0, 0, 0, 1, 1]
}
df = pd.DataFrame(data)
print(df)

# Model Building

print("Create SVM Model,Train the Model,Make Predictions")
import pandas as pd
from sklearn.svm import SVC
data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Result"]
model = SVC()
model.fit(X, y)
prediction = model.predict([[4]])
print("Prediction:", prediction)

# Prediction Practice

print("Predict Student Result")
import pandas as pd
from sklearn.svm import SVC
data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Result"]
model = SVC()
model.fit(X, y)
prediction = model.predict([[5]])
print("Student Result:", prediction)


print("Predict Disease Status")
import pandas as pd
from sklearn.svm import SVC
data = {
    "Temperature": [98, 99, 100, 101, 102],
    "Disease": [0, 0, 0, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Temperature"]]
y = df["Disease"]
model = SVC()
model.fit(X, y)
prediction = model.predict([[101]])
print("Disease Status:", prediction)



print("Predict Spam Detection")
import pandas as pd
from sklearn.svm import SVC
data = {
    "MessageLength": [10, 20, 30, 40, 50],
    "Spam": [0, 0, 0, 1, 1]
}
df = pd.DataFrame(data)
X = df[["MessageLength"]]
y = df["Spam"]
model = SVC()
model.fit(X, y)
prediction = model.predict([[45]])
print("Spam Prediction:", prediction)