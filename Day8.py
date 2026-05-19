print("Function to find factorial")
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
factorial(5)


print("Function to check prime number")
def prime(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("Prime Number")
    else:
        print("Not Prime Number")

prime(7)


print("Function to reverse string")
def reverse(text):
    print(text[::-1])
reverse("python")


print("Function to calculate average")
def average(a,b,c):
    avg = (a+b+c)/3
    print(avg)
average(10,20,30)


print("Factorial using recursion")
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))


print("Sum of numbers using recursion")
def total(n):
    if n == 1:
        return 1
    return n + total(n-1)
print(total(5))


print("Fibonacci series")
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
for i in range(6):
    print(fibonacci(i))


print("Square all numbers")
nums = [1,2,3,4]
result = list(map(lambda x:x*x, nums))
print(result)


print("Double all values")
nums = [1,2,3]
result = list(map(lambda x:x*2, nums))
print(result)


print("Convert list to uppercase")
words = ["ai","ml","python"]
result = list(map(lambda x:x.upper(), words))
print(result)


print("Find even numbers")
nums = [1,2,3,4,5,6]
result = list(filter(lambda x:x%2==0, nums))
print(result)


print("Filter students with marks > 50")
marks = [30,60,80,45]
result = list(filter(lambda x:x>50, marks))
print(result)


print("Filter words with length > 5")
words = ["python","ai","machine","data"]
result = list(filter(lambda x:len(x)>5, words))
print(result)


print("Sum of digits using recursion")
def digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + digit_sum(n//10)
print(digit_sum(123))


print("Flatten nested list")
nested = [[1,2],[3,4],[5]]
flat = []
for i in nested:
    for j in i:
        flat.append(j)
print(flat)


print("Count occurrences using dictionary")
numbers = [1,2,2,3,3,3]
count = {}
for i in numbers:
    count[i] = count.get(i,0) + 1
print(count)
