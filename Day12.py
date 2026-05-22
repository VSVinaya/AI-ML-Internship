#List Comprehension

print("Square numbers")
nums = [1,2,3,4]
squares = [x*x for x in nums]
print(squares)

print("Even numbers")
nums = [1,2,3,4,5,6]
even = [x for x in nums if x % 2 == 0]
print(even)

print("Strings to uppercase")
names = ["ai","ml","python"]
upper = [n.upper() for n in names]
print(upper)

print("Filter numbers greater than 50")
nums = [20,55,70,30,90]
result = [x for x in nums if x > 50]
print(result)

#Dictionary Comprehension

print("Square dictionary")
nums = [1,2,3,4]
squares = {x:x*x for x in nums}
print(squares)

print("Filter even numbers")
nums = [1,2,3,4,5,6]
even_dict = {x:x*x for x in nums if x % 2 == 0}
print(even_dict)

print("Map names to lengths")
names = ["AI","Python","Machine"]
result = {n:len(n) for n in names}
print(result)

#Set Practice

print("Remove duplicates")
nums = [1,2,2,3,4,4]
unique = set(nums)
print(unique)

print("Common elements")
a = {1,2,3}
b = {2,3,4}
print(a & b)

print("Union and difference")
a = {1,2,3}
b = {3,4,5}
print(a | b)
print(a - b)

#Generator Practice

print("Generator for numbers")
def numbers(n):
    for i in range(n):
        yield i
for x in numbers(5):
    print(x)

print("Generate even numbers")
def even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
for x in even(10):
    print(x)

print("Fibonacci using generator")
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b
for x in fibonacci(6):
    print(x)

# Zip & Enumerate

print("Combine two lists")
names = ["A","B"]
marks = [80,90]
combined = list(zip(names, marks))
print(combined)

print("Print index and value")
names = ["AI","ML","Python"]
for i, n in enumerate(names):
    print(i, n)

print("Zip result to dictionary")
names = ["A","B"]
marks = [80,90]
result = dict(zip(names, marks))
print(result)
