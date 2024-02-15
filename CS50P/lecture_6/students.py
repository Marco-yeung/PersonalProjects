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

with open("students.csv") as file:
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

with open("students.csv") as file:
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

with open("students.csv") as file:
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

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # it create a non empty dictionary with the name key and house key
        student= {"name": name, "house": house}
        students.append(student)
# This lambda function are gonna called every one of the dictionaries in that list
for student in sorted(students, key = lambda student: student["name"]):
        print(f"student['name'] is in {student['house']}")
 
"""

# introducing csv module
"""
import csv
students = []

# this reader function in csv woud help us read the file and figure out where is the comma
# a reader would return list
with open("students.csv") as file:
    reader = csv.reader(file)
    for name, reader in reader:
          students.append({"name": name, "house": reader})
# This lambda function are gonna called every one of the dictionaries in that list
for student in sorted(students, key = lambda student: student["name"]):
        print(f"student['name'] is in {student['house']}")
"""

# introducing dict_reader
"""
import csv
students = []

# this reader function in csv woud help us read the file and figure out where is the comma
with open("students_dict.csv") as file:
# DictReader would return a dictionary
    reader = csv.DictReader(file)
    for row in reader:
          students.append({"name": row["name"], "house": row["home"]})
# This lambda function are gonna called every one of the dictionaries in that list
for student in sorted(students, key = lambda student: student["name"]):
        print(f"student['name'] is in {student['house']}")
"""

# here we are using writerow to write things in the csv
"""
import csv 

name = input("What's you name")
home = input("Where's your home")

with open("students_input.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
"""

# here we are using DictWriter
import csv 

name = input("What's you name")
home = input("Where's your home")

with open("students_input.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "home"])
    writer.writerow({"name": name, "house": home})
