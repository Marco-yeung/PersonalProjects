"""
1. implement a function that expects a line of text as input as input and return an int, the number of um appear in text, case-insensitively
2. the "um" needs to be a word by itself, not a substring

- need to write a testing file for it
"""


import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = re.findall(r"\b(um)\b", s, flags = re.IGNORECASE)
    return len(s)



if __name__ == "__main__":
    main()