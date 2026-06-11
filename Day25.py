# Marks Analysis

print("Find Average Marks")
import numpy as np
marks = np.array([
    [85,78,90],
    [70,88,60],
    [95,92,89]
])
print("Average Marks:", np.mean(marks))


print("Find Highest Marks")
import numpy as np
marks = np.array([
    [85,78,90],
    [70,88,60],
    [95,92,89]
])
print("Highest Marks:", np.max(marks))


print("Find Lowest Marks")
import numpy as np
marks = np.array([
    [85,78,90],
    [70,88,60],
    [95,92,89]
])
print("Lowest Marks:", np.min(marks))


print("Find Topper")
import numpy as np
marks = np.array([
    [85,78,90],
    [70,88,60],
    [95,92,89]
])
total = np.sum(marks, axis=1)
topper = np.argmax(total)
print("Top Student Index:", topper)

# Image Operations

print("Increase Brightness")
import numpy as np
image = np.array([
    [50,100],
    [150,200]
])
bright = image + 50
print(bright)


print("Decrease Brightness")
import numpy as np
image = np.array([
    [50,100],
    [150,200]
])
dark = image - 30
print(dark)


print("Normalize Image Pixels")
import numpy as np
image = np.array([
    [50,100],
    [150,200]
])
normalized = image / np.max(image)
print(normalized)

# Dataset Filtering

print("Filter Values Greater Than 50")
import numpy as np
arr = np.array([10,25,30,5,60,80])
print(arr[arr > 50])

print("Replace Low Values")
import numpy as np
arr = np.array([10,25,30,5,60,80])
arr[arr < 20] = 0
print(arr)

print("Count Filtered Values")
import numpy as np
arr = np.array([10,25,30,5,60,80])
filtered = arr[arr > 20]
print(len(filtered))

# Reshaping

print("Convert 1D → 2D")
import numpy as np
arr = np.arange(12)
print(arr.reshape(3,4))

print("Convert 2D → 1D")
import numpy as np
arr = np.array([
    [1,2,3],
    [4,5,6]
])
print(arr.flatten())


print("Create 3D Dataset")
import numpy as np
arr = np.arange(24)
print(arr.reshape(2,3,4))


# Dataset Simulation

print("Attendance Matrix")
import numpy as np
attendance = np.random.randint(0,2,size=(5,7))
print(attendance)

print("Marks Dataset")
import numpy as np
marks = np.random.randint(40,101,size=(5,3))
print(marks)

print("Weather Dataset")
import numpy as np
weather = np.random.randint(20,40,size=(7,))
print(weather)
