import random
import string

def generate_password(min_length, numbers = True, special_characters = True):
    # string.ascii_letters would generate all uppercase and lowercase characters
    letters = string.ascii_letters
    digits = string.digits
    # string.punctuation would generate all special characters
    special = string.punctuation

    characters = letters
    # if numbers is True, we would add those digits to our characters(passwords)
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False


    # while we are not meeting the criteria (we don't have a number or special characters) or we have lenght of passwords less than our minimum length. we would continue to add characters to our pasword
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        # common pattern of programming: You start a variable equal to True, then you try to prove the variable is equal to false
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print(f"The generated password is {pwd}")