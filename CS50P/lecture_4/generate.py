# a module would contain a bunch of functions that you would need to load to the computer memory to access it
# a module would be similar to a library
# import would allows you to import the contents of the functions from some module

# here we are importing everything from the module, so not just the functions random.choice() but a few other functions in random module
# a downside of it would be need to type random.choice(), random.this() everytime, because everything I am calling has to be associated within the scope of that module 
import random

# this would the function name choice into my current namespace into the scope of the file I am working in
from random import choice

coins = random.choice(["head", "tail"])
print(coins)

number = random.randint(1,10)
print(number)

# here we are shuffling the cards and print it, we can see a different sequence of the cards
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)