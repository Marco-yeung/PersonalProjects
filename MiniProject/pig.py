"""
create a function that let players roll a dice. make player be a variable so that multiple people can play
once there is a player reach 50, the game can ended

"""
# originally thinking of function of solving the problem
'''
def roll() -> int: 
    dice = random.randint(1,6)
    return dice


while True:
    players = input("how many players gonna play this game (2-4)")
    if players.isdigit():
        players = int(players)
        break
    else:
        print("Please enter valid input")
        continue



while True:
    rolling = roll()
    if rolling == 1:
        break
    else:
        player_score += rolling
'''

# sudden think of class method
'''
class PIG:
    def __init__(self, player_score):
        self.player_score = player_score
        player_score = 0

    def roll(self) -> int: 
        dice = random.randint(1,6)
        return dice
    
    def player(self) -> int:
        while True:
            players = input("how many players gonna play this game (2-4)")
            if players.isdigit():
                players = int(players)
                break
            else:
                print("Please enter valid input")
                continue
        return players
    
    def score(self) -> int:
        while True:
            rolling = roll()
            if rolling == 1:
                break
            else:
                player_score += rolling
        return player_score
    
'''
# then change it back to main function (oop) first, is just earier, later could try back class method
import random
def main():
    player_score_ls = []
    no_of_players = player()
    for _ in range(no_of_players):
        player_score_ls.append(0)
    for i in range(len(player_score_ls)):
        while player_score_ls[i] < 20:
            player_score_ls[i] = score(i+1, player_score_ls[i])
        # else:
        #     print(f"player {i} won. his score is {player_score_ls[i]}")
        #     break
        


def roll() -> int: 
        dice = random.randint(1,6)
        return dice
    
def player() -> int:
    while True:
        players = input("how many players gonna play this game (2-4)? ")
        if players.isdigit():
            players = int(players)
            break
        else:
            print("Please enter valid input")
            continue
    return players

def score(player_no, player_score) -> int:
    while True:
        keep_going = input(f"Player {player_no}, do you want to keep rolling another dice? (roll/hold) ").lower()
        if keep_going == "roll":
            rolling = roll()
            if rolling == 1:
                print(f"player {player_no} rolled a 1")
                break
            else:
                player_score += rolling
                print(f"Player {player_no} rolled a {rolling}. player {player_no} score: {player_score}")
                if player_score > 20:
                    print(f"Player {player_no} won. his score is {player_score}")
                    break
        elif keep_going == "hold":
            print(f"Player {player_no}: {player_score}")
            break

        else:
            print("Please enter valid input")
            continue
    return player_score

if __name__ == '__main__':
    main()