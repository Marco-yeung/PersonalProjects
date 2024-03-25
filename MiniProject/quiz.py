import sys

print("Welcome to my quiz game!")

answer = input("Do you want to play a game? (Y/N): ")

if answer.lower() == "y":
    answer = input("What is ILAS stand for?")
    if answer.lower() == "Investment-Linked Assurance Scheme":
        print("Yes, You are right")
    elif answer.lower() == "Investment Linked Assurance Scheme":
        print("You are so close")
    else:
        print("Please try again")

elif answer.lower() == "n":
    sys.exit("Welcome to play it next time!")
    # quit()
else:
    sys.exit("please enter valid input")
    # quit()