#Print your details
name = "Vinaya"
age = 20
course = "BSc Computer Science"
print("Name:", name)
print("Age:", age)
print("Course:", course)

#Add, subtract, multiply two numbers
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

#Check even or odd
num = 8
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

#Find largest of two numbers
a = 15
b = 20
if a > b:
    print("Largest number is", a)
else:
    print("Largest number is", b)

#Take input and display it
name = input("Enter your name: ")
print("Welcome", name)


#Check positive, negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")


#Find largest of 3 numbers
a = 10
b = 25
c = 15
if a > b and a > c:
    print("Largest number is", a)
elif b > c:
    print("Largest number is", b)
else:
    print("Largest number is", c)


#Grade system
marks = 85
if marks > 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")


print("numbers 1–20")
for i in range(1, 21):
    print(i)


print("even numbers")
for i in range(2, 21, 2):
    print(i)


print("sum of first N numbers")
n = 5
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum is", sum)


print("Reverse number")
for i in range(10, 0, -1):
    print(i)

#Function to add two numbers
def add(a, b):
    return a + b
print(add(5, 3))

#Function to check prime number
def prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("Prime Number")
    else:
        print("Not Prime Number")
prime(7)

#Function to find factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print(factorial(5))
