name = input("What is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    # if nth else fit the above condition, it will fall to below condition
    case _:
        print("Who?")