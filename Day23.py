# Basic Broadcasting

print("Add Scalar to Array")
import numpy as np
arr = np.array([1,2,3,4])
print(arr + 10)

print("Multiply Array with Scalar")
import numpy as np
arr = np.array([1,2,3,4])
print(arr * 5)

print("Divide Array by Scalar")
import numpy as np
arr = np.array([10,20,30,40])
print(arr / 10)

# Array Broadcasting

print("Add Two Compatible Arrays")
import numpy as np
a = np.array([[1],[2],[3]])
b = np.array([10,20,30])
print(a + b)

print("Multiply Arrays")
import numpy as np
a = np.array([[1],[2],[3]])
b = np.array([10,20,30])
print(a * b)

print("Observe Shape Changes")
import numpy as np
a = np.array([[1],[2],[3]])
b = np.array([10,20,30])
print(a.shape)
print(b.shape)

# Shape Practice

print("Print Shapes")
import numpy as np
a = np.array([[1],[2],[3]])
b = np.array([10,20,30])
print(a.shape)
print(b.shape)

print("Check Compatible Shapes")
import numpy as np
a = np.array([[1],[2],[3]])
b = np.array([10,20,30])
print(a + b)

# print("Incompatible Shapes")
# import numpy as np
# a = np.array([1,2,3])
# b = np.array([1,2])
# print(a + b)
#Output: Error because shapes are incompatible.

# 2D Broadcasting

print("Add Scalar to Matrix")
import numpy as np
arr = np.array([
    [1,2,3],
    [4,5,6]
])
print(arr + 100)


print("Multiply Matrix")
import numpy as np
arr = np.array([
    [1,2,3],
    [4,5,6]
])
print(arr * 2)


print("Normalize Matrix Values")
import numpy as np
arr = np.array([
    [10,20,30],
    [40,50,60]
])
print(arr / 10)

