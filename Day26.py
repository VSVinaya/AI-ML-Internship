# Series Practice

print("Create Series")
import pandas as pd
data = pd.Series([10,20,30,40])
print(data)


print("Create Series with Custom Index")
import pandas as pd
marks = pd.Series(
    [85,90,78],
    index=["Math","Science","English"]
)
print(marks)


print("Access Series Values")
import pandas as pd
marks = pd.Series(
    [85,90,78],
    index=["Math","Science","English"]
)
print(marks["Math"])

# DataFrame Practice

print("Create DataFrame Using Dictionary")
import pandas as pd
data = {
    "Name":["Rahul","Anu","Arjun"],
    "Marks":[85,90,78]
}
df = pd.DataFrame(data)
print(df)


print("Print DataFrame")
import pandas as pd
data = {
    "Name":["Rahul","Anu","Arjun"],
    "Marks":[85,90,78]
}
df = pd.DataFrame(data)
print(df)


print("Add One More Column")
import pandas as pd
data = {
    "Name":["Rahul","Anu","Arjun"],
    "Marks":[85,90,78]
}
df = pd.DataFrame(data)
df["Grade"] = ["A","A+","B"]
print(df)

# Data Access

print("Access Single Column")
import pandas as pd
data = {
    "Name":["Rahul","Anu","Arjun"],
    "Marks":[85,90,78]
}
df = pd.DataFrame(data)
print(df["Name"])


print("Access Multiple Columns")
import pandas as pd
data = {
    "Name":["Rahul","Anu","Arjun"],
    "Marks":[85,90,78]
}
df = pd.DataFrame(data)
print(df[["Name","Marks"]])


print("Print Specific Rows")
import pandas as pd
data = {
    "Name":["Rahul","Anu","Arjun"],
    "Marks":[85,90,78]
}
df = pd.DataFrame(data)
print(df.iloc[0])

# Data Information

print("Use head()")
import pandas as pd
data = {
    "Name":["Rahul","Anu","Arjun"],
    "Marks":[85,90,78]
}
df = pd.DataFrame(data)
print(df.head())


print("Use tail()")
import pandas as pd
data = {
    "Name":["Rahul","Anu","Arjun"],
    "Marks":[85,90,78]
}
df = pd.DataFrame(data)
print(df.tail())


print("Use info()")
import pandas as pd
data = {
    "Name":["Rahul","Anu","Arjun"],
    "Marks":[85,90,78]
}
df = pd.DataFrame(data)
print(df.info())
