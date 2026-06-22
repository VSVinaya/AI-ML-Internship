# Line Plot Practice

print("Create Line Graph")
import seaborn as sns
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
sns.lineplot(x=x, y=y)
plt.show()

print("Add Style")
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("darkgrid")
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
sns.lineplot(x=x, y=y)
plt.show()

print("Compare Data Trends")
import seaborn as sns
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
sales = [100, 150, 200, 250]
profit = [20, 40, 60, 80]
sns.lineplot(x=x, y=sales, label="Sales")
sns.lineplot(x=x, y=profit, label="Profit")
plt.show()

# Bar Plot Practice

print("Student Marks Comparison")
import seaborn as sns
import matplotlib.pyplot as plt
students = ["Rahul", "Anu", "Arjun"]
marks = [85, 90, 78]
sns.barplot(x=students, y=marks)
plt.show()

print("Sales Comparison")
import seaborn as sns
import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar"]
sales = [15000, 22000, 18000]
sns.barplot(x=months, y=sales)
plt.show()

print("Employee Salary Comparison")
import seaborn as sns
import matplotlib.pyplot as plt
employees = ["A", "B", "C"]
salary = [40000, 55000, 50000]
sns.barplot(x=employees, y=salary)
plt.show()

# Scatter Plot Practice

print("Height vs Weight")
import seaborn as sns
import matplotlib.pyplot as plt
height = [150, 160, 170, 180]
weight = [50, 60, 70, 80]
sns.scatterplot(x=height, y=weight)
plt.show()

print("Study Hours vs Marks")
import seaborn as sns
import matplotlib.pyplot as plt
hours = [1, 2, 3, 4, 5]
marks = [40, 55, 70, 85, 95]
sns.scatterplot(x=hours, y=marks)
plt.show()

print("Temperature vs Sales")
import seaborn as sns
import matplotlib.pyplot as plt
temperature = [20, 25, 30, 35]
sales = [100, 150, 220, 300]
sns.scatterplot(x=temperature, y=sales)
plt.show()

# Histogram Practice

print("Create Histogram")
import seaborn as sns
import matplotlib.pyplot as plt
data = [10, 20, 20, 30, 40, 40, 50]
sns.histplot(data)
plt.show()

print("Analyze Frequency")
import seaborn as sns
import matplotlib.pyplot as plt
marks = [60, 65, 70, 75, 80, 85, 90, 95]
sns.histplot(marks)
plt.show()

print("Use Random Dataset")
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(100)
sns.histplot(data)
plt.show()

# Box Plot Practice

print("Detect Outliers")
import seaborn as sns
import matplotlib.pyplot as plt
data = [10, 20, 30, 40, 100]
sns.boxplot(x=data)
plt.show()

print("Analyze Salary Dataset")
import seaborn as sns
import matplotlib.pyplot as plt
salary = [30000, 35000, 40000, 45000, 90000]
sns.boxplot(x=salary)
plt.show()

print("Analyze Marks Dataset")
import seaborn as sns
import matplotlib.pyplot as plt
marks = [55, 60, 70, 80, 95]
sns.boxplot(x=marks)
plt.show()

# Count Plot Practice

print("Course Count")
import seaborn as sns
import matplotlib.pyplot as plt
courses = ["AI", "Web", "AI", "Cloud", "AI"]
sns.countplot(x=courses)
plt.show()

print("Department Count")
import seaborn as sns
import matplotlib.pyplot as plt
departments = ["HR", "IT", "IT", "Finance", "HR"]
sns.countplot(x=departments)
plt.show()

print("Product Category Count")
import seaborn as sns
import matplotlib.pyplot as plt
categories = ["Electronics", "Food", "Food", "Electronics", "Clothes"]
sns.countplot(x=categories)
plt.show()
