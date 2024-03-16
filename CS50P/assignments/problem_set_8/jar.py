"""
1. implement a class called Jar
- __init__: a Jar with given capacity, and it is not a non-negative integer, otherwise it should raise a ValueError
- __str__: return a string with n 🍪, where n is the number of cookie in the cookie jar
- deposit: should add n cookies to the cookie jar
    -> if adding that would exceed the capacity, should raise a ValueError
- withdraw: should remove n cookies from the cookie jar
    -> if removing that would be negative, should raise a ValueError
- capacity: should return the cookie jar capacity
- size: should return the number of cookie actually in the cookie jar, initially 0

"""

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    def __str__(self):
        ...

    def deposit(self, n):
        self.capacity += n

    def withdraw(self, n):
        self.capacity -= n

    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        return 