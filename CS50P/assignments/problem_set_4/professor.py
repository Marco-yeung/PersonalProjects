import random


def main():
    level = get_level()
    no_of_question = 0
    score = 0
    
    while no_of_question < 10:
        no_of_attempts: int = 0
        question = generate_integer(level)
        answer: int = int(question[0] + question[1])
        while no_of_attempts <= 3:
            answer_input: int = int(input(f"{question[0]} + {question[1]} = "))
            if answer_input == answer:
                score += 1
                break
            else:
                no_of_attempts += 1
                if no_of_attempts == 3:
                    print("EEE")
                    break
        no_of_question += 1
    print(f"Score: {score}")


    
    
    
def get_level():
    valid_levels = (1,2,3)
    try:
        while True:
            n: int = int(input("Level: "))
            if n in valid_levels:
                break
    except ValueError:
        return get_level()
    return n


def generate_integer(level):
    min_no = 10 ** (level - 1)
    max_no = (10 ** level) -1

# level 1: (0 - 9)
# level 2: (10 - 99)
# level 3: (100 - 999)
    x: int = random.randint(min_no, max_no)
    y: int = random.randint(min_no, max_no)
    return x,y


if __name__ == "__main__":
    main()

"""
1. prompt the user to input 1,2 or 3 represent the level. If not should promopt the user input again
2. randomly generate 10 problem ( X + Y =), X and Y are non-negative integers, with n digits. -> prompt the user to answer all the Q
3. If answer is not correct(or not even a no.), print "EEE", and let user input again. Let user have up to 3 trial.
4. if user cant get the answer, print the correct answer


It should have count their total score out of 10 marks

    
"""