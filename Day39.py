# Dataset Creation

print("Create Student Dataset")
import pandas as pd
data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Result": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
print(df)

print("Create Height Dataset")
import pandas as pd
data = {
    "Height": [150, 155, 160, 165, 170, 175],
    "Category": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
print(df)

print("Create Temperature Dataset")
import pandas as pd
data = {
    "Temperature": [98, 99, 100, 101, 102, 103],
    "Disease": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
print(df)

# Train KNN Model

print("Train KNN Classifier")
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Result": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Result"]
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)
print("KNN Model Trained Successfully")

# Prediction Practice

print("Predict Student Result")
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Result": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Result"]
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)
prediction = model.predict([[5]])
print("Prediction:", prediction)


print("Predict Disease Status")
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
data = {
    "Temperature": [98, 99, 100, 101, 102, 103],
    "Disease": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Temperature"]]
y = df["Disease"]
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)
prediction = model.predict([[102]])
print("Disease Prediction:", prediction)


print("Predict Height Category")
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
data = {
    "Height": [150, 155, 160, 165, 170, 175],
    "Category": [0, 0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)
X = df[["Height"]]
y = df["Category"]
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)
prediction = model.predict([[168]])
print("Category Prediction:", prediction)
