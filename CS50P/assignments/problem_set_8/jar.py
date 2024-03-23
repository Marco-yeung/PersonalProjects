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
# my own code
"""
class Jar:
    def __init__(self, capacity=12, actual = 0):
        self.capacity = capacity
        self.actual = actual

    def __str__(self):
        return f"Jar: ", {self.actual} * "🍪"

    def deposit(self, n):
        if self.actual + n < self.capacity:
            self.actual += n
        else:
            print('The jar is full that it cant contain that much cookie')
    def withdraw(self, n):
        if n < self.actual:
            self.actual -= n
        else:
            print("The jar doesn't have that much cookies")
    # getter for capacity
    @property
    def capacity(self):
        return self._capacity
    # setter for capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("Capacity must be a positive integer")

    @property
    def size(self):
        return self._actual
    
    @size.setter
    def size(self, size):
        if size >= 0:
            self._actual = size
        else:
            raise ValueError("Size must be a non-negative integer")
        
    """

# tutor code
"""

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Wrong capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Invalid capacity")
        if n + self.size > self.capacity:
            raise ValueError("Not enough capacity")
        self.size += n
        

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Not enough cookies to remove")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
        
jar = Jar()
print(jar)

"""

class Jar:
    def __init__(self, capacity=12)-> None:
        self.capacity = capacity
        self.size = 0

    def __str__(self) -> str:
        return self.size * "🍪"
    
    def deposit(self, n:int)-> None:
        self.size += n
    
    def withdraw(self, n:int)-> None:
        self.size -= n

    # getter of capacity
    @property
    def capacity(self) -> int:
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity:int) -> None:
        if capacity < 0:
            raise ValueError("Invalid capacity of the jar")
        self._capacity = capacity

    # getter of size
    @property
    def size(self) -> int:
        return self._size
    
    @size.setter
    def size(self, size:int)-> None:
        if size < 0:
            raise ValueError("Too few cookies")
        if size > self.capacity:
            raise ValueError("Too many cookies")
        self._size = size
        
        

    