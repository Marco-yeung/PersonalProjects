# my way of doing it, but in vain
"""
import re
def main():
    your_input= input("camelCase: ")
    answer = split_name(your_input)
    print(f"snake_case: {answer}")

def split_name(x):
    # name = input("what is your name? ")
        ls = re.sub( r"([A-Z])", r" \1", x).split()
        if len(ls) < 2:
            return x
        else:
             pass
        return ([print(c, sep= "_") for c in ls])


if __name__ == "__main__":
    main()
"""

# others answer from online
# link: https://www.youtube.com/watch?v=GBGLrrf_MXg
camelCase = input("camelCase: ")
print("snake_case: ", end = "")
for letter in camelCase:
    if letter.isupper():
        print("_" + letter.lower(), end = "")

    else:
        print(letter, end ="")
print()