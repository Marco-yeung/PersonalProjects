import emoji
def main():
    test = convert(input("Input: "))
    print(f"Output: {test}")
    

def convert(x):
    return emoji.emojize(x)


if __name__ == "__main__":
    main()