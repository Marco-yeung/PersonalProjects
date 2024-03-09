"""
1. Use parse function expects a str of HTML as input, that extracts any Youtube URL that has an "src" attribute in "iframe element
2. return a shorter and shareable youtu.be as a string
3. assume that value of src would be surrounded by ""

assume URL would have exactly one, and if input does not contain any such URL at all, return None

steps
- confirm that is iframe and have src
- find text that inside "" after words "src="

- replace "youtube.com/embed" with "youtu.be"
- replace "www," with ""

"""


import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    ...


...


if __name__ == "__main__":
    main()