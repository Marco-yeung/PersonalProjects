# user_input = input("Please enter your name: ")
# print(user_input.lower())

def get_input():
    while True:
        try:
            x = str(input("Please enter your name: "))
        except:
            pass
        else:
            break
    return x


def main():
    test = get_input()
    print(f"Here is your input {test}")

main()