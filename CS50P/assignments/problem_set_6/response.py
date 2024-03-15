from validator_collection import validators, checkers, errors

def main():
    print(is_email(input("what's your email address? ")))

def is_email(email):
    if checkers.is_email(email):
        return "Valid"
    else:
        return "Invalid"
    
if __name__ == "__main__":
    main()
