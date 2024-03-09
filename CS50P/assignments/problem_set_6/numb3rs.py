"""
1. we want to validate an ip is in a correct format, which is (#.#.#.#)
2. # should be number between 0 and 255 inlcusively
3. if an ip is in correct format, then show true, if not, then show false

"""

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^([0-9]+\.){3}[0-9]+$", ip):
        list_of_numbers = ip.split(".")
        for number in list_of_numbers:
            if int(number) < 0 or int(number) > 255:
                return False
        return True
    else:
        return  False



if __name__ == "__main__":
    main()