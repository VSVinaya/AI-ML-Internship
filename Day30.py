# Line Plot Practice
print("Create Simple Line Graph")
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
plt.plot(x, y)
plt.show()

print("Add Labels")
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
plt.plot(x, y)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

print("Add Title")
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
plt.plot(x, y)
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Styling Graphs

print("Add Marker")
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
plt.plot(x, y, marker="o")
plt.show()

print("Change Line Style")
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
plt.plot(x, y, linestyle="--")
plt.show()

print("Add Grid")
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
plt.plot(x, y)
plt.grid()
plt.show()

# Bar Chart Practice

print("Student Marks Comparison")
import matplotlib.pyplot as plt
students = ["Rahul", "Anu", "Arjun"]
marks = [85, 90, 78]
plt.bar(students, marks)
plt.title("Student Marks Comparison")
plt.show()

print("Sales Comparison")
import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar"]
sales = [15000, 22000, 18000]
plt.bar(months, sales)
plt.title("Monthly Sales")
plt.show()

print("Product Comparison")
import matplotlib.pyplot as plt
products = ["Laptop", "Mobile", "Tablet"]
sales = [50, 80, 30]
plt.bar(products, sales)
plt.title("Product Sales Comparison")
plt.show()

# Pie Chart Practice

print("Department Distribution")
import matplotlib.pyplot as plt
data = [40, 30, 20, 10]
labels = ["AI", "Web", "Cloud", "Cyber"]
plt.pie(data, labels=labels)
plt.title("Department Distribution")
plt.show()

print("Expense Analysis")
import matplotlib.pyplot as plt
expenses = [5000, 3000, 2000]
labels = ["Food", "Travel", "Shopping"]
plt.pie(expenses, labels=labels)
plt.title("Expense Analysis")
plt.show()

print("Course Popularity")
import matplotlib.pyplot as plt
students = [50, 35, 25]
courses = ["Python", "Java", "Data Science"]
plt.pie(students, labels=courses)
plt.title("Course Popularity")
plt.show()

# Scatter Plot Practice

print("Height vs Weight")
import matplotlib.pyplot as plt
height = [150, 160, 170, 180]
weight = [50, 60, 70, 80]
plt.scatter(height, weight)
plt.title("Height vs Weight")
plt.show()

print("Study Hours vs Marks")
import matplotlib.pyplot as plt
hours = [1, 2, 3, 4, 5]
marks = [40, 50, 65, 75, 90]
plt.scatter(hours, marks)
plt.title("Study Hours vs Marks")
plt.show()

print("Temperature vs Sales")
import matplotlib.pyplot as plt
temperature = [20, 25, 30, 35]
sales = [100, 150, 220, 300]
plt.scatter(temperature, sales)
plt.title("Temperature vs Sales")
plt.show()
