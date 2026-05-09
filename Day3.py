print("Create a list of 10 numbers")
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)


print("Find sum of list elements")
numbers = [1,2,3,4,5]
print(sum(numbers))


print("Find maximum number")
numbers = [10,25,5,40,15]
print(max(numbers))


print("even numbers from list")
numbers = [1,2,3,4,5,6,7,8]
for i in numbers:
    if i % 2 == 0:
        print(i)

        
print("Reverse a list")
numbers = [1,2,3,4,5]
numbers.reverse()
print(numbers)


print("Create student dictionary")
student = {
    "name":"Vinaya",
    "age":20,
    "marks":85
}
print(student)


print("Update marks")
student = {
    "name":"Vinaya",
    "marks":85
}
student["marks"] = 95
print(student)


print("Add new key")
student = {
    "name":"Vinaya",
    "marks":95
}
student["grade"] = "A"
print(student)


print("Print all keys and values")
student = {
    "name":"Vinaya",
    "age":20,
    "marks":90
}
for key,value in student.items():
    print(key,":",value)


print("Count number of characters")
text = "Hello AI"
print(len(text))


print("Reverse a string")
text = "Python"
print(text[::-1])


print("Check palindrome")
text = "madam"
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


print("Count vowels")
text = "education"
count = 0
for i in text:
    if i in "aeiou":
        count += 1

print(count)


print("Remove duplicates using set")
numbers = [1,2,2,3,4,4,5]
print(set(numbers))


print("Find common elements")
a = {1,2,3,4}
b = {3,4,5,6}
print(a.intersection(b))


print("Squares from 1-10")
squares = [x*x for x in range(1,11)]
print(squares)


print("Even numbers from 1-20")
even = [x for x in range(1,21) if x % 2 == 0]
print(even)
