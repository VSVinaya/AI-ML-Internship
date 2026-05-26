#Data Practice

print("Create List of Marks")
marks = [80,90,70,60]

print("Find Average")
marks = [80,90,70,60]
avg = sum(marks) / len(marks)
print(avg)

print("Find Max and Min")
marks = [80,90,70,60]
print(max(marks))
print(min(marks))

print("Count Total Students")
marks = [80,90,70,60]
print(len(marks))

#Data Cleaning

print("Remove None Values")
marks = [80,90,None,70]
cleaned = [m for m in marks if m is not None]
print(cleaned)

print("Remove Negative Values")
numbers = [10,-5,20,-2,30]
cleaned = [n for n in numbers if n >= 0]
print(cleaned)

print("Clean Invalid Data")
data = [80,"abc",90,None,70]
cleaned = [x for x in data if type(x) == int]
print(cleaned)

#Data Filtering

print("Find Passed Students")
marks = [80,40,90,30]
passed = [m for m in marks if m >= 50]
print(passed)

print("Marks Greater Than 75")
marks = [60,85,90,70]
result = [m for m in marks if m > 75]
print(result)

print("Filter Even Numbers")
numbers = [1,2,3,4,5,6]
even = [n for n in numbers if n % 2 == 0]
print(even)

#Data Transformation

print("Convert Marks to Percentage")
marks = [80,90]
scaled = [m/100 for m in marks]
print(scaled)

print("Multiply Values")
numbers = [1,2,3,4]
result = [n*10 for n in numbers]
print(result)

print("Normalize Data")
numbers = [10,20,30]
max_value = max(numbers)
normalized = [n/max_value for n in numbers]
print(normalized)
