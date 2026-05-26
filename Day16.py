#Cleaning Practice

# print("Remove None Values")
# students = [
#  {"name":"A","marks":80},
#  {"name":"B","marks":None},
#  {"name":"C","marks":70}
# ]
# cleaned = [s for s in students if s["marks"] is not None]
# print(cleaned)


# print("Remove Negative Values")
# students = [
#  {"name":"A","marks":80},
#  {"name":"B","marks":-10},
#  {"name":"C","marks":70}
# ]
# cleaned = [s for 
# s in students if s["marks"] >= 0]
# print(cleaned)


# print("Keep Only Valid Data")
# students = [
#  {"name":"A","marks":80},
#  {"name":"B","marks":None},
#  {"name":"C","marks":-5},
#  {"name":"D","marks":90}
# ]
# cleaned = [s for s in students if s["marks"] is not None and s["marks"] >= 0]
# print(cleaned)


#Transformation

# print("Add Pass/Fail Field")
# students = [
#  {"name":"A","marks":80},
#  {"name":"B","marks":40}
# ]
# for s in students:
#     s["status"] = "Pass" if s["marks"] >= 50 else "Fail"
# print(students)


# print("Convert Marks to Percentage")
# marks = [80,90,70]
# percentage = [m/100 for m in marks]
# print(percentage)


# print("Create New Calculated Field")
# students = [
#  {"name":"A","marks":80},
#  {"name":"B","marks":60}
# ]
# for s in students:
#     s["bonus"] = s["marks"] + 5
# print(students)

#Sorting

# print("Sort Students by Marks")
# students = [
#  {"name":"A","marks":80},
#  {"name":"B","marks":95},
#  {"name":"C","marks":60}
# ]
# students.sort(key=lambda x:x["marks"], reverse=True)
# print(students)


# print("Print Top 3 Students")
# students = [
#  {"name":"A","marks":80},
#  {"name":"B","marks":95},
#  {"name":"C","marks":60},
#  {"name":"D","marks":88}
# ]
# students.sort(key=lambda x:x["marks"], reverse=True)
# print(students[:3])


#Grouping


# print("Group Pass and Fail")
# students = [
#  {"name":"A","marks":80},
#  {"name":"B","marks":40},
#  {"name":"C","marks":70}
# ]
# result = {"pass":[],"fail":[]}
# for s in students:
#     if s["marks"] >= 50:
#         result["pass"].append(s)
#     else:
#         result["fail"].append(s)
# print(result)


# print("Count Each Group")
# students = [
#  {"name":"A","marks":80},
#  {"name":"B","marks":40},
#  {"name":"C","marks":70}
# ]
# passed = 0
# failed = 0
# for s in students:
#     if s["marks"] >= 50:
#         passed += 1
#     else:
#         failed += 1
# print("Pass:", passed)
# print("Fail:", failed)

#Data Analysis

print("Find Average Marks")
marks = [80,90,70]
avg = sum(marks) / len(marks)
print(avg)

print("Find Highest Marks")
marks = [80,90,70]
print(max(marks))

print("Find Lowest Marks")
marks = [80,90,70]
print(min(marks))
