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
    guess = guess_input(level)
    print(condition(level, guess))


def level_input():
     while True:
        try:     
            n = input("Level: ")
            n = int(n)
        except ValueError:
            continue 
        except:
            if n <= 0:
                continue

def guess_input(n):
    while True:
        try:
            # while n > 0:
                ans = random.randint(1,n)
                guess = input("Guess: ")
                guess = int(guess)
                break
        except ValueError:
            continue
        except:
            if guess <= 0:
                continue

def condition(level: int, guess: int):
     ans = random.randint(1,level)
     while guess != ans:
        if guess == ans:
            print("Just right")
        elif guess <= ans:
            print("Too small")
        elif guess >= ans:
            print("Too large")

if __name__ == "__main__":
    main()







        
        
        
