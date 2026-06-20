# Multiple Plot Practice

print("Plot Two Lines")
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [15, 25, 35, 45]
plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")
plt.legend()
plt.show()

print("Compare Student Marks")
import matplotlib.pyplot as plt
subjects = ["Math", "Science", "English"]
rahul = [80, 90, 85]
anu = [85, 95, 88]
plt.plot(subjects, rahul, label="Rahul")
plt.plot(subjects, anu, label="Anu")
plt.legend()
plt.show()

print("Compare Sales")
import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar"]
sales1 = [100, 150, 200]
sales2 = [120, 170, 220]
plt.plot(months, sales1, label="Store A")
plt.plot(months, sales2, label="Store B")
plt.legend()
plt.show()

# Legends and Titles

print("Add Legend")
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [10, 20, 30]
plt.plot(x, y, label="Data")
plt.legend()
plt.show()

print("Add Main Title")
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [10, 20, 30]
plt.plot(x, y)
plt.title("Student Performance")
plt.show()

print("Customize Labels")
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [10, 20, 30]
plt.plot(x, y)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Subplot Practice

print("Create 2 Subplots")
import matplotlib.pyplot as plt
plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [10, 20, 30])
plt.subplot(1, 2, 2)
plt.plot([1, 2, 3], [30, 20, 10])
plt.show()

print("Create 4 Subplots")
import matplotlib.pyplot as plt
plt.subplot(2, 2, 1)
plt.plot([1, 2, 3], [10, 20, 30])
plt.subplot(2, 2, 2)
plt.plot([1, 2, 3], [30, 20, 10])
plt.subplot(2, 2, 3)
plt.plot([1, 2, 3], [5, 15, 25])
plt.subplot(2, 2, 4)
plt.plot([1, 2, 3], [25, 15, 5])
plt.show()

print("Compare Graphs")
import matplotlib.pyplot as plt
plt.subplot(1, 2, 1)
plt.bar(["A", "B", "C"], [10, 20, 15])
plt.title("Bar Chart")
plt.subplot(1, 2, 2)
plt.plot([1, 2, 3], [10, 20, 15])
plt.title("Line Chart")
plt.show()

# Histogram Practice

print("Create Histogram")
import matplotlib.pyplot as plt
marks = [60, 70, 80, 85, 90, 95, 75, 65]
plt.hist(marks)
plt.title("Student Marks Distribution")
plt.show()

print("Analyze Distribution")
import matplotlib.pyplot as plt
ages = [18, 19, 20, 21, 22, 22, 23, 24, 20, 21]
plt.hist(ages)
plt.title("Age Distribution")
plt.show()

print("Use Random Dataset")
import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(100)
plt.hist(data)
plt.title("Random Data Distribution")
plt.show()

# Save Graphs

print("Save Line Graph")
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [10, 20, 30])
plt.savefig("line_graph.png")
plt.show()

print("Save Histogram")
import matplotlib.pyplot as plt
plt.hist([10, 20, 30, 40, 50])
plt.savefig("histogram.png")
plt.show()

print("Save Subplot Figure")
import matplotlib.pyplot as plt
plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [10, 20, 30])
plt.subplot(1, 2, 2)
plt.plot([1, 2, 3], [30, 20, 10])
plt.savefig("subplot.png")
plt.show()
