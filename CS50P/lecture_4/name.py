# sys.argv: it stands for argument factor, the list of all the words that human type in the command line

import sys

# sys.argvp[0] would be representing our file name, name.py, so here would be argv[1](our name)
# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("You have to few arguments")


# sys.exit() here could exit the program without printing anything below
if len(sys.argv) < 2:
    sys.exit("You have to few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("You have to many arguments")

# print("Hello, my name is", sys.argv[1])

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)
    
    
# A third party library in python would be called packages
# packages would be a module implemented in a folder, not just a file
# A package would be a library that we can install in our own PC

# pip would be a common command to install package online to our own PC
    

