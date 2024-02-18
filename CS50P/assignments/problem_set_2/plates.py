import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# requirments for regex: Numbers cannot be used in the middle of a plate; they must come at the end. ALSO, The first number used cannot be a ‘0’
# Here User can start with captial A to Z, then at least one character for A to Z/ 1-9 using + operator. Lastly endwith 0-9
def is_valid(s):
    if len(s) <= 6 and len(s) >= 2 and re.search(r"^[A-Z][1-9A-Z]+[0-9]$", s): 
        return True
    else:
        return False


main()