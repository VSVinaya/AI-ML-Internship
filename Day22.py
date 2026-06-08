#Basic Aggregation

print("Find Sum")
import numpy as np
arr = np.array([10,20,30,40])
print(np.sum(arr))

print("Find Mean")
import numpy as np
arr = np.array([10,20,30,40])
print(np.mean(arr))

print("Find Max and Min")
import numpy as np
arr = np.array([10,20,30,40])
print(np.max(arr))
print(np.min(arr))

#Statistical Functions

print("Find Median")
import numpy as np
arr = np.array([10,20,30,40])
print(np.median(arr))

print("Find Standard Deviation")
import numpy as np
arr = np.array([10,20,30,40])
print(np.std(arr))

print("Find Variance")
import numpy as np
arr = np.array([10,20,30,40])
print(np.var(arr))

#Axis Practice

print("Row-wise Sum")
import numpy as np
arr = np.array([
    [1,2,3],
    [4,5,6]
])
print(np.sum(arr, axis=1))

print("Column-wise Sum")
import numpy as np
arr = np.array([
    [1,2,3],
    [4,5,6]
])
print(np.sum(arr, axis=0))

print("Mean Using Axis")
import numpy as np
arr = np.array([
    [1,2,3],
    [4,5,6]
])
print(np.mean(arr, axis=0))
print(np.mean(arr, axis=1))

#Index Functions

print("Find Index of Maximum Value")
import numpy as np
arr = np.array([10,50,20,40])
print(np.argmax(arr))

print("Find Index of Minimum Value")
import numpy as np
arr = np.array([10,50,20,40])
print(np.argmin(arr))

#Cumulative Operations
print("Compute Cumulative Sum")
import numpy as np
arr = np.array([1,2,3,4])
print(np.cumsum(arr))
