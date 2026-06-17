# Missing Data Practice

print("Create Dataset With Missing Values")
import pandas as pd
import numpy as np
data = {
    "Name": ["Rahul", "Anu", "Arjun", None],
    "Marks": [85, np.nan, 78, 90],
    "City": ["Kochi", "Trivandrum", None, "Kollam"]
}
df = pd.DataFrame(data)
print(df)


print("Detect Missing Values")
import pandas as pd
import numpy as np
data = {
    "Name": ["Rahul", "Anu", "Arjun", None],
    "Marks": [85, np.nan, 78, 90],
    "City": ["Kochi", "Trivandrum", None, "Kollam"]
}
df = pd.DataFrame(data)
print(df.isnull())


print("Count Missing Values")
import pandas as pd
import numpy as np
data = {
    "Name": ["Rahul", "Anu", "Arjun", None],
    "Marks": [85, np.nan, 78, 90],
    "City": ["Kochi", "Trivandrum", None, "Kollam"]
}
df = pd.DataFrame(data)
print(df.isnull().sum())

# Removing Missing Data

print("Drop Rows with Missing Values")
import pandas as pd
import numpy as np
data = {
    "Name": ["Rahul", "Anu", "Arjun", None],
    "Marks": [85, np.nan, 78, 90],
    "City": ["Kochi", "Trivandrum", None, "Kollam"]
}
df = pd.DataFrame(data)
print(df.dropna())


print("Drop Columns with Missing Values")
import pandas as pd
import numpy as np
data = {
    "Name": ["Rahul", "Anu", "Arjun", None],
    "Marks": [85, np.nan, 78, 90],
    "City": ["Kochi", "Trivandrum", None, "Kollam"]
}
df = pd.DataFrame(data)
print(df.dropna(axis=1))

# Fill Missing Data

print("Fill Missing Values with Text")
import pandas as pd
import numpy as np

data = {
    "Name": ["Rahul", "Anu", None],
    "Marks": [85, np.nan, 78]
}
df = pd.DataFrame(data)
print(df.fillna("Unknown"))


print("Fill Missing Marks with Mean Value")
import pandas as pd
import numpy as np
data = {
    "Name": ["Rahul", "Anu", "Arjun"],
    "Marks": [85, np.nan, 78]
}
df = pd.DataFrame(data)
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print(df)


print("Fill Numeric Columns")
import pandas as pd
import numpy as np
data = {
    "Marks": [85, np.nan, 78],
    "Age": [20, np.nan, 22]
}
df = pd.DataFrame(data)
df = df.fillna(df.mean())
print(df)

# Duplicate Handling

print("Create Duplicate Rows")
import pandas as pd
data = {
    "Name": ["Rahul", "Anu", "Rahul"],
    "Marks": [85, 90, 85]
}
df = pd.DataFrame(data)
print(df)


print("Detect Duplicates")
import pandas as pd
data = {
    "Name": ["Rahul", "Anu", "Rahul"],
    "Marks": [85, 90, 85]
}
df = pd.DataFrame(data)
print(df.duplicated())


print("Remove Duplicates")
import pandas as pd
data = {
    "Name": ["Rahul", "Anu", "Rahul"],
    "Marks": [85, 90, 85]
}
df = pd.DataFrame(data)
print(df.drop_duplicates())

# Column Operations

print("Rename Columns")
import pandas as pd
data = {
    "Name": ["Rahul", "Anu"],
    "Marks": [85, 90]
}
df = pd.DataFrame(data)
df.rename(columns={"Marks": "Score"}, inplace=True)
print(df)


print("Change Data Type")
import pandas as pd
data = {
    "Score": [85.5, 90.2]
}
df = pd.DataFrame(data)
df["Score"] = df["Score"].astype(int)
print(df)


print("Print Data Types")
import pandas as pd
data = {
    "Name": ["Rahul", "Anu"],
    "Score": [85, 90]
}
df = pd.DataFrame(data)
print(df.dtypes)
