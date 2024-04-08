"""
create a math game to ask user x questions, we can set the question be like "1 + 2" / "4 - 2"
let computer to choose the operator and the number for us
we can set the limit of the left/right number
we need to time the user how much time they used to answer x questions
eval() is python in-built function to calculate an answer for the math question
"""

import random
import time

# we are using all capital letters to represent these are our constants
# MIN and MAX operand means the largest and smallest number we would like to have in our problems
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    # eval() would evaluate a string is it a python expression
    answer = eval(expr)
    return expr, answer

wrong = 0
input('press enter to start')
print("---------------------------------")

# This would give us the time stamp in seconds
start_time = time.time()

# expr, answer = generate_problem()
# print(expr, "=", answer)

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + ":" + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time
    
print("--------------------")
print(f"Nice work! You finished it in {total_time:.2f} seconds!")