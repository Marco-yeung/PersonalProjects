
"""
names = []


for _ in range(3):
    names.append(input("What is your name? "))

# sorted is an inbuilt function in python, it would sort the list in ascending order
for name in sorted(names):
    print(f"Hello, {name}") 

"""
# code above can first create an empty list, then add the 3 name and sort it, but it cant store the name we enter
# Therefore, we would need to have a notepad/excel to store the data

"""
name  = input("what is your name? ")
# using "a" in second argument even if the file not even exists, it would still creawte a new one first, then append a new data later

file = open("names.txt", "a")
file.write(f"{name}\n")
# file.close() would literally save and close the file
file.close()
"""

# with function could automatically open and close a file
"""
name = input("what is your name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
"""

# once the names.txt has been created, it would have names sotre in it
"""
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
"""

# when I want to store the names and sorted it the same time when I am using open function
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

# a much more compact way of doing it
"""
    with open("names.txt") as file:
        for line in sorted(file):
            print(f"hello, {line.rstrip()}")
"""


 