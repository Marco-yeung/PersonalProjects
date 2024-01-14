# sys.argv: it stands for argument factor, the list of all the words that human type in the command line

import sys

# sys.argvp[0] would be representing our file name, name.py, so here would be argv[1](our name)
# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("You have to few arguments")

if len(sys.argv) < 2:
    print("You have to few arguments")
elif len(sys.argv) > 2:
    print("You have to many arguments")
else:
    print("Hello, my name is", sys.argv[1])
    

