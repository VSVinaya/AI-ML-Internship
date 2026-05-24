#Debugging Practice

print("Fix Syntax Error")
#Wrong Code : print("Hello
# Correct Code : 
print("Hello")

print("Fix Value Error")
#Wrong Code : x = int("abc")
#Correct Code : 
x = int("10")
print(x)

print("Fix Index Error")
#Wrong Code : nums = [1,2,3]
#print(nums[5])
#Correct Code : 
nums = [1,2,3]
print(nums[2])

#Optimization Practice

#Replace Loops with Built-in Functions
#Before
nums = [1,2,3]
total = 0
for i in nums:
    total += i
print(total)
#Optimized
nums = [1,2,3]
print(sum(nums))

#Optimize Sorting
#Before
numbers = [5,2,8,1]
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print(numbers)
#Optimized
numbers = [5,2,8,1]
numbers.sort()
print(numbers)

#Reduce Repeated Code
#Before
nums1 = [1,2,3]
total1 = sum(nums1)
print(total1)
nums2 = [4,5,6]
total2 = sum(nums2)
print(total2)
#Optimized
def calculate_sum(numbers):
    return sum(numbers)
print(calculate_sum([1,2,3]))
print(calculate_sum([4,5,6]))

#Refactoring

#Convert Long Code → Functions
#Before
marks = [80,90,70]
total = sum(marks)
average = total / len(marks)
print(average)
#After Refactoring
def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average
marks = [80,90,70]
print(calculate_average(marks))

#Convert Repeated Logic → Reusable Function
#Before
a = 10
b = 20
print(a+b)
x = 5
y = 15
print(x+y)
#After Refactoring
def add_numbers(a, b):
    return a + b
print(add_numbers(10,20))
print(add_numbers(5,15))
