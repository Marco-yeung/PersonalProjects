"""
with open("students.csv") as file:
    for line in file:
        # split would give us a list of strings
        row = line.rstrip().split(",")
        # print the first element of row and is in second element of row
        print(f"{row[0]} is in {row[1]}")
"""

# more readable way of doing it, instead of using row[0] and row[1]
"""
with open("students.csv") as file:
    for line in file:
        # split would give us a list of strings
        name, house = line.rstrip().split(",")
        # print the first element of row and is in second element of row
        print(f"{name} is in {house}")
"""

"""
students = []

with open("student.csv") as file:
    for line in fileL
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)

"""

# using dictionaries to solve the problem
# here I have sollected all the info I have for students while still keeping track, what is name and what is house
"""
students = []

with open("student.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student= {}
        student["name"] = name
        student["house"] = house
        students.append(student)

    for student in students:
        print(f"student['name'] is in {student['house']}")

"""

"""
students = []

with open("student.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # it create a non empty dictionary with the name key and house key
        student= {"name": name, "house": house}
        students.append(student)

    for student in students:
        print(f"student['name'] is in {student['house']}")

"""

# introducing a function get_name and get_house to sort the dictionary output
"""
students = []

with open("student.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # it create a non empty dictionary with the name key and house key
        student= {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

def get_house(student):
     return student["house"]

# key could throw in another function to tell python how we want to sort the dictionary output
for student in sorted(students, key = get_name, reverse = True):
        print(f"student['name'] is in {student['house']}")

"""

# introducing lambda function
"""
students = []

with open("student.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # it create a non empty dictionary with the name key and house key
        student= {"name": name, "house": house}
        students.append(student)
# This lambda function are gonna called every one of the dictionaries in that list
for student in sorted(students, key = lambda student: student["name"]):
        print(f"student['name'] is in {student['house']}")
 
"""