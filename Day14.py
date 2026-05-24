
#JSON Practice

# print("Convert Dictionary to JSON")
# import json
# data = {
#     "name":"Sara",
#     "marks":90
# }
# json_data = json.dumps(data)
# print(json_data)


# print("Convert JSON to Dictionary")
# import json
# json_data = '{"name":"Sara","marks":90}'
# data = json.loads(json_data)
# print(data)


# print("Write JSON to File")
# import json
# data = {
#     "name":"Alex",
#     "marks":85
# }
# with open("data.json","w") as file:
#     json.dump(data,file)


# print("Read JSON from File")
# import json
# with open("data.json","r") as file:
#     data = json.load(file)
# print(data)

#CSV Practice

#Create CSV File and Write Student Data
# import csv
# with open("data.csv","w",newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["name","marks"])
#     writer.writerow(["John",80])
#     writer.writerow(["Sara",90])


# print("Read CSV File")
# import csv
# with open("data.csv","r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# print("Print Formatted Output")
# import csv
# with open("data.csv","r") as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         print("Name:", row[0])
#         print("Marks:", row[1])


#Combined Task

#Read CSV , Convert to Dictionary and Save as JSON
import csv
import json
students = []
with open("data.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)
with open("students.json","w") as file:
    json.dump(students,file,indent=4)
print("JSON file created")
