#Arithmetic Practice

print("Add Two Arrays")
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a + b)

print("Multiply Arrays")
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a * b)

print("Divide Arrays")
import numpy as np
a = np.array([10,20,30])
b = np.array([2,4,5])
print(a / b)

#Scalar Operations

print("Add Constant to Array")
import numpy as np
arr = np.array([1,2,3])
print(arr + 10)

print("Multiply Array")
import numpy as np
arr = np.array([1,2,3])
print(arr * 5)

print("Subtract Constant")
import numpy as np
arr = np.array([10,20,30])
print(arr - 5)

#Math Functions

print("Find Square Root")
import numpy as np
arr = np.array([4,9,16])
print(np.sqrt(arr))

print("Find Log Values")
import numpy as np
arr = np.array([1,2,3])
print(np.log(arr))

print("Round Values")
import numpy as np
arr = np.array([1.2,2.7,3.5])
print(np.round(arr))

#Aggregation

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

#Axis Practice

print("Row-wise Sum")
import numpy as np
a = np.array([[1,2], [3,4]])
print(np.sum(a, axis=1))

print("Column-wise Sum")
import numpy as np
a = np.array([[1,2], [3,4]])
print(np.sum(a, axis=0))

#Filtering

print("Filter Values Greater Than 20")
import numpy as np
arr = np.array([10,20,30,40])
print(arr[arr > 20])

print("Filter Even Numbers")
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr[arr % 2 == 0])
