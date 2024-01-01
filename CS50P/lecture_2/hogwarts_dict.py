students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Slytherin"
}

# while using for loop in dictionary, it would print the key for it, but not the value
# for s in students:
#     print(s)
    
# student[s] could access to the value of the key
for s in students:
    print(s, students[s], sep = " ")