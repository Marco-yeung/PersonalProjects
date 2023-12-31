# hello function
name = input("What is your name? ")
# title() could only captialize the first letter of the name
name.strip().title()
name = name.capitalize()
print(f"Hello, {name}")
# default the end would open a new line to print another print statement, it could subsitute to anything
# the same as sep, it could be anything else instead of a space
# print(f"Hello, {name.capitalize()}", sep = " ", end = "\n")