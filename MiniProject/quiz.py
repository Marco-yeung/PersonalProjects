import sys

print("Welcome to my quiz game!")

answer = input("Do you want to play a game? (Y/N): ")

score = 0

if answer.lower() == "y":
    answer = input("What is ILAS stand for? ")
    if answer.lower() == "investment-linked assurance scheme":
        print("Yes, You are right")
        score += 1
    elif answer.lower() == "investment linked assurance scheme":
        print("You are so close")
    else:
        print("Here is next question")

    answer = input("What is GI stand for? ")
    if answer.lower() == "general insurance":
        print("Yes, You are right")
        score += 1
    else:
        print("Here is next question")

    answer = input("What is LI stand for? ")
    if answer.lower() == "life insurance":
        print("Yes, You are right")
        score += 1
    else:
        pass

elif answer.lower() == "n":
    sys.exit("Welcome to play it next time!")
    # quit()
else:
    sys.exit("please enter valid input")
    # quit()

print("ended")
print(f"Your score is {score}")