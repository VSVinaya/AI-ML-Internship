# Sorting Practice

print("Sort Salary in Ascending Order")
import pandas as pd
data = {
    "Name": ["Rahul", "Anu", "Arjun", "Meera"],
    "Department": ["AI", "Web", "AI", "Web"],
    "Salary": [50000, 40000, 60000, 45000]
}
df = pd.DataFrame(data)
print(df.sort_values("Salary"))


print("Sort Salary in Descending Order")
import pandas as pd
data = {
    "Name": ["Rahul", "Anu", "Arjun", "Meera"],
    "Department": ["AI", "Web", "AI", "Web"],
    "Salary": [50000, 40000, 60000, 45000]
}
df = pd.DataFrame(data)
print(df.sort_values("Salary", ascending=False))


print("Sort by Department and Salary")
import pandas as pd
data = {
    "Name": ["Rahul", "Anu", "Arjun", "Meera"],
    "Department": ["AI", "Web", "AI", "Web"],
    "Salary": [50000, 40000, 60000, 45000]
}
df = pd.DataFrame(data)
print(df.sort_values(["Department", "Salary"]))

# Grouping Practice

print("Group Employees by Department")
import pandas as pd
data = {
    "Name": ["Rahul", "Anu", "Arjun", "Meera"],
    "Department": ["AI", "Web", "AI", "Web"]
}
df = pd.DataFrame(data)
print(df.groupby("Department").size())


print("Group Students by City")
import pandas as pd
data = {
    "Name": ["Rahul", "Anu", "Arjun"],
    "City": ["Kochi", "Kochi", "Kollam"]
}
df = pd.DataFrame(data)
print(df.groupby("City").size())


print("Group Products by Category")
import pandas as pd
data = {
    "Product": ["Laptop", "Rice", "Mobile"],
    "Category": ["Electronics", "Food", "Electronics"]
}
df = pd.DataFrame(data)
print(df.groupby("Category").size())

# Aggregation Practice

print("Find Average Salary")
import pandas as pd
data = {
    "Department": ["AI", "Web", "AI", "Web"],
    "Salary": [50000, 40000, 60000, 45000]
}
df = pd.DataFrame(data)
print(df.groupby("Department")["Salary"].mean())


print("Find Total Salary")
import pandas as pd
data = {
    "Department": ["AI", "Web", "AI", "Web"],
    "Salary": [50000, 40000, 60000, 45000]
}
df = pd.DataFrame(data)
print(df.groupby("Department")["Salary"].sum())


print("Count Employees")
import pandas as pd
data = {
    "Name": ["Rahul", "Anu", "Arjun", "Meera"],
    "Department": ["AI", "Web", "AI", "Web"]
}
df = pd.DataFrame(data)
print(df.groupby("Department")["Name"].count())

# Multiple Aggregation

print("Find Mean, Maximum and Minimum Salary")
import pandas as pd
data = {
    "Department": ["AI", "Web", "AI", "Web"],
    "Salary": [50000, 40000, 60000, 45000]
}
df = pd.DataFrame(data)
print(df.groupby("Department")["Salary"].agg(["mean", "max", "min"]))

# Value Counts

print("Count Departments")
import pandas as pd
data = {
    "Department": ["AI", "Web", "AI", "Web"]
}
df = pd.DataFrame(data)
print(df["Department"].value_counts())


print("Count Repeated Values")
import pandas as pd
data = {
    "Department": ["AI", "Web", "AI", "Web", "AI"]
}
df = pd.DataFrame(data)
print(df["Department"].value_counts())


print("Analyze Category Frequency")
import pandas as pd
data = {
    "Category": ["A", "B", "A", "C", "A", "B"]
}
df = pd.DataFrame(data)
print(df["Category"].value_counts())

