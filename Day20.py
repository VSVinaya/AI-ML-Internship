#1D Practice

print("Access First Element")
import numpy as np
arr = np.array([10,20,30,40])
print(arr[0])

print("Access Last Element")
import numpy as np
arr = np.array([10,20,30,40])
print(arr[-1])

print("Slice Array")
import numpy as np
arr = np.array([10,20,30,40])
print(arr[1:3])

#2D Practice

print("Access Element")
import numpy as np
arr = np.array([
    [1,2,3],
    [4,5,6]
])
print(arr[0,1])


print("Print Row")
import numpy as np
arr = np.array([
    [1,2,3],
    [4,5,6]
])
print(arr[0])


print("Print Column")
import numpy as np
arr = np.array([
    [1,2,3],
    [4,5,6]
])
print(arr[:,1])

#3D Practice

print("Access Layer")
import numpy as np
arr = np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
])
print(arr[0])


print("Access Row Inside Layer")
import numpy as np
arr = np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
])
print(arr[0][1])


print("Access Single Element")
import numpy as np
arr = np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
])
print(arr[1,0,2])

#Slicing

print("Extract Sub-array")
import numpy as np
arr = np.array([10,20,30,40,50])
print(arr[1:4])

print("Use Step Slicing")
import numpy as np
arr = np.array([10,20,30,40,50])
print(arr[::2])

print("Slice Rows and Columns")
import numpy as np
arr = np.array([
    [1,2,3],
    [4,5,6]
])
print(arr[:,1:3])

#Boolean Indexing

print("Filter Values Greater Than 25")
import numpy as np
arr = np.array([10,20,30,40,50])
print(arr[arr > 25])

print("Filter Values Between Range")
import numpy as np
arr = np.array([10,20,30,40,50])
print(arr[(arr > 20) & (arr < 50)])

print("Replace Values Conditionally")
import numpy as np
arr = np.array([10,20,30,40])
arr[arr > 25] = 0
print(arr)
