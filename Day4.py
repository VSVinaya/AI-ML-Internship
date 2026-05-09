print("Create file and write your details")
file = open("details.txt", "w")
file.write("Name: Vinaya\n")
file.write("Course: BSc Computer Science\n")
file.write("Age: 20")
file.close()


print("Read file and display")
file = open("details.txt", "r")
print(file.read())
file.close()

print("Append new data")
file = open("details.txt", "a")
file.write("\nCollege: St. Paul's College")
file.close()


print("Count number of lines")
with open("details.txt", "r") as file:
    lines = file.readlines()
    print(len(lines))


print("Count number of words")
with open("details.txt", "r") as file:
    text = file.read()
    words = text.split()
    print(len(words))

print("Handle divide by zero")
try:
    num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")


print("Handle invalid input")
try:
    age = int(input("Enter age: "))
    print(age)
except ValueError:
    print("Invalid Input")


print("Use try-except-else-finally")
try:
    num = int(input("Enter number: "))
except:
    print("Error")
else:
    print("No Error")
finally:
    print("Program Finished")


print("Handle file not found error")
try:
    file = open("sample.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
    

print("Find longest word in file")
with open("details.txt", "r") as file:
    text = file.read()
    words = text.split()
    longest = max(words, key=len)
    print(longest)


print("Count vowels in file")
with open("details.txt", "r") as file:
    text = file.read().lower()
    count = 0
    for i in text:
        if i in "aeiou":
            count += 1
    print(count)


print("Remove duplicate lines")
with open("details.txt", "r") as file:
    lines = file.readlines()
unique = set(lines)
print(unique)

