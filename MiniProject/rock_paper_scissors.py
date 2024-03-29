"""
1. create a function that store rock, paper, scissors into a list, then can access the answer with indexing the list
2. set a random number for the computer, let user input then play with the computer, then count the wins and losses 
3. set q be quit() be my first condition, once quite the function, print the win and losses of user and computer 

"""

# my own rock paper scissors game
"""
import sys
import random

answer = input("Do you want to play rock, paper and scissors game? (Y/N) ")
choice_ls = ["rock", "paper", "scissors"]

if answer.lower() not in ['y', 'n']:
    print('please enter valid input')
elif answer.lower() == 'n':
    sys.exit("Welcome to play next time")
else:
    choice = input("What is your choice? (Rock/Paper/Scissors) ").lower()
    com_choice_int = random.randint(0, 2)
    com_choice = choice_ls[com_choice_int]

if choice not in choice_ls:
    print('please enter valid input')


if choice == com_choice:
    print(f"your choice: {choice}")
    print("It's a tie!")
elif choice == 'rock':
    if com_choice == "scissors":
        print(f"your choice: {choice}")
        print(f"computer choice: {com_choice}")
        print("You win!")
    else:
        print(f"your choice: {choice}")
        print(f"computer choice: {com_choice}")
        print("You lose!")
elif choice == 'rock':
    if com_choice == "paper":
        print(f"your choice: {choice}")
        print(f"computer choice: {com_choice}")
        print("You lose!")
    else:
        print(f"your choice: {choice}")
        print(f"computer choice: {com_choice}")
        print("You win!")

elif choice == 'paper':
    if com_choice == "scissors":
        print(f"your choice: {choice}")
        print(f"computer choice: {com_choice}")
        print("You lose!")
    else:
        print(f"your choice: {choice}")
        print(f"computer choice: {com_choice}")
        print("You win!")
    
elif choice == 'paper':
    if com_choice == "rock":
        print(f"your choice: {choice}")
        print(f"computer choice: {com_choice}")
        print("You win!")
    else:
        print(f"your choice: {choice}")
        print(f"computer choice: {com_choice}")
        print("You lose!")

elif choice == 'scissors':
    if com_choice == "rock":
        print(f"your choice: {choice}")
        print(f"computer choice: {com_choice}")
        print("You lose!")
    else:
        print(f"your choice: {choice}")
        print(f"computer choice: {com_choice}")
        print("You win!")

elif choice == 'scissors':
    if com_choice == "paper":
        print(f"your choice: {choice}")
        print(f"computer choice: {com_choice}")
        print("You win!")
    else:
        print(f"your choice: {choice}")
        print(f"computer choice: {com_choice}")
        print("You lose!")

"""

# online rock paper scisors game

import random
import sys

print("Welcome to my rock paper scissors game!\n")
choice_ls = ["rock", "paper", "scissors"]

com_wins = 0
player_wins = 0

while True:
    answer = input("Rock, paper, scissor or Q to quit the game? ").lower()
    if answer == "q":
        break
    elif answer not in choice_ls:
        print("please enter valid input")
        # if player is not inputting anything match with the choice_ls, continue would force player to enter sth match with the list first. It would back to the top of the while loop. It is one of the function in while loop
        continue

    com_choice_int = random.randint(0, 2)
    com_choice = choice_ls[com_choice_int]

    if com_choice == answer:
        print("It's a tie!")
    elif answer == "rock" and com_choice == "scissors":
        print("You win!")
        player_wins += 1
    elif answer == "paper" and com_choice == "rock":
        print("You win!")
        player_wins += 1
    elif answer == "scissors" and com_choice == "paper":
        print("You win!")
        player_wins += 1
    else:
        print("computer win!")
        com_wins += 1

print(f"You win {player_wins} times.")
print(f"Computer win {com_wins} times.")

print("Goodbye!")

