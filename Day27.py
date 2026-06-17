# Create CSV File

print("Read CSV Using Pandas")
import pandas as pd
df = pd.read_csv("students.csv")
print(df)

print("Print Dataset")
import pandas as pd
df = pd.read_csv("students.csv")
print(df)

# Column Selection

print("Select Single Column")
import pandas as pd
df = pd.read_csv("students.csv")
print(df["Name"])

print("Select Multiple Columns")
import pandas as pd
df = pd.read_csv("students.csv")
print(df[["Name","Marks"]])

print("Print Specific Column Values")
import pandas as pd
df = pd.read_csv("students.csv")
print(df["Marks"])

# Row Selection

print("Select Row Using loc")
import pandas as pd
df = pd.read_csv("students.csv")
print(df.loc[0])

print("Select Row Using iloc")
import pandas as pd
df = pd.read_csv("students.csv")
print(df.iloc[1])

print("Slice Rows")
import pandas as pd
df = pd.read_csv("students.csv")
print(df.iloc[0:2])

# Filtering

print("Filter Marks > 80")
import pandas as pd
df = pd.read_csv("students.csv")
print(df[df["Marks"] > 80])

print("Filter City Names")
import pandas as pd
df = pd.read_csv("students.csv")
print(df[df["City"] == "Kochi"])

print("Combine Conditions")
import pandas as pd
df = pd.read_csv("students.csv")
print(df[(df["Marks"] > 80) & (df["City"] == "Kochi")])

