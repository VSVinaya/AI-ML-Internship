print("maximum and minimum")
numbers = [10,20,5,40,15]
print(max(numbers))
print(min(numbers))


print("second largest")
numbers = [10,20,5,40]
numbers.sort()
print(numbers[-2])


print("Remove duplicates")
numbers = [1,2,2,3,4,4]
unique = list(set(numbers))
print(unique)


print("even and odd numbers")
numbers = [1,2,3,4,5,6]
even = 0
odd = 0
for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even)
print("Odd:", odd)


print("Reverse string")
text = "python"
print(text[::-1])


print("Check palindrome")
text = "madam"
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


print("Count characters")
text = "hello"
count = {}
for ch in text:
    count[ch] = count.get(ch,0) + 1
print(count)


print("Count vowels and consonants")
text = "education"
vowels = 0
consonants = 0
for i in text:
    if i in "aeiou":
        vowels += 1
    else:
        consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)


print("student list")
students = [
    {"name":"A","marks":70},
    {"name":"B","marks":90}
]
print(students)


print("topper")
students = [
    {"name":"A","marks":70},
    {"name":"B","marks":95}
]
top = students[0]
for s in students:
    if s["marks"] > top["marks"]:
        top = s
print(top)


print("Calculate average")
students = [
    {"name":"A","marks":70},
    {"name":"B","marks":90}
]
total = 0
for s in students:
    total += s["marks"]
avg = total / len(students)
print(avg)


print("Filter passed students")
marks = [50,80,90,40]
passed = [m for m in marks if m >= 50]
print(passed)


print("Second smallest number")
numbers = [10,20,5,40]
numbers.sort()
print(numbers[1])


print("Merge two lists without duplicates")
a = [1,2,3]
b = [3,4,5]
merged = list(set(a+b))
print(merged)


print("Frequency of elements")
numbers = [1,2,2,3,3,3]
for i in numbers:
    print(i, ":", numbers.count(i))
