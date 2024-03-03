# original code
"""
sentence = input("Input: ")
for letter in sentence:
    if letter in ("a", "e", "i", "o", "u"):
        pass
    else:
        print(letter, end="")
"""

def main():
    shorten(input("Input: ").lower())


def shorten(word):
    whole_word = ""
    for letter in word:
        if letter in ("a", "e", "i", "o", "u"):
            pass
        else:
            # print(letter, end="")
            whole_word += letter
    return whole_word


if __name__ == "__main__":
    main()