# #Create class Create object and print values
# class Car:
#     name = ""
#     price = 0
# c1 = Car()
# c1.name = "BMW"
# c1.price = 5000000
# print(c1.name)
# print(c1.price)


# #Create class Student using constructor
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
# s1 = Student("John", 85)
# print(s1.name)
# print(s1.marks)


# print("Check pass/fail and calculate grade")
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def is_pass(self):
#         if self.marks >= 50:
#             return "Pass"
#         else:
#             return "Fail"
#     def grade(self):
#         if self.marks >= 90:
#             return "A"
#         elif self.marks >= 75:
#             return "B"
#         else:
#             return "C"
# s1 = Student("Sara", 92)
# print(s1.is_pass())
# print(s1.grade())


# print("Create list of students and find topper")
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
# students = [
#     Student("A",70),
#     Student("B",95),
#     Student("C",60)
# ]
# for s in students:
#     print(s.name, s.marks)
# topper = students[0]
# for s in students:
#     if s.marks > topper.marks:
#         topper = s
# print("Topper:", topper.name)


print("Create Class BankAccount")
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def check_balance(self):
        print(self.balance)
b1 = BankAccount(1000)
b1.deposit(500)
b1.withdraw(200)
b1.check_balance()


print("Create Class Product")
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def discount(self):
        return self.price - (self.price * 0.10)
p1 = Product("Laptop", 50000)
print(p1.name)
print(p1.discount())
