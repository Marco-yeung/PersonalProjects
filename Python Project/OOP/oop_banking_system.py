"""
Link: https://www.youtube.com/watch?v=xTh-ln2XhgU
Title: How to create a banking system using Object Oriented Programming in python for beginners
Here are we create a Parent class, User, to store user name, age, gender
Also to create a child class, Bank, to handle user deposit and withdrawal
"""

# Parent class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_details(self):
        print("Person Details")
        print("")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

# Info of parent class and child class
        
"""
The parent class defines common attributes and behaviors that can be shared among multiple child classes.
The child class extends the functionality of the parent class by adding new attributes or overriding existing ones.
The child class can introduce new methods or properties specific to its own implementation.
The parent class acts as a blueprint for creating child classes.
The child class can access and initialize attributes defined in the parent class using the super() keyword.
"""


# Child class
class Bank(User):
    def __init__(self, name, age, gender):
        super.__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account valance has been updated : $", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds, Balance Available : $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account valance has been updated : $", self.balance)
        
    def view_balance(self):
        self.show_detials()
        print("Account Balance : $", self.balance)

        