import sys
# it will cause python to find sayings.py, read it from top to bottom, left to right. it is going to ignore the call to main this time. It is because it is wrap inside the conditional
# In this case, when we are importing a file, and not directly running it in the command line, main will not get call
from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])