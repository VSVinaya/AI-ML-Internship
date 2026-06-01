#Math Practice

print("Find Square Root")
import math
print(math.sqrt(25))

print("Find Power")
import math
print(math.pow(2,4))

print("Round Numbers")
import math
print(math.ceil(2.3))
print(math.floor(2.9))

print("Use π Value")
import math
print(math.pi)

#Random Practice

print("Generate Random Number")
import random
print(random.randint(1,10))

print("Pick Random Element")
import random
numbers = [10,20,30,40]
print(random.choice(numbers))

print("Generate List of Random Numbers")
import random
nums = []
for i in range(5):
    nums.append(random.randint(1,100))
print(nums)

#Datetime Practice

print("Print Current Date")
import datetime
today = datetime.datetime.now()
print(today)

print("Format Date")
import datetime
today = datetime.datetime.now()
print(today.strftime("%Y-%m-%d"))

print("Extract Year and Month")
import datetime
today = datetime.datetime.now()
print(today.year)
print(today.month)

#Visualization

print("Create Line Graph")
import matplotlib.pyplot as plt
x = [1,2,3]
y = [10,20,30]
plt.plot(x,y)
plt.show()

print("Create Bar Chart")
import matplotlib.pyplot as plt
x = [1,2,3]
y = [10,20,30]
plt.bar(x,y)
plt.show()

print("Plot Student Marks")
import matplotlib.pyplot as plt
students = ["A","B","C"]
marks = [80,90,70]
plt.bar(students, marks)
plt.show()
