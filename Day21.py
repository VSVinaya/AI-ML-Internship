#Reshape Practice

print("Convert 1D → 2D")
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr.reshape(2,3))

print("Convert 1D → 3D")
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr.reshape(1,2,3))

# print("Try Invalid Reshape")
# import numpy as np
# arr = np.array([1,2,3,4,5,6])
# print(arr.reshape(4,2))
#Error : 6 elements cannot be reshaped into 8 positions.

#Flatten

print("Convert 2D → 1D")
import numpy as np
arr = np.array([
    [1,2],
    [3,4]
])
print(arr.flatten())

print("Compare Flatten vs Ravel")
import numpy as np
arr = np.array([
    [1,2],
    [3,4]
])
print(arr.flatten())
print(arr.ravel())

#Transpose

print("Transpose Matrix")
import numpy as np
arr = np.array([
    [1,2],
    [3,4]
])
print(arr.T)

print("Verify Rows and Columns")
import numpy as np
arr = np.array([
    [1,2,3],
    [4,5,6]
])
print("Original Shape:", arr.shape)
print("Transpose Shape:", arr.T.shape)

#Stacking

print("Vertical Stack")
import numpy as np
a = np.array([1,2])
b = np.array([3,4])
print(np.vstack((a,b)))

print("Horizontal Stack")
import numpy as np
a = np.array([1,2])
b = np.array([3,4])
print(np.hstack((a,b)))

print("Combine Arrays")
import numpy as np
a = np.array([10,20])
b = np.array([30,40])
combined = np.hstack((a,b))
print(combined)

#Splitting

print("Split Array")
import numpy as np
arr = np.array([1,2,3,4])
print(np.split(arr,2))

print("Split Rows")
import numpy as np
arr = np.array([
    [1,2],
    [3,4]
])
print(np.vsplit(arr,2))
