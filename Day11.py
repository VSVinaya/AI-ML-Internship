#Inheritance Practice
#Create Animal and Dog class
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    pass
d1 = Dog()
d1.sound()


#Method Overriding
#Vehicle and Car class
class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    def start(self):
        print("Car starts with key")
c1 = Car()
c1.start()


# Encapsulation Practice
# BankAccount Class
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount
    def check_balance(self):
        print(self.__balance)
b1 = BankAccount(1000)
b1.deposit(500)
b1.withdraw(200)
b1.check_balance()


# Combined Practice
# Person and Employee Class
class Person:
    def __init__(self, name):
        self.name = name
class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
e1 = Employee("Alex", 50000)
e1.display()

