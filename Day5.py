print("Reverse a string")
text = "Python"
print(text[::-1])


print("number of words")
text = "Artificial Intelligence and Machine Learning"
words = text.split()
print(len(words))


print("Check palindrome")
text = "madam"
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


print("Replace words")
text = "Hello AI"
print(text.replace("AI", "ML"))


print("Count vowels")
text = "education"
count = 0
for i in text:
    if i in "aeiou":
        count += 1
print(count)


print("list of 5 students")
students = [
    {"name":"A", "marks":70},
    {"name":"B", "marks":85},
    {"name":"C", "marks":90},
    {"name":"D", "marks":60},
    {"name":"E", "marks":95}
]
print(students)


print("Print all students")
students = [
    {"name":"A", "marks":70},
    {"name":"B", "marks":85}
]
for s in students:
    print(s["name"], s["marks"])


print("average marks")
students = [
    {"name":"A", "marks":70},
    {"name":"B", "marks":80}
]
total = 0
for s in students:
    total += s["marks"]
avg = total / len(students)
print(avg)


print("highest marks")
students = [
    {"name":"A", "marks":70},
    {"name":"B", "marks":95},
    {"name":"C", "marks":80}
]
highest = 0
for s in students:
    if s["marks"] > highest:
        highest = s["marks"]
print(highest)


print("students with marks > 75")
students = [
    {"name":"A", "marks":70},
    {"name":"B", "marks":85},
    {"name":"C", "marks":90}
]
for s in students:
    if s["marks"] > 75:
        print(s["name"])

print("Second highest number in list")
numbers = [10, 20, 30, 40, 50]
numbers.sort()
print(numbers[-2])


print("frequency of characters")
text = "python"
for i in text:
    print(i, ":", text.count(i))


print("Remove duplicates")
numbers = [1,2,2,3,4,4,5]
unique = list(set(numbers))
print(unique)


print("math module")
import math
print(math.sqrt(25))
print(math.pow(2, 3))


print("Use random module")
import random
print(random.randint(1, 10))
colors = ["red", "blue", "green"]
print(random.choice(colors))


print("your own module")
import mymodule
print(mymodule.greet("Vinaya"))
