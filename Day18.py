#Array Creation

print("Create 1D Array")
import numpy as np
arr = np.array([1,2,3,4])
print(arr)

print("Create 2D Array")
import numpy as np
arr2 = np.array([[1,2],[3,4]])
print(arr2)

print("Create 3D Array")
import numpy as np
arr3 = np.array([[[1,2],[3,4]]])
print(arr3)

print("Print All")
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([[1,2],[3,4]])
arr3 = np.array([[[1,2],[3,4]]])
print(arr1)
print(arr2)
print(arr3)

#Properties
print("Print Shape")
import numpy as np
arr = np.array([[1,2],[3,4]])
print(arr.shape)

print("Print Dimensions")
import numpy as np
arr = np.array([[1,2],[3,4]])
print(arr.ndim)

print("Print Data Type")
import numpy as np
arr = np.array([1,2,3])
print(arr.dtype)

#Special Arrays

print("Create Zero Matrix")
import numpy as np
print(np.zeros((2,3)))

print("Create Ones Matrix")
import numpy as np
print(np.ones((2,2)))

print("Create Identity Matrix")
import numpy as np
print(np.eye(3))

print("Create Range Array")
import numpy as np
print(np.arange(1,10))

#Indexing

print("Access First Element")
import numpy as np
arr = np.array([10,20,30,40])
print(arr[0])

print("Slice Array")
import numpy as np
arr = np.array([10,20,30,40])
print(arr[1:3])

print("Access Element in 2D")
import numpy as np
arr = np.array([[1,2],[3,4]])
print(arr2[0,1])

#Reshaping

print("Convert 1D → 2D")
import numpy as np
arr = np.array([1,2,3,4,5,6])
reshaped = arr.reshape(2,3)
print(reshaped)

print("Convert 2D → 1D")
import numpy as np
arr = np.array([[1,2],[3,4]])
flat = arr.reshape(4)
print(flat)