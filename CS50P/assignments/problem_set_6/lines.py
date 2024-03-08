# import sys
# def main():
#     lines()

# def lines():
#     try:
#         if len(sys.argv) <= 1:
#             sys.exit("Too few command-line arguments")
#         elif len(sys.argv) > 1:
#             sys.exit("Too many command-line arguments")
#         if sys.argv[1].endswith(".py"):
#             pass
#         else:
#             sys.exit("Not a Python file")

# # To handle file that doesn't exist issue
#     except FileNotFoundError:
#         print("File does not exist")
#         sys.exit("File does not exist")


# if __name__ == "__main__":
#     main()


"""
import sys


class TooFewArgumentsError(Exception):
    pass

class TooManyArgumentsError(Exception):
    pass

class NotPythonFileError(Exception):
    pass


def main():
    try:
        lines()
    except TooFewArgumentsError:
        print("Too few command-line arguments")
        sys.exit(1)
    except TooManyArgumentsError:
        print("Too many command-line arguments")
        sys.exit(1)
    except NotPythonFileError:
        print("Not a Python file")
        sys.exit(1)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

def lines():
    if len(sys.argv) <= 1:
        print("Inside TooFewArgumentsError")
        raise TooFewArgumentsError
    elif len(sys.argv) > 2:
        print("Inside TooManyArgumentsError")
        raise TooManyArgumentsError
    if not sys.argv[1].endswith(".py"):
        print("Inside NotPythonFileError")
        raise NotPythonFileError

if __name__ == "__main__":
    main()
"""


import sys

def main():
    try:
        if len(sys.argv) < 2:
            print("Too few command-line arguments")
        elif len(sys.argv) > 2:
            print("Too many command-line arguments")
        elif not(sys.argv[1].endswith(".py")):
            print("Not a Python file") 
        else:
            print(lines())
    except FileNotFoundError:
        sys.exit("File does not exist")

def lines():
    with open(sys.argv[1], "r") as file:
        line_count = 0
        for line in file:
            line_count += 1
            
            # if len(sys.argv) <= 1:
            #     sys.exit("Too few command-line arguments")
            # elif len(sys.argv) > 1:
            #     sys.exit("Too many command-line arguments")


    # except:
    #     if sys.argv[1].endswith(".py"):
    #         pass
    #     else:
    #         print(sys.exit("Not a Python file"))

    return line_count

if __name__ == "__main__":
    main()

"""
1. implement a program that expects one CLA, which is the name of python file
2. then output the no. of lines of code in that file, excluding comments and blank line

# Handle corner case
- does not specify exact one CLA
- does not specify file name as ".py"
- does not have CLA
-> should print sys.exit

"""
    