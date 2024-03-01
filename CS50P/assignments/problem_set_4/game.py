import random 

# while True:
#     try:     
#         n = input("Level: ")
#         n = int(n)
#     except ValueError:
#          continue 
#     except:
#          if n <= 0:
#               continue     
#     try:
#         while n > 0:
#                 ans = random.randint(1,n)
#                 guess = input("Guess: ")
#                 guess = int(guess)
#                 if guess == ans:
#                     print("Just right")
#                 elif guess <= ans:
#                     print("Too small")
#                 elif guess >= ans:
#                     print("Too large")
#     except ValueError:
#         continue
#     except:
#          if guess <= 0:
#               continue

def main():
    level = level_input()
    guess = guess_input()
    ans = random.randint(1,level)
    print(condition(level, guess, ans))


def level_input():
    while True:
        try:     
            n = input("Level: ")
            n = int(n)
            if n <= 0:
                continue
            break
        except ValueError:
            continue 
    return n        

def guess_input():
    while True:
        try:
            # while n > 0:
                # ans = random.randint(1,n)
                guess = input("Guess: ")
                guess = int(guess)
                if guess <= 0:
                    continue    
                break
        except ValueError:
            continue
    return guess
            

# def condition(level: int, guess: int, x):
#     #  ans = random.randint(1,level)
#     while True:
#         if guess == x:
#             # return "Just right"
#             break
#         elif guess <= x:
#             print("Too small")
#             continue
#         elif guess >= x:
#             print("Too large")
#             continue
#     return "Just right"

def condition(level: int, guess: int, x):
    while guess != x:
        if guess < x:
            print("Too small!")
        elif guess > x:
            print("Too large!")
        guess = guess_input()

    return "Just right!"
    
if __name__ == "__main__":
    main()







        
        
        
