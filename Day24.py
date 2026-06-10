# Random Integer Practice

print("Generate Random Integer")
import numpy as np
print(np.random.randint(1,10))

print("Generate Array of Integers")
import numpy as np
print(np.random.randint(1,100,size=5))

print("Create Random Matrix")
import numpy as np
print(np.random.randint(1,50,size=(3,3)))

# Random Decimal Practice

print("Generate Decimal Values")
import numpy as np
print(np.random.rand(5))

print("Create 2D Decimal Matrix")
import numpy as np
print(np.random.rand(2,3))

# Random Choice

print("Pick Random Color")
import numpy as np
colors = ["Red","Blue","Green"]
print(np.random.choice(colors))

print("Generate Multiple Choices")
import numpy as np
colors = ["Red","Blue","Green"]
print(np.random.choice(colors,size=5))

print("Simulate Random Names")
import numpy as np
names = ["John","Sara","Alex","David"]
print(np.random.choice(names,size=3))

# Shuffle

print("Shuffle Array")
import numpy as np
arr = np.array([1,2,3,4,5])
np.random.shuffle(arr)
print(arr)

print("Shuffle Student IDs")
import numpy as np
ids = np.array([101,102,103,104,105])
np.random.shuffle(ids)
print(ids)

# Dataset Simulation

print("Create Marks Dataset")
import numpy as np
marks = np.random.randint(40,100,size=(5,3))
print(marks)

print("Create Attendance Dataset")
import numpy as np
attendance = np.random.randint(60,101,size=(5,3))
print(attendance)

print("Create Random Image Matrix")
import numpy as np
image = np.random.randint(0,256,size=(3,3))
print(image)
