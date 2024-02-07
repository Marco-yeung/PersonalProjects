with open("students.csv") as file:
    for line in file:
        # split would give us a list of strings
        row = line.rstrip().split(",")
        # print the first element of row and is in second element of row
        print(f"{row[0]} is in {row[1]}")