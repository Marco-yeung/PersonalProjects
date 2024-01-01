students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": None},
    {"name": "Ron", "house": "Slytherin", "patronus": "Jack Russell terrier"}
    ]

for student in students:
    print(student["name"], student["patronus"], sep = ", ")