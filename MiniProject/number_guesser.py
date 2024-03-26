"""
1. create a number guesser function that let user input a number, count their guesses and return how many times for them to get the correct answer. we could generate our correct answer randomly
2. could set some condition to let user know is higher or lower than the correct answer
3

"""

import random

print("Welcome to number guessing game!")

answer = random.randint(0,10)
guesses = 0
guess_ls = []
# isdigit() is use to test for a string is a number or not
while True:
    number:str = input("Enter a guess: ")  
    while True:
        if number.isdigit():
            guess:int = int(number)
            guess_ls.append(guess)
            break
        else:
            print("Please enter a number")
            number:str = input("Enter a guess: ")
            continue
    
    
    if guess == answer:
        guesses += 1
        print("You got it!")
        break
    elif guess >= answer:
        guesses += 1
        print("Last guess was too high")
        print(f"here is your previous guess:", *guess_ls)
    elif guess <= answer:
        guesses += 1
        print("Last guess was too low")
        print(f"here is your previous guess: ", *guess_ls)
print(f"The answer is {answer}, and you have guess: {guesses} times.")


