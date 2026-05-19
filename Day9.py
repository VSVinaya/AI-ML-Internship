#Create file with student data
file = open("students.txt","w")
file.write("John,80\n")
file.write("Sara,90\n")
file.write("Alex,70")
file.close()


print("Read and store in list of dictionary")
students = []
with open("students.txt","r") as file:
    for line in file:
        name, marks = line.strip().split(",")
        students.append({
            "name":name,
            "marks":int(marks)
        })
print(students)


print("Print all students")
students = [
    {"name":"John","marks":80},
    {"name":"Sara","marks":90}
]
for s in students:
    print(s)


print("Find average marks")
students = [
    {"name":"John","marks":80},
    {"name":"Sara","marks":90}
]
total = sum(s["marks"] for s in students)
avg = total / len(students)
print(avg)


print("Find topper")
students = [
    {"name":"John","marks":80},
    {"name":"Sara","marks":90}
]
top = max(students, key=lambda x:x["marks"])
print(top)


print("students with marks > 75")
students = [
    {"name":"John","marks":80},
    {"name":"Sara","marks":90},
    {"name":"Alex","marks":70}
]
for s in students:
    if s["marks"] > 75:
        print(s)


print("Number of students")
students = [
    {"name":"John","marks":80},
    {"name":"Sara","marks":90}
]
print(len(students))


print("Lowest marks")
students = [
    {"name":"John","marks":80},
    {"name":"Sara","marks":90},
    {"name":"Alex","marks":70}
]
low = min(students, key=lambda x:x["marks"])
print(low)


print("Sort students by marks")
students = [
    {"name":"John","marks":80},
    {"name":"Sara","marks":90},
    {"name":"Alex","marks":70}
]
sorted_students = sorted(students, key=lambda x:x["marks"])
print(sorted_students)


print("Function to Calculate average")
def average(students):
    total = sum(s["marks"] for s in students)
    return total / len(students)
students = [
    {"name":"John","marks":80},
    {"name":"Sara","marks":90}
]
print(average(students))


print("Function to find topper")
def topper(students):
    return max(students, key=lambda x:x["marks"])
students = [
    {"name":"John","marks":80},
    {"name":"Sara","marks":90}
]
print(topper(students))


print("Function to filter students")
def filter_students(students):
    result = []
    for s in students:
        if s["marks"] > 75:
            result.append(s)
    return result
students = [
    {"name":"John","marks":80},
    {"name":"Alex","marks":70}
]
print(filter_students(students))


print("Student with second highest marks")
students = [
    {"name":"John","marks":80},
    {"name":"Sara","marks":90},
    {"name":"Alex","marks":70}]
students.sort(key=lambda x:x["marks"])
print(students[-2])


print("Count passed and failed students")
marks = [80,40,90,30]
passed = 0
failed = 0
for m in marks:
    if m >= 50:
        passed += 1
    else:
        failed += 1
print("Passed:", passed)
print("Failed:", failed)


print("Convert data into dictionary format")
names = ["John","Sara"]
marks = [80,90]
students = {}
for i in range(len(names)):
    students[names[i]] = marks[i]
print(students)
