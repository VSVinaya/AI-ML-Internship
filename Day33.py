# Correlation Practice

print("Create Dataset")
import pandas as pd
data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 70, 80],
    "SleepHours": [8, 7, 6, 5, 4]
}
df = pd.DataFrame(data)
print(df)


print("Find Correlation Matrix")
import pandas as pd
data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 70, 80],
    "SleepHours": [8, 7, 6, 5, 4]
}
df = pd.DataFrame(data)
print(df.corr())

# Analysis:
# •	StudyHours and Marks show a strong positive correlation. 
# •	StudyHours and SleepHours show a negative correlation. 
# •	Marks and SleepHours also show a negative correlation. 

# Heatmap Practice

print("Create Heatmap")
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 70, 80],
    "SleepHours": [8, 7, 6, 5, 4]
}
df = pd.DataFrame(data)
sns.heatmap(df.corr())
plt.show()


print("Show Annotations")
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 70, 80],
    "SleepHours": [8, 7, 6, 5, 4]
}
df = pd.DataFrame(data)
sns.heatmap(df.corr(), annot=True)
plt.show()

# Pairplot Practice

print("Create Pairplot")
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 70, 80],
    "SleepHours": [8, 7, 6, 5, 4]
}
df = pd.DataFrame(data)
sns.pairplot(df)
plt.show()

# Scatter Plot Practice

print("Study Hours vs Marks")
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 70, 80]
}
df = pd.DataFrame(data)
sns.scatterplot(x="StudyHours", y="Marks", data=df)
plt.show()


print("Salary vs Experience")
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [25000, 30000, 40000, 50000, 60000]
}
df = pd.DataFrame(data)
sns.scatterplot(x="Experience", y="Salary", data=df)
plt.show()


print("Temperature vs Sales")
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "Temperature": [20, 25, 30, 35, 40],
    "Sales": [100, 150, 220, 300, 400]
}
df = pd.DataFrame(data)
sns.scatterplot(x="Temperature", y="Sales", data=df)
plt.show()

# Dataset Analysis

print("Student Dataset")
import pandas as pd
data = {
    "StudyHours": [2, 4, 6, 8],
    "Marks": [50, 65, 80, 95]
}
df = pd.DataFrame(data)
print(df.corr())
#Analysis: More study hours generally lead to higher marks.


print("Employee Dataset")
import pandas as pd
data = {
    "Experience": [1, 3, 5, 7],
    "Salary": [25000, 40000, 55000, 70000]
}
df = pd.DataFrame(data)
print(df.corr())
#Analysis: Salary increases as experience increases.


print("Hospital Dataset")
import pandas as pd
data = {
    "Age": [20, 30, 40, 50],
    "BP": [110, 120, 130, 140]
}
df = pd.DataFrame(data)
print(df.corr())
#Analysis: Blood pressure tends to increase with age.
