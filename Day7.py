print("Check Palindrome")
text = "madam"
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


print("Largest Number in List")
numbers = [10,20,5,40,15]
print(max(numbers))


print("Vowels in String")
text = "education"
count = 0
for i in text:
    if i in "aeiou":
        count += 1
print(count)


print("Create Dictionary and Print Values")
student = {
    "name":"Vinaya",
    "marks":90,
    "course":"BSc CS"
}
print(student.values())


print("Find Average & Topper")
students = []
for i in range(5):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students.append({"name":name, "marks":marks})
total = 0
topper = students[0]
for s in students:
    total += s["marks"]
    if s["marks"] > topper["marks"]:
        topper = s
average = total / len(students)
print("Average:", average)
print("Topper:", topper)


print("Reverse List")
numbers = [1,2,3,4,5]
numbers.reverse()
print(numbers)


print("Words in String")
text = "Artificial Intelligence and Machine Learning"
words = text.split()
print(len(words))


print("Remove Duplicates")
numbers = [1,2,2,3,4,4,5]
unique = list(set(numbers))
print(unique)


print("Second Largest")
numbers = [10,20,5,40]
numbers.sort()
print(numbers[-2])



