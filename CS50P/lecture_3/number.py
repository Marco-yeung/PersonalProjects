# while True:
#     try:    
#         x = int(input("What is x?"))
#     # here we are trying to catch the value error 

#     except ValueError:
#         print("x is not an integer")

#     # and we should try more corner cases to catch more error for the user

#     # we could use the "else" keyword to catch the error if the value is not an integer
#     else:
#         break
    
# print(f"x is {x}")

# # a more condensed version of the while loop
# while True:
#     try:
#         x = int(input("What is x?"))
#         break
#     except ValueError:
#         print("x is not an integer")        
        
# print(f"x is {x}")

# a step backward to the code and make it into a function
# def main():
#     x = get_int()
#     print(f"x is {x}")


# def get_int():
#     while True:
#         try:
#             x = int(input("What is x?"))
#         except ValueError:
#             print("x is not an integer")
#             # # we could use pass here to handle the error, we just omit it and deal with it later
#             # pass
#         else:
#             break
#     return x

# a more condensed version of the while loop
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What is x? "))
        except ValueError:
            print("x is not an integer")
            # pass

main()

# common error could be raised
# - SyntaxError: Usually related to missing the closing quote
# - ValueError: Usually related to entering data type other than a integer/float in the argument
# - NameError: Usually related to a variable that haven't been defined yet
            
        